#Assignment 1

**Project Overview**
This project demonstrates the deployment of a microservice-based architecture across multiple Virtual Machines (VMs) using VirtualBox. The services communicate over a configured network and are containerized using Docker for scalability and portability.

**Technologies Used**
- **VirtualBox** (VM management)
- **Ubuntu 22.04** (OS for VMs)
- **Python & Flask** (Microservices framework)
- **Docker** (Containerization)
- **GitHub** (Version control)

**Project Setup & Execution**

**1. Setup Virtual Machines**
1. Install VirtualBox and create two VMs (`vm1-user-service` and `vm2-order-service`).
2. Configure network settings: 
   - Adapter 1: NAT (for internet access)
   - Adapter 2: Host-Only Adapter (for inter-VM communication)
3. Assign static IPs to VMs and verify connectivity using `ping`.

**2. Deploy Microservices**

**User Service (VM1)**
```bash
sudo apt update && sudo apt install -y python3 python3-pip
pip3 install flask
```
Create `app.py`:
```python
from flask import Flask, jsonify

app = Flask(__name__)
users = {1: {"name": "Alice", "email": "alice@example.com"}}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(users.get(user_id, {"error": "User not found"}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
```
Run the service:
```bash
python3 app.py
```

**Order Service (VM2)**
```bash
sudo apt update && sudo apt install -y python3 python3-pip
pip3 install flask requests
```
Create `app.py`:
```python
from flask import Flask, jsonify
import requests

app = Flask(__name__)
orders = {101: {"user_id": 1, "product": "Laptop"}}
USER_SERVICE_URL = "http://192.168.1.101:6001/users/"

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id, None)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    user_response = requests.get(f"{USER_SERVICE_URL}{order['user_id']}")
    order["user_details"] = user_response.json()
    return jsonify(order)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)
```
Run the service:
```bash
python3 app.py
```

**3. Deploy Microservices Using Docker**

**Install Docker**
```bash
sudo apt update && sudo apt install -y docker.io
```

**Build & Run User Service (VM1)**
Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python", "app.py"]
```
```bash
docker build -t user-service .
docker run -d -p 6000:6000 user-service
```

**Build & Run Order Service (VM2)**
Create `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask requests
CMD ["python", "app.py"]
```
```bash
docker build -t order-service .
docker run -d -p 6001:6001 order-service
```

**4. Testing the Deployment**
- Test User Service:
```bash
curl http://192.168.196.189:6000/users/1
```
- Test Order Service:
```bash
curl http://192.168.196.189:6001/orders/101
```

**Repository & Demo**
- **Source Code**: https://github.com/IITNNidhiRani/VCC_Assigment1.git
- **Video Demonstration**: [Demo Video Link](https://your-demo-link.com)

**Conclusion**
This project successfully demonstrates the deployment of a distributed microservice architecture across multiple VMs with containerized services. This setup enhances scalability, modularity, and ease of deployment.
---
