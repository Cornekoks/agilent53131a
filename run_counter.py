import agilent53131a
ag = agilent53131a.Agilent53131a()

print(ag.open_device('GPIB::3')) #change the name to the correct bus of course