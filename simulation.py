import lift
import lodge
import trail

class Simulation:
    def __init__(self, mountain):
        self.mountain = mountain

    def run(self):

        #trails created
        vista_glades = Trail.trail("Vista Glades", 3, False)
        alta_vista = Trail.trail("Alta Vista", 2, True)
        shermans_pass = Trail.trail("Sherman's Pass", 1, True)
        cobrass = Trail.trail("Cobrass", 2, False)
        preacher = Trail.trail("Preacher", 4, False)
        bolton_outlaw = Trail.trail("Bolton Outlaw", 3, False)
        cougar = Trail.trail("Cougar", 3, False)
        lost_boyz = Trail.trail("Lost Boyz", 4, False)
        adams_solitude = Trail.trail("Adam's Solitude", 4, False)

        #lifts created
        vista = Lift.lift("Vista", True)
        wilderness = Lift.lift("Wilderness", True)
        timberline = Lift.lift("Timberline", True)

        #lodges created
        base_lodge = Lodge.lodge("Base", True, True)
        timberline_lodge = Lodge.lodge("Timberline", True, True)

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
