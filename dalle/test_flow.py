import requests

API_URL = "https://flowiseai-railway-production-70cb.up.railway.app/api/v1/prediction/2b142d01-c9cf-4a48-9da7-e2ed62f29003"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Hey, how are you?",
    "overrideConfig": {
        "temperature": "0.9",
    }
})

