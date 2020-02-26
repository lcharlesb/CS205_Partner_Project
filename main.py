import mountain
import simulation

def main():
    mtn = mountain.Mountain()

    sim = simulation.Simulation(mtn)
    sim.run()

main()
