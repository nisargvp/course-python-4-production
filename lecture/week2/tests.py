from fastapi.testclient import TestClient
from pydantic import BaseModel
from main import app

import unittest


# $python -m unittest tests.py 
# $pytest tests.py

client = TestClient(app)

class TestHogwarts(unittest.TestCase):
    def test_get_member(self):
        response = client.get("/hogwarts/members/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"name": "Harry Potter", "house": "Gryffindor", "year": 5})

    def test_get_member_not_found(self):
        response = client.get("/hogwarts/members/999")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"error": "Member not found"})

    def test_add_member(self):
        response = client.post("/hogwarts/members", json={"name": "Ron Weasley", "house": "Gryffindor", "year": 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"success": True, "member_id": 2})

    def test_add_member_no_house(self):
        response = client.post("/hogwarts/members", json={"name": "Luna Lovegood", "year": 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"success": True, "member_id": 3})
    
    def test_get_class(self):
        response = client.post("/classes/", json={"id": 1, "name": "Potions", "professor": "Severus Snape", "description": "Learn how to brew various magical potions."})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Class created successfully"})
    
    def test_patch_class(self):
        response = client.patch("/classes/1", json={"name": "Conformal Predictions", "professor": "Aryabhatta"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Class partially updated successfully"})