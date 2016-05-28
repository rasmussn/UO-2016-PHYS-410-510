#
# on AICSS:
#
#     qsub -I
#     module load python/2.7.9
#

from netCDF4 import Dataset

## groups
#
rootgrp = Dataset("test.nc", "w", format="NETCDF4")

## dimensions
#
time = rootgrp.createDimension("time", None)
r    = rootgrp.createDimension("r",   259)
z    = rootgrp.createDimension("z",    67)
phi  = rootgrp.createDimension("phi",   4)
mode = rootgrp.createDimension("mode", 67)

## variables
#
rho      = rootgrp.createVariable("rho",     "f8",("phi","z","r"))
resid    = rootgrp.createVariable("resid",   "f8",(      "z","r"))
rho_mode = rootgrp.createVariable("rho_mode","f8",(      "z","r"))

## attributes
#
rho.long_name = "density distribution"
rho.units     = "g/cm^3?"

## close
#
rootgrp.close()

## reopen
#
rootgrp = Dataset("test.nc", "a")

## write data to the file
#
rho_mode[:,:] = 13

rootgrp.close()
