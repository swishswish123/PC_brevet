from app import app

import unittest

class BasicTest(unittest.TestCase):

    def test_home_valid(self):
        tester = app.test_client(self)
        response = tester.get('/acceuil')
        self.assertEqual(response.status_code, 200)


if __name__ == '__maim__':
    unittest.main()