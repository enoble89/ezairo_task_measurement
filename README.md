
  # task_detector

## This measurement analyzer only works with special ezairo firmware

## Getting started

1. Flash your ezairo with the scheduler debug flag enabled. DEBUG_GPIO_SCHEDULER
2. Connect logic analyzer to GPIO defined in the code
3. Collect data and measure
4. Measurement tool will calculate total runtime for each task.

e.g data output:

ΔT	0.0001491312487180707	s
bypass	6.260000000111176e-7	
sp	0.00004451200000005428	
fs	6.260000001248045e-7	
auxo	6.240000000161672e-7	
comp	6.240000000161672e-7	
tnr	6.240000000161672e-7	
sgen	6.240000000161672e-7	
mpo	6.259999998974308e-7	
vfb	0	
