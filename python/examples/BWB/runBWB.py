import sys, os, time
from mdo_import_helper import import_modules, MPI, mpiPrint
sys.path.append('../../')
import pyHyp
import petsc4py
petsc4py.init(sys.argv)
from petsc4py import PETSc

options= {
    # ---------------------------
    #        Grid Parameters
    # ---------------------------
    'N': 65, 
    's0':4e-6,
    'rMin':25,

    # ---------------------------
    #   Pseudo Grid Parameters
    # ---------------------------
    'NMax':1000,
    'ps0':5e-6,
    'pGridRatio':1.125,
    'cMax':6,

    # ---------------------------
    #   Smoothing parameters
    # ---------------------------
    'epsE': 1.0,
    'epsI': 2.0,
    'theta': 3.0,
    'volCoef': .16,
    'volBlend': 0.0005,
    'volSmoothIter': 10,

    # ---------------------------
    #   Solution Parameters
    # ---------------------------
    'kspRelTol': 1e-5,
    'kspMaxIts': 500,
    'preConLag': 5,
    'kspSubspaceSize':50,
    }

hyp = pyHyp.pyHyp('3d',fileName='bwb.fmt', options=options, zMirror=True)
hyp.run()
hyp.writeCGNS('bwb.cgns')
#hyp.writeCGNSOrig('bwbOrig.cgns')
