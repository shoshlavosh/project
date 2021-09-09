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

###############################################
# Running Doctests In a Unit Test

# Once you start to do this a lot, you may want to be able to have a single unittest-based file that you can run that finds all of your tests, even doctests.

# With the unittest framework, you can load all tests by defining a function called load_tests. You can see an example of this in our demo code, at the end of test_arithmetic.py

# test_arithmetic.py
    # def load_tests(loader, tests, ignore):
    #     """Also run our doctests and file-based doctests.

    #     This function name, ``load_tests``, is required.
    #     """

    #     tests.addTests(doctest.DocTestSuite(arithmetic))
    #     tests.addTests(doctest.DocFileSuite("tests.txt"))
    #     return tests


    #example doc test:
    # def only_vowels(llist):
    # """ Return a new LinkedList object containing nodes with the strings from
    # the original linked list that start with vowels.

    #     >>> llist = LinkedList()
    #     >>> llist.add_node("cherry")
    #     >>> llist.add_node("berry")
    #     >>> llist.add_node("apple")
    #     >>> llist.add_node("durian")
    #     >>> llist.add_node("elderberry")
    #     >>> new_llist = only_vowels(llist)
    #     >>> new_llist.head.data == "apple"
    #     True
    #     >>> new_llist.head.next.data == "elderberry"
    #     True
    #     >>> new_llist.tail.data == "elderberry"
    #     True
    # """

    # if __name__ == "__main__":
    #     import doctest

    #     print()
    #     result = doctest.testmod()
    #     if not result.failed:
    #         print("ALL TESTS PASSED. GOOD WORK!")
    #     print()




if __name__ == "__main__":
    unittest.main()