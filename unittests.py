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
        # Called one time, at beginning
        print('setUpClass()')

        # Mountain created
        self.mountain = mountain.Mountain("Bolton Valley", "Bolton, VT")

        # Trails created
        vista_glades = trail.Trail("Vista Glades", 3, False)
        alta_vista = trail.Trail("Alta Vista", 2, True)
        shermans_pass = trail.Trail("Sherman's Pass", 1, True)
        cobrass = trail.Trail("Cobrass", 2, False)
        preacher = trail.Trail("Preacher", 4, False)
        bolton_outlaw = trail.Trail("Bolton Outlaw", 3, False)
        cougar = trail.Trail("Cougar", 3, False)
        lost_boyz = trail.Trail("Lost Boyz", 4, False)
        adams_solitude = trail.Trail("Adam's Solitude", 4, False)

        # Lifts created
        vista = lift.Lift("Vista", True)
        wilderness = lift.Lift("Wilderness", False)
        timberline = lift.Lift("Timberline", True)

        # Lodges created
        base_lodge = lodge.Lodge("Base", True, True)
        timberline_lodge = lodge.Lodge("Timberline", False, False)

        # Trails added to lifts
        vista.add_trail(vista_glades)
        vista.add_trail(alta_vista)
        vista.add_trail(shermans_pass)
        vista.add_trail(cobrass)
        vista.add_trail(preacher)
        wilderness.add_trail(bolton_outlaw)
        wilderness.add_trail(cougar)
        timberline.add_trail(lost_boyz)
        timberline.add_trail(adams_solitude)

        # Lifts added to trails
        vista_glades.add_lift(vista)
        alta_vista.add_lift(vista)
        shermans_pass.add_lift(vista)
        cobrass.add_lift(vista)
        preacher.add_lift(vista)
        bolton_outlaw.add_lift(wilderness)
        cougar.add_lift(wilderness)
        lost_boyz.add_lift(timberline)
        adams_solitude.add_lift(timberline)

        # Trails added to mountain
        self.mountain.add_trail(vista_glades)
        self.mountain.add_trail(alta_vista)
        self.mountain.add_trail(shermans_pass)
        self.mountain.add_trail(cobrass)
        self.mountain.add_trail(preacher)
        self.mountain.add_trail(bolton_outlaw)
        self.mountain.add_trail(cougar)
        self.mountain.add_trail(lost_boyz)
        self.mountain.add_trail(adams_solitude)

        # Lifts added to mountain
        self.mountain.add_lift(vista)
        self.mountain.add_lift(wilderness)
        self.mountain.add_lift(timberline)

        # Lodges added to mountain
        self.mountain.add_lodge(base_lodge)
        self.mountain.add_lodge(timberline_lodge)

    @classmethod
    def tearDownClass(self):
        # Called one time, at end
        print('tearDownClass()')

    def setUp(self):
        # Called before every test
        print('setUp()')

    def tearDown(self):
        # Called after every test
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
        temp_trail = trail.Trail("Temp Trail")
        returned_string = temp_trail.to_string()

        self.assertEqual("Temp Trail", returned_string)

    def test_trail_get_name(self):
        temp_trail = trail.Trail("Temp Trail")
        returned_string = temp_trail.get_name()

        self.assertEqual("Temp Trail", returned_string)

    def test_trail_get_difficulty(self):
        temp_trail = trail.Trail("Temp Trail", 1, False)
        returned_integer = temp_trail.get_difficulty()

        self.assertEqual(1, returned_integer)

    def test_trail_get_groomed(self):
        # Test for groomed trail.
        temp_trail = trail.Trail("Temp Trail", 0, True)
        returned_boolean = temp_trail.get_groomed()

        self.assertEqual(True, returned_boolean)

        # Test for ungroomed trail.
        temp_trail = trail.Trail("Temp Trail", 0, False)
        returned_boolean = temp_trail.get_groomed()

        self.assertEqual(False, returned_boolean)

    def test_trail_get_lifts(self):
        lift1 = lift.Lift("Lift1")
        lift2 = lift.Lift("Lift2")

        trail1 = trail.Trail("Trail1")
        trail1.add_lift(lift1)
        trail1.add_lift(lift2)

        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            trail1.get_lifts()

        expected_print_statement = "Lift1\nLift2\n"
        assert temp_stdout.getvalue() == expected_print_statement

    def test_trail_groom_trail(self):
        trail1 = trail.Trail("Trail1", 0, False)
        trail1.groom_trail()

        trail_is_groomed = trail1.groomed

        self.assertTrue(trail_is_groomed)

    def test_trail_add_lift(self):
        added_lift = lift.Lift("Added Lift")
        trail1 = trail.Trail("Trail1")
        trail1.add_lift(added_lift)
        lift_exists_in_trail = False
        for curr_lift in trail1.lifts:
            if curr_lift.name == "Added Lift":
                lift_exists_in_trail = True

        self.assertTrue(lift_exists_in_trail)

    def test_trail_remove_lift(self):
        added_lift = lift.Lift("Added Lift")
        trail1 = trail.Trail("Trail1")
        trail1.add_lift(added_lift)
        trail1.remove_lift("Added Lift")
        lift_exists_in_trail = False
        for curr_lift in trail1.lifts:
            if curr_lift.name == "Added Lift":
                lift_exists_in_trail = True

        self.assertFalse(lift_exists_in_trail)

    # Functions for testing lift.py - Luke
    def test_lift_to_string(self):
        temp_lift = lift.Lift("Temp Lift")
        returned_string = temp_lift.to_string()

        self.assertEqual("Temp Lift", returned_string)

    def test_lift_get_name(self):
        temp_lift = lift.Lift("Temp Lift")
        returned_string = temp_lift.get_name()

        self.assertEqual("Temp Lift", returned_string)

    def test_lift_get_running(self):
        # Test for running lift.
        running_lift = lift.Lift("Temp Lift", True)
        returned_boolean = running_lift.get_running()

        self.assertEqual(True, returned_boolean)

        # Test for not running lift.
        not_running_lift = lift.Lift("Temp Lift", False)
        returned_boolean = not_running_lift.get_running()

        self.assertEqual(False, returned_boolean)

    def test_lift_get_trails(self):
        trail1 = trail.Trail("Trail1")
        trail2 = trail.Trail("Trail2")

        lift1 = lift.Lift("Lift1")
        lift1.add_trail(trail1)
        lift1.add_trail(trail2)

        with mock.patch('sys.stdout', new=io.StringIO()) as temp_stdout:
            lift1.get_trails()

        expected_print_statement = "Trail1\nTrail2\n"
        assert temp_stdout.getvalue() == expected_print_statement

    def test_lift_run_lift(self):
        lift1 = lift.Lift("Lift1", False)
        lift1.run_lift()

        lift_is_running = lift1.running

        self.assertTrue(lift_is_running)

    def test_lift_stop_lift(self):
        lift1 = lift.Lift("Lift1", True)
        lift1.stop_lift()

        lift_is_not_running = lift1.running

        self.assertFalse(lift_is_not_running)

    def test_lift_add_trail(self):
        added_trail = trail.Trail("Added Trail")
        lift1 = lift.Lift("Lift1")
        lift1.add_trail(added_trail)
        trail_exists_in_lift = False
        for curr_trail in lift1.trails:
            if curr_trail.name == "Added Trail":
                trail_exists_in_lift = True

        self.assertTrue(trail_exists_in_lift)

    def test_lift_remove_trail(self):
        added_trail = trail.Trail("Added Trail")
        lift1 = lift.Lift("Lift1")
        lift1.add_trail(added_trail)
        lift1.remove_trail("Added Trail")
        trail_exists_in_lift = False
        for curr_trail in lift1.trails:
            if curr_trail.name == "Added Trail":
                trail_exists_in_lift = True

        self.assertFalse(trail_exists_in_lift)

    # Functions for testing lodge.py - Matt
    def test_lodge_to_string(self):
        temp_lodge = lodge.Lodge("Temp Lodge")
        returned_string = temp_lodge.to_string()

        self.assertEqual("Temp Lodge", returned_string)

    def test_lodge_get_name(self):
        temp_lodge = lodge.Lodge("Temp Lodge")
        returned_string = temp_lodge.get_name()

        self.assertEqual("Temp Lodge", returned_string)

    def test_lodge_get_open(self):
        # Test for open lodge.
        temp_lodge = lodge.Lodge("Temp Lodge", True, False)
        returned_boolean = temp_lodge.get_open()

        self.assertEqual(True, returned_boolean)
        
        # Test for closed lodge.
        temp_lodge = lodge.Lodge("Temp Lodge", False, False)
        returned_boolean = temp_lodge.get_open()

        self.assertEqual(False, returned_boolean)

    def test_lodge_get_food(self):
        # Test for serving food.
        temp_lodge = lodge.Lodge("Temp Lodge", True, True)
        returned_boolean = temp_lodge.get_food()

        self.assertEqual(True, returned_boolean)

        # Test for not serving food.
        temp_lodge = lodge.Lodge("Temp Lodge", True, False)
        returned_boolean = temp_lodge.get_food()

        self.assertEqual(False, returned_boolean)

    def test_lodge_open_lodge(self):
        lodge1 = lodge.Lodge("Lodge1", False, False)
        lodge1.open_lodge()

        lodge_is_open = lodge1.open

        self.assertTrue(lodge_is_open)

    def test_lodge_close_lodge(self):
        lodge1 = lodge.Lodge("Lodge1", True, False)
        lodge1.close_lodge()

        lodge_is_closed = lodge1.open

        self.assertFalse(lodge_is_closed)

    def test_lodge_open_food(self):
        lodge1 = lodge.Lodge("Lodge1", True, False)
        lodge1.open_food()

        lodge_food_is_open = lodge1.open_food

        self.assertTrue(lodge_food_is_open)

    def test_lodge_close_food(self):
        lodge1 = lodge.Lodge("Lodge1", True, True)
        lodge1.close_food()

        lodge_food_is_closed = lodge1.open_food

        self.assertFalse(lodge_food_is_closed)

if __name__ == "__main__":
    unittest.main()
