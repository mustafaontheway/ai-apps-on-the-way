from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# le -> less than or equal to
# lt -> less than

class Employee(BaseModel):
    emp_id: int = Field(le=9999, description="Employee ID must be 4 digits!")
    name: str = Field(min_length=5, max_length=50)
    department: str = Field(min_length=2, max_length=20)
    salary: int = Field(le=999999, description="Salary amount should be realistic:)")
    married: bool
    
    
EMPLOYEES: List[Employee] = [
    
    Employee(emp_id=4296, name="Ayhan Bilir", department="Finance", salary=42000, married=True),
    Employee(emp_id=3254, name="Hakan Kaya", department="FinTech", salary=87000, married=True),
    Employee(emp_id=2154, name="Bengü İyi", department="HR", salary=30000, married=False),
    Employee(emp_id=6874, name="Kul Yapıcı", department="Accounting", salary=32500, married=False),
    Employee(emp_id=1100, name="Bumin Burada", department="Marketing", salary=66800, married=True),
]

@app.get("/employees")
async def get_employees() -> List[Employee]:
    return EMPLOYEES


@app.post("/create-employee")
async def create_employee(new_employee: Employee):
    EMPLOYEES.append(new_employee)
    return new_employee
