import NMRfit as nmrft
import os
import matplotlib.pyplot as plt
import numpy as np


# input directory
inDir = "./Data/blindedData/dc_4a_cdcl3_kilimanjaro_25c_1d_1H_1_043016.fid"

# read in data
data = nmrft.varian_process(os.path.join(inDir, 'fid'), os.path.join(inDir, 'procpar'))

# bound the data
data.select_bounds(low=3.23, high=3.6)

# select peaks and satellites
peaks = data.select_peaks(method='auto', n=6, plot=True)

# generate bounds and initial conditions
lb, ub = data.generate_initial_conditions()

# fit data
fit = nmrft.FitUtility(data, lb, ub)

# generate result
res = fit.generate_result(scale=1)

# # summary
fit.summary()
