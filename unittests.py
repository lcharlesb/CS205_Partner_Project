import unittest
from unittest import mock
import io

import mountain
import trail
import lift
import lodge

class TestMountain(unittest.TestCase):
    mountain = None

    @classmethod
    def setUpClass(self):
        # called one time, at beginning
        print('setUpClass()')

        #mountain created
        self.mountain = mountain.Mountain("Bolton Valley", "Bolton, VT")

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
        wilderness = lift.Lift("Wilderness", False)
        timberline = lift.Lift("Timberline", True)

        #lodges created
        base_lodge = lodge.Lodge("Base", True, True)
        timberline_lodge = lodge.Lodge("Timberline", False, False)

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
        self.mountain.add_trail(vista_glades)
        self.mountain.add_trail(alta_vista)
        self.mountain.add_trail(shermans_pass)
        self.mountain.add_trail(cobrass)
        self.mountain.add_trail(preacher)
        self.mountain.add_trail(bolton_outlaw)
        self.mountain.add_trail(cougar)
        self.mountain.add_trail(lost_boyz)
        self.mountain.add_trail(adams_solitude)

        #lifts added to mountain
        self.mountain.add_lift(vista)
        self.mountain.add_lift(wilderness)
        self.mountain.add_lift(timberline)

        #lodges added to mountain
        self.mountain.add_lodge(base_lodge)
        self.mountain.add_lodge(timberline_lodge)

    @classmethod
    def tearDownClass(self):
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
        mountain_to_string = "Bolton Valley, Bolton, VT"
        returned_string = self.mountain.to_string()

        self.assertEqual(mountain_to_string, returned_string)

    def test_mountain_get_name(self):
        mountain_name = "Bolton Valley"
        returned_string = self.mountain.get_name()

        self.assertEqual(mountain_name, returned_string)

    def test_mountain_get_location(self):
        mountain_location = "Bolton, VT"
        returned_string = self.mountain.get_location()

        self.assertEqual(mountain_location, returned_string)

    def test_mountain_get_trails(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.get_trails()

        expected_print_statement = "Vista Glades\nAlta Vista\nSherman's Pass\nCobrass\nPreacher\nBolton Outlaw\nCougar\nLost Boyz\nAdam's Solitude\nAdded Trail\n"
        assert temp_stdout.getvalue() == expected_print_statement

    def test_mountain_get_lifts(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.get_lifts()

        expected_print_statement = "Vista\nWilderness\nTimberline\nAdded Lift\n"
        assert temp_stdout.getvalue() == expected_print_statement

    def test_mountain_get_lodges(self):
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.get_lodges()

        expected_print_statement = "Base\nTimberline\nAdded Lodge\n"
        assert temp_stdout.getvalue() == expected_print_statement

    def test_mountain_trail_status(self):
        # Test for a found trail, ungroomed.
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.trail_status("Vista Glades")

        expected_print_statement = "Vista Glades is currently ungroomed.\n"
        assert temp_stdout.getvalue() == expected_print_statement

        # Test for a found trail, groomed.
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.trail_status("Alta Vista")

        expected_print_statement = "Alta Vista is currently groomed.\n"
        assert temp_stdout.getvalue() == expected_print_statement

        # Test for an unfound trail.
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.trail_status("Fake Trail")

        expected_print_statement = "No trail by the name of Fake Trail exists on this mountain.\n"
        assert temp_stdout.getvalue() == expected_print_statement

    def test_mountain_lift_status(self):
        # Test for a found lift, not running.
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.lift_status("Wilderness")

        expected_print_statement = "Wilderness is currently not running.\n"
        assert temp_stdout.getvalue() == expected_print_statement

        # Test for a found lift, running.
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.lift_status("Vista")

        expected_print_statement = "Vista is currently running.\n"
        assert temp_stdout.getvalue() == expected_print_statement

        # Test for an unfound lift.
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.lift_status("Fake Lift")

        expected_print_statement = "No lift by the name of Fake Lift exists on this mountain.\n"
        assert temp_stdout.getvalue() == expected_print_statement

    def test_mountain_lodge_status(self):
        # Test for a found lodge, open and serving food.
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.lodge_status("Base")

        expected_print_statement = "Base is currently open and serving food.\n"
        assert temp_stdout.getvalue() == expected_print_statement

        # Test for a found lodge, closed and not serving food.
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.lodge_status("Timberline")

        expected_print_statement = "Timberline is currently closed and not serving food.\n"
        assert temp_stdout.getvalue() == expected_print_statement

        # Test for an unfound lodge.
        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            self.mountain.lodge_status("Fake Lodge")

        expected_print_statement = "No lodge by the name of Fake Lodge exists on this mountain.\n"
        assert temp_stdout.getvalue() == expected_print_statement

    def test_mountain_add_trail(self):
        added_trail = trail.Trail("Added Trail")
        self.mountain.add_trail(added_trail)
        trail_exists_in_mountain = False
        for curr_trail in self.mountain.trails:
            if curr_trail.name == "Added Trail":
                trail_exists_in_mountain = True

        self.assertTrue(trail_exists_in_mountain)

    def test_mountain_remove_trail(self):
        self.mountain.remove_trail("Added Trail")
        trail_exists_in_mountain = False
        for curr_trail in self.mountain.trails:
            if curr_trail.name == "Added Trail":
                trail_exists_in_mountain = True

        self.assertFalse(trail_exists_in_mountain)

    def test_mountain_add_lift(self):
        added_lift = lift.Lift("Added Lift")
        self.mountain.add_lift(added_lift)
        lift_exists_in_mountain = False
        for curr_lift in self.mountain.lifts:
            if curr_lift.name == "Added Lift":
                lift_exists_in_mountain = True

        self.assertTrue(lift_exists_in_mountain)

    def test_mountain_remove_lift(self):
        self.mountain.remove_lift("Added Lift")
        lift_exists_in_mountain = False
        for curr_lift in self.mountain.lifts:
            if curr_lift.name == "Added Lift":
                lift_exists_in_mountain = True

        self.assertFalse(lift_exists_in_mountain)

    def test_mountain_add_lodge(self):
        added_lodge = lodge.Lodge("Added Lodge")
        self.mountain.add_lodge(added_lodge)
        lodge_exists_in_mountain = False
        for curr_lodge in self.mountain.lodges:
            if curr_lodge.name == "Added Lodge":
                lodge_exists_in_mountain = True

        self.assertTrue(lodge_exists_in_mountain)

    def test_mountain_remove_lodge(self):
        self.mountain.remove_lodge("Added Lodge")
        lodge_exists_in_mountain = False
        for curr_lodge in self.mountain.lodges:
            if curr_lodge.name == "Added Lodge":
                lodge_exists_in_mountain = True

        self.assertFalse(lodge_exists_in_mountain)

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
