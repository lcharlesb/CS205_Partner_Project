import mountain
import simulation

def main():
    mtn = mountain.Mountain("Bolton Valley", "Bolton, VT")

    sim = simulation.Simulation(mtn)
    sim.run()

main()
