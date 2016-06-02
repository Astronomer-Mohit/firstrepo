from numpy import*
hd = open("test_2.txt","w")
a = arange(100)*10**(-2)
k = logspace(0,1000000,101)
#i = 100
#g = 0.3
for i in k:
	for g in a:
		clean(vis='SNR_G55_10s.calib.ms', imagename='SNR_G55_10s.Reg.Clean.trial1', imsize=1280, cell='8arcsec', interactive=False, niter=int(i), stokes='I', usescratch=F, gain = g ) 
		xstat = imstat("SNR_G55_10s.Reg.Clean.trial1.image")
		xs= "niter=" + str(i) + "; gain=" + str(g) + ", sigma=" + str(xstat["sigma"][0]) + ": rms=" + str(xstat["rms"][0]) + "/\n"
		hd.write(str(xs))
		rmtables("SNR_G55_10s.Reg.Clean.trial1.*")
hd.close()
		
