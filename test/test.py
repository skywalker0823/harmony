import unittest
from app import app

class Test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tester(self):
        rv = self.app.get('/test')
        self.assertEqual(rv.data, b"get!")

if __name__ == '__main__':
    unittest.main()
