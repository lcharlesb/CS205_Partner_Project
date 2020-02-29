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

        #mountain created
        cls.mountain = mountain.Mountain("Bolton Valley", "Bolton, VT")

        #trails created
        vista_glades = trail.Trail("Vista Glades", 3, False)
        alta_vista = trail.Trail("Alta Vista", 2, True)
        shermans_pass = trail.Trail("Sherman's Pass", 1, True)
        cobrass = trail.Trail("Cobrass", 2, False)
        preacher = trail.Trail("Preacher", 4, False)
        bolton_outlaw = trail.Trail("Bolton Outlaw", 3, False)
        cougar = trail.Trail("Cougar", 3, False)
        lost_boyz = trail.Trail("Lost Boyz", 4, False)
        adams_solitude = trail.Trail("Adam's Solitude", 4, False)

        #lifts created
        vista = lift.Lift("Vista", True)
        wilderness = lift.Lift("Wilderness", True)
        timberline = lift.Lift("Timberline", True)

        #lodges created
        base_lodge = lodge.Lodge("Base", True, True)
        timberline_lodge = lodge.Lodge("Timberline", True, True)

        #trails added to lifts
        vista.add_trail(vista_glades)
        vista.add_trail(alta_vista)
        vista.add_trail(shermans_pass)
        vista.add_trail(cobrass)
        vista.add_trail(preacher)
        wilderness.add_trail(bolton_outlaw)
        wilderness.add_trail(cougar)
        timberline.add_trail(lost_boyz)
        timberline.add_trail(adams_solitude)

        #lifts added to trails
        vista_glades.add_lift(vista)
        alta_vista.add_lift(vista)
        shermans_pass.add_lift(vista)
        cobrass.add_lift(vista)
        preacher.add_lift(vista)
        bolton_outlaw.add_lift(wilderness)
        cougar.add_lift(wilderness)
        lost_boyz.add_lift(timberline)
        adams_solitude.add_lift(timberline)

        #trails added to mountain
        cls.mountain.add_trail(vista_glades)
        cls.mountain.add_trail(alta_vista)
        cls.mountain.add_trail(shermans_pass)
        cls.mountain.add_trail(cobrass)
        cls.mountain.add_trail(preacher)
        cls.mountain.add_trail(bolton_outlaw)
        cls.mountain.add_trail(cougar)
        cls.mountain.add_trail(lost_boyz)
        cls.mountain.add_trail(adams_solitude)

        #lifts added to mountain
        cls.mountain.add_lift(vista)
        cls.mountain.add_lift(wilderness)
        cls.mountain.add_lift(timberline)

        #lodges added to mountain
        cls.mountain.add_lodge(base_lodge)
        cls.mountain.add_lodge(timberline_lodge)

    @classmethod
    def tearDownClass(cls):
        # called one time, at end
        print('tearDownClass()')

    def setUp(cls):
        # called before every test
        print('setUp()')

    def tearDown(cls):
        # called after every test
        print('tearDown()')

    # Functions for testing mountain.py - Luke
    def test_mountain_to_string(cls):
        print('TODO')

    def test_mountain_get_name(cls):
        print('TODO')

    def test_mountain_get_location(cls):
        print('TODO')

    def test_mountain_get_trails(cls):
        print('TODO')

    def test_mountain_get_lifts(cls):
        print('TODO')

    def test_mountain_get_lodges(cls):
        print('TODO')

    def test_mountain_trail_status(cls):
        print('TODO')

    def test_mountain_lift_status(cls):
        print('TODO')

    def test_mountain_lodge_status(cls):
        print('TODO')

    def test_mountain_add_trail(cls):
        print('TODO')

    def test_mountain_remove_trail(cls):
        print('TODO')

    def test_mountain_add_lift(cls):
        print('TODO')

    def test_mountain_remove_lift(cls):
        print('TODO')

    def test_mountain_add_lodge(cls):
        print('TODO')

    def test_mountain_remove_lodge(cls):
        print('TODO')

    # Functions for testing trail.py - Matt
    def test_trail_to_string(cls):
        print('TODO')

    def test_trail_get_name(cls):
        print('TODO')

    def test_trail_get_difficulty(cls):
        print('TODO')

    def test_trail_get_groomed(cls):
        print('TODO')

    def test_trail_get_lifts(cls):
        print('TODO')

    def test_trail_get_trail(cls):
        print('TODO')

    def test_trail_add_lift(cls):
        print('TODO')

    def test_trail_remove_lift(cls):
        print('TODO')

    # Functions for testing lift.py - Luke
    def test_lift_to_string(cls):
        print('TODO')

    def test_lift_get_name(cls):
        print('TODO')

    def test_lift_get_running(cls):
        print('TODO')

    def test_lift_get_trails(cls):
        print('TODO')

    def test_lift_run_lift(cls):
        print('TODO')

    def test_lift_stop_lift(cls):
        print('TODO')

    def test_lift_add_trail(cls):
        print('TODO')

    def test_lift_remove_trail(cls):
        print('TODO')

    # Functions for testing lodge.py - Matt
    def test_lodge_to_string(cls):
        print('TODO')

    def test_lodge_get_name(cls):
        print('TODO')

    def test_lodge_get_open(cls):
        print('TODO')

    def test_lodge_get_food(cls):
        print('TODO')

    def test_lodge_open_lodge(cls):
        print('TODO')

    def test_lodge_close_lodge(cls):
        print('TODO')

    def test_lodge_open_food(cls):
        print('TODO')

    def test_lodge_close_food(cls):
        print('TODO')

if __name__ == "__main__":
    unittest.main()
