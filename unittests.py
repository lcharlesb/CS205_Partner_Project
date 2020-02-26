import unittest
import mountain
import trail
import lift
import lodge

class TestMountain(unittest.TestCase):
    mountain = None

    @classmethod
    def setUpClass(cls):
        print('setUpClass()')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass()')

    def setUp(self):
        print('setUp()')

    def tearDown(self):
        print('tearDown()')

if __name__ == "__main__":
    unittest.main()
