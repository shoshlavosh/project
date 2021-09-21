import unittest
import seed_database
from model import db
from server import app, connect_to_db

#running this file would call: setUp, test1, tearDown, setUp, test2, tearDown

class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Set up that runs before every test"""

        self.client = app.test_client() #uses Flask test client
        app.config['TESTING'] = True

    def tearDown(self):
        """Tear down that runs after every test"""

        db.session.close()
        db.drop_all() 

    def test_homepage(self):
        """Test whether user can access the homepage"""

        result = self.client.get("/")
        self.assertIn(b"Tenant Helper", result.data)

    def test_login(self):
        """Test whether login works"""

        result = self.client.post("/login", 
                                data={"email": "user0@test.com", "password": "test"},
                                follow_redirects=True)
        self.assertIn(b"Create", result.data)


if __name__ == "__main__":
    unittest.main()