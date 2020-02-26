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

    # Functions for testing mountain.py - Luke
    def test_mountain_to_string(self):
        print('TODO')

    def test_mountain_get_name(self):
        print('TODO')

    def test_mountain_get_location(self):
        print('TODO')

    def test_mountain_get_trails(self):
        print('TODO')

    def test_mountain_get_lifts(self):
        print('TODO')

    def test_mountain_get_lodges(self):
        print('TODO')

    def test_mountain_trail_status(self):
        print('TODO')

    def test_mountain_lift_status(self):
        print('TODO')

    def test_mountain_lodge_status(self):
        print('TODO')

    def test_mountain_add_trail(self):
        print('TODO')

    def test_mountain_remove_trail(self):
        print('TODO')

    def test_mountain_add_lift(self):
        print('TODO')

    def test_mountain_remove_lift(self):
        print('TODO')

    def test_mountain_add_lodge(self):
        print('TODO')

    def test_mountain_remove_lodge(self):
        print('TODO')

    # Functions for testing trail.py - Matt
    def test_trail_to_string(self):
        print('TODO')

    def test_trail_get_name(self):
        print('TODO')

    def test_trail_get_difficulty(self):
        print('TODO')

    def test_trail_get_groomed(self):
        print('TODO')

    def test_trail_get_lifts(self):
        print('TODO')

    def test_trail_get_trail(self):
        print('TODO')

    def test_trail_add_lift(self):
        print('TODO')

    def test_trail_remove_lift(self):
        print('TODO')

    # Functions for testing lift.py - Luke
    def test_lift_to_string(self):
        print('TODO')

    def test_lift_get_name(self):
        print('TODO')

    def test_lift_get_running(self):
        print('TODO')

    def test_lift_get_trails(self):
        print('TODO')

    def test_lift_run_lift(self):
        print('TODO')

    def test_lift_stop_lift(self):
        print('TODO')

    def test_lift_add_trail(self):
        print('TODO')

    def test_lift_remove_trail(self):
        print('TODO')

    # Functions for testing lodge.py - Matt
    def test_lodge_to_string(self):
        print('TODO')

    def test_lodge_get_name(self):
        print('TODO')

    def test_lodge_get_open(self):
        print('TODO')

    def test_lodge_get_food(self):
        print('TODO')

    def test_lodge_open_lodge(self):
        print('TODO')

    def test_lodge_close_lodge(self):
        print('TODO')

    def test_lodge_open_food(self):
        print('TODO')

    def test_lodge_close_food(self):
        print('TODO')

if __name__ == "__main__":
    unittest.main()
