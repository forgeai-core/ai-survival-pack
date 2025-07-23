from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="LabGPT", description="ForgeAI’s Lab Generator Microservice", version="0.1")

class LabRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_lab(request: LabRequest):
    prompt = request.prompt.lower()

    if "docker" in prompt:
        return {"output": generate_docker(prompt)}
    elif "terraform" in prompt:
        return {"output": generate_terraform(prompt)}
    elif "ansible" in prompt:
        return {"output": generate_ansible(prompt)}
    else:
        raise HTTPException(status_code=400, detail="Prompt must contain 'docker', 'terraform', or 'ansible'.")

def generate_docker(prompt):
    return f"""```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```"""

def generate_terraform(prompt):
    return f"""```hcl
provider "aws" {{
  region = "us-west-2"
}}

resource "aws_instance" "lab_vm" {{
  ami           = "ami-0abcdef1234567890"
  instance_type = "t2.micro"
}}
```"""

def generate_ansible(prompt):
    return f"""```yaml
- name: Install and start nginx
  hosts: all
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
    - name: Start nginx
      service:
        name: nginx
        state: started
        enabled: true
```"""
