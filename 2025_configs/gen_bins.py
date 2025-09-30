#imports
import numpy as np
import matplotlib.pyplot as plt

#geometry
nx = 10
ny = 72
nz = 45
jb = 12

#parameters
D0 = 4800.
T0 = 9.
τ0 = 0.1

#filenames
topFile = 'topog.bin'
TInitFile = 'Tinit.bin'
rbcsTFile = 'rbcs_T.bin'
rbcsMaskFile = 'rbcs_mask.bin'
tauXFile = 'wind_x.bin'

#topography
wetMask = np.zeros((nz, ny, nx))
wetMask[:,2:-2,:] = 1
top = -D0 * np.ones((ny, nx))
top[[0,1,-2,-1],:] = 0.
top[jb:,[0,-1]] = 0.
top.astype('>f4').tofile(topFile)

#initial temperature
TInit = T0 * np.ones((nz, ny, nx))
TInit.astype('>f4').tofile(TInitFile)

#rbcs
rbcsMask = np.concatenate([np.expand_dims(top < 0, axis=0),
                           np.zeros((nz-1, ny, nx))])
SST = np.hstack([0., 0., T0*np.arange(1/2, jb-2, 1)/(jb-2), T0*np.ones(ny-jb-2), 0., 0.])
rbcsT = rbcsMask * np.expand_dims(SST, axis=[0,-1])
rbcsMask.astype('>f4').tofile(rbcsMaskFile)
rbcsT.astype('>f4').tofile(rbcsTFile) 
    
#wind stress
tauX = τ0 * np.outer(np.hstack([0., 0.,
                                np.sin(np.pi * np.arange(1/2, 2*(jb-2), 1) / (2*(jb-2)))**2,
                                np.zeros(ny-2*jb+2)]), np.ones(nx))
tauX.astype('>f4').tofile(tauXFile)

#figures
XC = np.arange(1, 2*nx, 2)
YC = np.arange(-ny+1, ny, 2)
plt.pcolormesh(XC, YC, top); plt.axhline(-48); plt.title('top'); plt.colorbar(); plt.savefig('imgs/top.png'); plt.close()
plt.pcolormesh(XC, YC, rbcsT[0,:,:]); plt.axhline(-48); plt.title('SST'); plt.colorbar(); plt.savefig('imgs/sst.png'); plt.close()
plt.pcolormesh(XC, YC, rbcsMask[0,:,:]); plt.axhline(-48); plt.title('RBCS mask'); plt.colorbar(); plt.savefig('imgs/mask.png'); plt.close()
plt.plot(YC, tauX, 'o'); plt.axvline(-48); plt.title('wind'); plt.savefig('imgs/wind.png'); plt.close()
plt.plot(YC, SST, 'o'); plt.axvline(-48); plt.title('SST'); plt.savefig('imgs/sst_1d.png'); plt.close()
