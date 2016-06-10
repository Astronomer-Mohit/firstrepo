from numpy import*
import numpy as np
hd = open("test_2.txt","w")
a = arange(50)*2*10**(-2)
k = np.logspace(3,5,21)
#i = 1
#g = 0.1
#print(k)
for i in k:
	for g in a:
		name_image = str("SNR_G55_10s.Reg.Clean.niter")+str(int(i))+str(".g")+str(g)
		name_image1 = str("SNR_G55_10s.Reg.Clean.niter")+str(int(i))+str(".g")+str(g)+str(".image")
#print(name_image)
		clean(vis='SNR_G55_10s.calib.ms', imagename= name_image, imsize=1280, cell='8arcsec', interactive=False, niter=int(i), stokes='I', usescratch=F, gain = g ) 
#viewer(name_image1)
		xstat = imstat(name_image1)
		xs= "niter=" + str(int(i)) + "; gain=" + str(g) + ", sigma=" + str(xstat["sigma"][0]) + ": rms=" + str(xstat["rms"][0]) + "/\n"
#print(xs)
		hd.write(str(xs))
		fits_image=str("SNR_G55_10s.Reg.Clean.niter")+str(int(i))+str(".g")+str(g)+str(".fits")
		exportfits(fitsimage=fits_image, imagename=name_image1, overwrite=True)  
#print(imagename,fitsimage)
		rmtables("SNR_G55_10s.Reg.Clean.niter*")
#fits_image
hd.close()
		
