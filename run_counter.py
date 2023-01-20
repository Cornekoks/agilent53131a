import agilent53131a
ag = agilent53131a.Agilent53131a()

print(ag.open_device('ASRL1::INSTR'))