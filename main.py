from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()


@app.get("/")
def hello():
    return {'message': 'a patient management system'}


@app.get("/about")
def about():
    return {'message': 'This is a simple FastAPI application.'}

def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/view")
def view():
    data = load_data()
    return data 

# path parmaeters are dynamic segement of url path used to specify a resource
# path function is used to get the patient data by id
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The id of the patient to view", example="POO1")):
    data = load_data()
    if  patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")



# Query parameters are used to filter the data first choose name and then order like ascending or descending
## ... show it is required parameter
@app.get('/sort')
def sort_patient(sort_by: str = Query(..., description="sort on the basis if heigh and weight or bmi"),order: str = Query('asc', description="order of sorting", example="asc")):
    data = load_data()
    valid_field = ['height', 'weight', 'bmi']
    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail="Invalid sort field. Choose from 'height', 'weight', or 'bmi'.")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Choose 'asc' or 'desc'.")
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse= True if order== 'desc' else False)
    return sorted_data






    