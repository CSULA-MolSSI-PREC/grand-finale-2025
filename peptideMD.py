from openmm import app
import openmm as mm
from simtk import unit
from sys import stdout
import time as time

# read in files
prmtop = app.AmberPrmtopFile('XXX.prmtop') # change XXX to your peptide's name
inpcrd = app.AmberInpcrdFile('XXX.inpcrd') # same here!

# OpenMM setup
system = prmtop.createSystem(nonbondedMethod=app.NoCutoff, constraints=app.HBonds, implicitSolvent=app.GBn2)
temperature = 298.15*unit.kelvin
integrator = mm.LangevinIntegrator(temperature, 1/unit.picosecond, 2*unit.femtoseconds)
platform = mm.Platform.getPlatformByName('CUDA')
simulation = app.Simulation(prmtop.topology, system, integrator, platform)
simulation.context.setPositions(inpcrd.positions)

# minimization
st = simulation.context.getState(getPositions=True,getEnergy=True)
print("Potential energy before minimization is %s" % st.getPotentialEnergy())

print('Minimizing...')
simulation.minimizeEnergy(maxIterations=100)

st = simulation.context.getState(getPositions=True,getEnergy=True)
print("Potential energy after minimization is %s" % st.getPotentialEnergy())

# equilibration
simulation.context.setVelocitiesToTemperature(298.15*unit.kelvin)
print('Equilibrating...')
tinit=time.time()
simulation.step(50000)
tfinal=time.time()
print('Done!')
print('Time required for simulation:', tfinal-tinit, 'seconds')

# production
simulation.reporters.append(app.DCDReporter('XXX_sim.dcd', 500)) # change YYYYY to your peptide's name
simulation.reporters.append(app.StateDataReporter(stdout, 50000, step=True, time=True,
    potentialEnergy=True, temperature=True, speed=True, separator='\t'))


print('Running Production...')
simulation.step() # add the number of steps inside the parentheses
print('Done!')
