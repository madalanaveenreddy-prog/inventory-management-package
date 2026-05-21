from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated


class patient(BaseModel):
    name: str
    age: int = Field(gt=0)
    email: EmailStr
    linked_url: AnyUrl
    weight: float = Field(gt=10)
    married: bool
    diseases: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age < 60 and "emergency" not in model.contact_details:
            raise ValueError("pateints older than 60 ust have emergency contact")


def pateint_insert_info(pateint: patient):
    print(pateint.name)
    print(pateint.age)
    print(pateint.weight)
    print(pateint.married)
    print(pateint.diseases)
    print(pateint.contact_details)
    print(pateint.email)
    print(pateint.linked_url)
    print("inserted data")


def pateint_update_info(pateint: patient):
    # print(pateint.name)
    # print(pateint.age)
    print("pateint data updated")


pateint_info = {
    "name": "naveen",
    "age": 89,
    "weight": 23.4,
    "linked_url": "http://linkedin.com",
    "email": "naveen@gmail.com",
    "married": True,
    "contact_details": {"phone": "23456789"},
}
some_pateint = patient(**pateint_info)
pateint_insert_info(some_pateint)
pateint_update_info(some_pateint)
