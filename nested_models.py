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
print(patient1)

print(patient1.adress.city)
print(patient1.adress.state)