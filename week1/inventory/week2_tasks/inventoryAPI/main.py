import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser




# 1. Initialize FastAPI App
app = FastAPI(
    title="Production LLM Query API",
    description="FastAPI endpoint featuring structured prompt handling and financial cost tracking.",
    version="1.0.0"
)

# Enforce API Key checking
if "OPENAI_API_KEY" not in os.environ:
    # Setting a dummy placeholder if not set in the environment variables yet
    os.environ["private open api key"] = "mock-key-replace-with-your-real-key"

# 2. Define Pydantic Input/Output Schemas
class QueryRequest(BaseModel):
    topic: str = Field(..., description="The main subject matter you want the LLM to process.")
    persona: str = Field(default="Technical Writer", description="The role/persona the LLM should assume.")

class TokenUsage(BaseModel):
    input_tokens: int
    output_tokens: int
    total_tokens: int
    estimated_cost_usd: float

class QueryResponse(BaseModel):
    topic: str
    persona: str
    response_text: str
    usage: TokenUsage

# 3. Cost Calculation Helper Function
def calculate_gpt4o_mini_cost(input_tokens: int, output_tokens: int) -> float:
    """
    Calculates costs based on standard pricing per 1,000,000 tokens.
    Input/Prompt: $0.150 / 1M tokens
    Output/Completion: $0.600 / 1M tokens
    """
    input_cost = (input_tokens / 1_000_000) * 0.150
    output_cost = (output_tokens / 1_000_000) * 0.600
    return round(input_cost + output_cost, 6)

# 4. Define the POST Query Endpoint
@app.post("/api/v1/query", response_model=QueryResponse)
async def query_llm(payload: QueryRequest):
    # Enforce token validation check if using placeholder keys
    if os.environ.get("OPENAI_API_KEY") == "mock-key-replace-with-your-real-key":
        raise HTTPException(
            status_code=500, 
            detail="OpenAI API Key missing. Please configure OPENAI_API_KEY environment variable."
        )

    try:
        # A. Prompt Handling: Create structural delimiters and pass persona dynamically
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are an expert {persona}. Answer the user query comprehensively in exactly 3 sentences."),
            ("user", "Explain the following topic: {topic}")
        ])

        # B. Model Object Definition: Strict, deterministic settings for data pipelines
        model = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.0
        )

        # C. Construct the LCEL Chain Pipeline
        # Notice we don't attach the StrOutputParser here because we need the raw metadata object 
        # from the model block to harvest token usage numbers.
        chain = prompt_template | model

        # D. Execute the API workflow
        raw_response = chain.invoke({
            "persona": payload.persona,
            "topic": payload.topic
        })

        # E. Extract Metadata and Calculate Operational Costs
        metadata = raw_response.response_metadata.get("token_usage", {})
        prompt_tokens = metadata.get("prompt_tokens", 0)
        completion_tokens = metadata.get("completion_tokens", 0)
        total_tokens = metadata.get("total_tokens", 0)

        total_cost = calculate_gpt4o_mini_cost(prompt_tokens, completion_tokens)

        # F. Return the Standardized Structured Output
        return QueryResponse(
            topic=payload.topic,
            persona=payload.persona,
            response_text=raw_response.content,
            usage=TokenUsage(
                input_tokens=prompt_tokens,
                output_tokens=completion_tokens,
                total_tokens=total_tokens,
                estimated_cost_usd=total_cost
            )
        )

    except Exception as e:
        # Graceful Production Error Fallback
        raise HTTPException(status_code=500, detail=f"Internal LLM Processing Error: {str(e)}")

# 5. Health Check Endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "llm-query-api"}
