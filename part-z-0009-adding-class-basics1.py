from fastapi import FastAPI

app = FastAPI()

class Employee:
    emp_id: int
    name: str
    department: str
    salary: int
    married: bool
    
    def __init__(self, emp_id, name, department, salary, married):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.married = married

EMPLOYEES = [

]

@app.get("/employees")
async def get_employees():
    return EMPLOYEES


