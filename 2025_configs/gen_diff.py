import numpy as np

datatemplate = '''# Model parameters
# Continuous equation parameters
 &PARM01
 tRef = 40*0.,
 sRef = 40*0.,
 diffKrNrT = {0},
 viscAr = 2.e-3,
 viscAh = 3.E4,
 bottomDragLinear =  1.e-2,
# bottomDragQuadratic = 0.001,
 tempAdvScheme =  77,
# saltAdvScheme = 77,
 saltstepping=.FALSE.,
 rhoConst=1035.,
 rhoConstFresh=1000.,
 tAlpha=2.E-4,
 sBeta =0.,
 gravity=9.81,
 eosType='LINEAR',
 ivdc_kappa=10., 
 implicitDiffusion=.TRUE.,
 implicitViscosity=.TRUE.,
 StaggerTimeStep=.TRUE.,        
 multiDimAdvection=.TRUE.,
 implicitFreeSurface=.TRUE.,
 allowFreezing=.FALSE.,
 hFacInf=0.2,
 hFacSup=2.0,
 useRealFreshWaterFlux=.TRUE.,
 useCDscheme=.TRUE.,  
 exactConserv=.TRUE.,
 rotationPeriod=86400.,
 exactConserv=.TRUE.,
 linFSConserveTr=.TRUE.,
 hFacMin=.05,
 hFacMindr=50.,
 readBinaryPrec=32,
 globalFiles=.TRUE.,
 useSingleCpuIO=.TRUE.,
 no_slip_sides=.FALSE.,
 &
# Elliptic solver parameters
 &PARM02
 cg2dMaxIters=1000,
 cg2dTargetResidual=1.E-13,
 &
# Time stepping parameters
 &PARM03
 nIter0 = 0,
 nTimeSteps = 15000000,
 deltaTmom  = 2700.    ,
# tauCD      = 321428.  ,
 deltaTtracer =   50400.0     ,
 deltaTClock  =   50400.0     ,
 abEps=0.1,
 pChkptFreq =   5.040000E+11 ,
 chkptFreq = 5.04E10,
 dumpFreq = 5.04E+12,
 monitorFreq = 5.04E9, 
 &
 # Gridding parameters
 &PARM04
 usingSphericalPolarGrid=.TRUE.,
 ygOrigin=-72.,
 dySpacing= 2.,
 dxSpacing= 2.,
 delR= 37,    40,    44,    48,    52,
 56,    60,    63,    66,    69,
 72,    75,    78,    81,    84,
 87,    90,    93,    96,    99,
 102,   105,   108,   111,   114,
 117,   120,   123,   126,   129,
 132,   135,   138,   141,   144,
 147,   150,   153,   156,   159,
 160,   160,   160,   160,   160,
 &
 &PARM05
 bathyFile=      'topog.bin',
 zonalWindFile=  'wind_x.bin',
# surfQfile =   'Qo',
 hydrogThetaFile = 'Tinit.bin',
 &'''

zl = np.array([    0.,   -37.,   -77.,  -121.,  -169.,  -221.,  -277.,  -337.,  -400.,
        -466.,  -535.,  -607.,  -682.,  -760.,  -841.,  -925., -1012., -1102.,
       -1195., -1291., -1390., -1492., -1597., -1705., -1816., -1930., -2047.,
       -2167., -2290., -2416., -2545., -2677., -2812., -2950., -3091., -3235.,
       -3382., -3532., -3685., -3841., -4000., -4160., -4320., -4480., -4640.])
z0 = -2500
for k, k0 in enumerate(1e-4*np.logspace(-1., 1., 3, base=2)):
    for l, lk in enumerate(np.concatenate((1000*np.logspace(-.5, .5, 3, base=2), [np.inf]))):
        for g, Kgm in enumerate(1000*np.logspace(-1., 0., 3, base=2)):
            print('{0}, {1}, {2}'.format(k0, lk, Kgm))
            diff = k0 * np.exp((z0 - zl) / lk)
            datafile = 'k{0}l{1}g{2}/data'.format(k, l, g)
            with open(datafile, 'w') as f:
                diffstr = ',\n    '.join([str(diff_j) for diff_j in diff])
                f.write(datatemplate.format(diffstr))
