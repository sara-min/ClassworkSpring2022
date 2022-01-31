print("This is the database module and python calls it {}".format(__name__))
# first module run is always called main
#import blood_calculator 
#from blood_calculator import check_HDL, check_LDL
import blood_calculator as bc
from matplotlib import * # not equivalent of import matplotlib
import numpy as np


HDL_value = 55
#classification = blood_calculator.check_HDL(HDL_value)
#classification = check_HDL(HDL_value)
classification = bc.check_HDL(HDL_value)
print("55 is {}".format(classification))
x = bc.check_LDL(200)

def function():
    print("1")
def function():
    print("2")  