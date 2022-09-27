import math
import numpy

print(math.exp(1))
print(numpy.arange(0, 5))

boolean = numpy.can_cast(numpy.uint64, numpy.timedelta64, casting="safe")


if boolean:
    print("Code is working!!")
else:
    raise ValueError("Code is broke!")