from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class patient(BaseModel):
    name: Annotated[
        str,
        Field(
            maxl_ength=45,
            title="Name of the pateint ",
            description="give the pateint name",
            examples=["naveen", "rahul"],
        ),
    ]
    age: int = Field(gt=0)
    email: EmailStr
    linked_url: AnyUrl
    weight: float = Field(gt=10)
    married: bool
    diseases: Optional[List[str]] = None
    contact_details: Dict[str, str]


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
    "age": 3,
    "weight": 23.4,
    "linked_url": "http://linkedin.com",
    "email": "naveen@gmail.com",
    "married": True,
    "contact_details": {"phone": "23456789"},
}
some_pateint = patient(**pateint_info)
pateint_insert_info(some_pateint)
pateint_update_info(some_pateint)
