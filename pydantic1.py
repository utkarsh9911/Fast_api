from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Dict, Any, Optional, List, Annotated

## Pydantic 
class Patient(BaseModel):
    name: str    # required field
    surname: Annotated[str, Field(max_length=50, title="Surname", description="Enter the surname of the patient", examples=["yash","raj"])]  # required field with additional validation
    age: int     # required field
    allergies: Optional[List[str]]= None  # optional field, default is None
    email: EmailStr
    email1: str
    
    # weight: float
    # bmi: float
    @field_validator('email1')
    @classmethod
    def field_validator(cls , value):
        valid_domain = ['gmail.com', 'yahoo.com', 'outlook.com']
        domain =  value.split('@')[-1]
        if domain not in valid_domain:
            raise ValueError(f"Invalid email domain. Allowed domains are: {', '.join(valid_domain)}")
        return value

    

def insert_data(patient:Patient):
    print(patient.name)
    print(patient.surname)
    print(patient.age)
    print(patient.allergies)
    print(patient.email)
    print(patient.email1)
    print("inserted")



pateint_info = {"name": "yash", "age":20, "email": "rah@gmail.con", "surname":"yt", "email1":"gb@cc.com"}    # all the fields are required by default in pydnatic model ----> rquired to pass all the instance variables to the model

patient1 = Patient(**pateint_info)
insert_data(patient1)

### A field validator is a special function in Pydantic (especially Pydantic v2) used to validate or modify individual fields when a model is created. It is defined using the @field_validator decorator.