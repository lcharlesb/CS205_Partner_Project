import lift
import lodge
import trail

class Simulation:
    def __init__(self, mountain):
        self.mountain = mountain

    def run(self):
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
        wilderness = lift.Lift("Wilderness", True)
        timberline = lift.Lift("Timberline", True)

        # Lodges created
        base_lodge = lodge.Lodge("Base", True, True)
        timberline_lodge = lodge.Lodge("Timberline", True, True)

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
