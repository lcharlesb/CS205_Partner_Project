import unittest
import mountain
import trail
import lift
import lodge

class TestMountain(unittest.TestCase):
    mountain = None

    @classmethod
    def setUpClass(cls):
        # called one time, at beginning
        print('setUpClass()')

    @classmethod
    def tearDownClass(cls):
        # called one time, at end
        print('tearDownClass()')

    def setUp(self):
        # called before every test
        print('setUp()')

    def tearDown(self):
        # called after every test
        print('tearDown()')

if __name__ == "__main__":
    unittest.main()
