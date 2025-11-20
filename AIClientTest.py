import requests
import json

IP = None
def generate_request(q,ip):
    data = '{ \\"question\\": \\"'+q+'\\" }'
    return f'curl -X POST http://{ip}:8000/ask -H "Content-Type: application/json" -d "{data}"'


IP = input("Δώσε server IP : ")
url = f"http://{IP}:8000/ask"
question = None
print("Καλώς ορίσατε στο chat μας . Γράψτε την ερώτηση σας ή 'έξοδος' για να βγείτε.")
while question != "έξοδος":
    question = input(">>> ")
    if question == "έξοδος":break
    data = {"question":question}
    response = json.loads(requests.post(url, json = data).text)["response"]
    print(response)