from fastapi import FastAPI
from fastapi.testclient import TestClient
import unittest

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

client = TestClient(app)

class TestApp(unittest.TestCase):
    def test_read_item(self):
        response = client.get("/items/42")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 42, "q": None})

    def test_read_item_with_query_param(self):
        response = client.get("/items/42?q=test")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 42, "q": "test"})