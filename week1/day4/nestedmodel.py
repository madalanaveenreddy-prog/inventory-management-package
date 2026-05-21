from pydantic import BaseModel, EmailStr
from typing import List, Dict


class Address(BaseModel):
    place: str
    pin: str
    state: str


class nestedmodel(BaseModel):
    name: str
    age: int
    email: EmailStr
    address: Address


def user_details(nested: nestedmodel):
    print(nested.name)
    print(nested.age)
    print(nested.address)


Address_dict = {"place": "hyderabad", "pin": "501508", "state": "telangane"}
address1 = Address(**Address_dict)

details = {
    "name": "naveen",
    "age": 23,
    "email": "naveen@gmail.com",
    "address": address1,
}
some = nestedmodel(**details)
# print(some.address.pin)
print(some.address.state)
