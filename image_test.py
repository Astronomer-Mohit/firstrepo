from numpy import*
import numpy as np
#hd = open("test_3.txt","w")
#a = arange(25)*4*10**(-2)
#k = np.logspace(3,5,15)
i = 1000
g = 0.1
#for i in k:
#	for g in a:
name_image  = str("test1.Clean.niter")+str(int(i))+str(".g")+str(g)+str(".image")
name_image1  = str("test1.Clean.niter")+str(int(i))+str(".g")+str(g)+str(".image")+str(".image")
out_file    = str("convolved.niter")+str(int(i))+str(".g")+str(g)+str(".image")
ImageDiff   = str("imagediff")+str(int(i))+str(".g")+str(g)+str(".image")
smooth      = str("smoothed")+str(int(i))+str(".g")+str(g)+str(".image")
print(smooth)
clean(vis="sim.alma.out10.noisy.ms",imagename=name_image,mode="channel",niter=int(i),gain=g,threshold="0.0mJy",nchan=1,imsize=[1024, 1024],cell=['0.1arcsec', '0.1arcsec'])
bmaj = imhead(imagename=name_image1, mode="get", hdkey="bmaj") 
bmin = imhead(imagename=name_image1, mode="get", hdkey="bmin") 
bpa = imhead(imagename=name_image1, mode="get", hdkey="bpa") 
#print(bmaj,bmin,bpa)
imsmooth(imagename="sim.alma.out10.skymodel",kernel="gauss",targetres=False,scale=-1.0,stokes="I",outfile=smooth,stretch=False,overwrite=True,major=bmaj,minor=bmin,pa=bpa)
#viewer(name_image1)

imregrid(imagename=smooth,template=name_image1,output=out_file)
immath(imagename=[out_file,name_image1],expr='(IM0-IM1)^2',outfile=ImageDiff)
xstat = imstat(ImageDiff)
xs= "niter=" + str(int(i)) + "; gain=" + str(g) + ", sigma=" + str(xstat["sigma"][0]) + ": rms=" + str(xstat["rms"][0]) + "/\n"
print(xs)
#		hd.write(str(xs))
fits_image=str("test1.niter")+str(int(i))+str(".g")+str(g)+str(".fits")
exportfits(fitsimage=fits_image, imagename=name_image1, overwrite=True)  
#print(imagename,fitsimage)
rmtables("test1.Clean.niter*")
#fits_image
#hd.close()



