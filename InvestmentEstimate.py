# A simple code for calculating the future value of an investment.
# Principle Amount (Present Value) = $15000
# Time/Period (nper) = 3 years
# Annual return rate = 7%
# Periodic Payments (pmt) = 0

import numpy_financial as npf
result = npf.fv(rate=0.07, nper=3, pmt=0, pv=15000)
print(result)
