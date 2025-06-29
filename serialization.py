from pydantic import BaseModel


class Adress(BaseModel):
    city : str
    state : str
    pincode : str

class Patient(BaseModel):
    name: str
    gender: str
    adress: Adress


address_dict = {'city':'mangol', 'state': 'delhi', 'pincode': '110084'}
adrees1 = Adress(**address_dict)

patient_info = {'name':'yash', 'gender':'male', 'adress': adrees1}
patient1 = Patient(**patient_info)

# temp = patient1.model_dump()  # Serialize the model to a JSON string
temp2 = patient1.model_dump(exclude={'adress': ['city', 'state']})  # Exclude specific fields
# print(temp)
# print(type(temp))


print(temp2)
# print
