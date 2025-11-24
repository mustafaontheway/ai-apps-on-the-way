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
    
    Employee(4296, "Ayhan Bilir", "Finance", 42000, True),
    Employee(3254, "Hakan Kaya", "FinTech", 87000, True),
    Employee(2154, "Bengü İyi", "HR", 30000, False),
    Employee(6874, "Kul Yapıcı", "Accounting", 32500, False),
    Employee(1100, "Bumin Burada", "Marketing", 66800, True),
]

@app.get("/employees")
async def get_employees():
    return EMPLOYEES


