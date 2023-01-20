import agilent53131a
ag = agilent53131a.Agilent53131a()

import time

print(ag.open_device('GPIB0::3::INSTR')) #change the name to the correct bus of course

ag.set_trigger_level(3)

for i in range(10):
    x=ag.get_counts()
    print(x)
    time.sleep(0.1)

ag.close_device()