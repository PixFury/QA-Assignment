import requests
import unittest

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.frontend_url = "http://<Minikube IP>:30001" #Edit Port Number and Minikube IP 

    def test_greeting_message(self):
        response = requests.get(self.frontend_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Testing", response.text) 

if __name__ == "__main__":
    unittest.main()