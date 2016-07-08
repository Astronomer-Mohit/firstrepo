import random
from numpy import*
import numpy as np
qw34 = np.arange(81)
k = np.arange(81)*0.1
a = np.arange(81)*0.1
cf = np.arange(81)*0.1
ms = np.arange(81)*0.1
mb = np.arange(81)*0.1
rb = np.arange(81)*0.1
K = np.arange(81)*0.1
sm = np.arange(81)*0.1
qw = np.arange(81)

hd = open("v1.txt")
i = 0	
for w in hd:
	k[i] = 1e1**(3+float(w)*2)      #NO.of interation
	i=i+1
hd.close()


hd = open("v2.txt")
i = 0	
for w in hd:
	a[i] = float(w)    #GAIN
	i=i+1
hd.close() 

hd = open("v3.txt")
i = 0	
for w in hd:
	cf[i] = (1+float(w)*4)              #cyclefactor
	i=i+1
hd.close()

hd = open("v4.txt")                          #multiscale
i = 0	
for w in hd:
	ms[i] = float(w)
	i=i+1
hd.close()

hd = open("v5.txt")                   #minpb
i = 0	
for w in hd:
	mb[i] = (0.001+float(w)*0.499)
	i=i+1
hd.close()

hd = open("v6.txt")
i = 0	
for w in hd:                 #rb
	rb[i] = float(w)
	i=i+1
hd.close()

hd = open("v7.txt")            #K
i = 0	
for w in hd:
	K[i] = float(w)
	i=i+1
hd.close()

hd = open("v8.txt")                       #sm
i = 0	
for w in hd:
	sm[i] = float(w)
	i=i+1
hd.close()
hd = open("sub_mohit_simobserve.txt","w")
#k = 1e1**(3+t[:]['V1']*2)             #niter
#a = t[:]['V2']                        #gain
#cf = (1+t[:]['V3']*4)                 #cyclefactor
#ms =t[:]['V4']                        #multiscale     -cat
#mb = (0.001+t[:]['V5']*0.499)           #minpb
#rb = t[:]['V6']                       #robust
wt = ("natural","uniform","briggs")   #V6:weighting   - cat
#K = t[:]['V7']
#sm = t[:]['V8']                       #smallscalebias

for i in qw34:
	name_image  = str("sub_mohit1_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")	
	name_image1 = str("sub_mohit1_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")+str(".image")
	out_file    = str("regrid_sub_mohit1_image.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")+str(".image")
	ImageDiff   = str("imagediff")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
	smooth      = str("smoothed")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
#print(smooth)
	if random.random() < ms[i]:
		multiscale = []
		smallscalebias = 0
	else:
		multiscale=[0,6,10,30,60]
		smallscalebias=float(sm[i])
	if float(K[i]) <  0.33:
		weighting=wt[0]
	if float(K[i]) > 0.33 and float(K[i]) < 0.66 :
		weighting =wt[1]
	if float(K[i]) > 0.66:
		weighting =wt[2]
	
	smooth_modelimage= str("smoothed_modelimage")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
	name_model_image =  str("sub_model_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
	name_model_image1 = str("sub_model_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")+str(".image")
	out_file_model    = str("regrid_model_image.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")+str(".image")
	ImageDiff_model   = str("imagediff_model")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
	
	#imsmooth(imagename="sub_smooth_modelimage_70", kernel="gauss", targetres=False, scale=-1.0, stokes="I", outfile=smooth_modelimage, stretch=False, overwrite=True, major='70arcsec', minor='70arcsec', pa='0deg')
	clean(vis="sub_mohit_simobserve/sub_mohit_simobserve.alma.out10.noisy.ms",imagename=name_model_image, modelimage="sub_smooth_modelimage_70", mode="channel",niter=int(k[i]),gain=float(a[i]),threshold="0.0mJy",nchan=1,imsize=[2000, 2000],cell=['0.3arcsec', '0.3arcsec'], robust= float(rb[i]), minpb = float(mb[i]), cyclefactor=float(cf[i]))
	xstat_model = imstat(name_model_image1)
	noise = xstat_model["medabsdevmed"][0]
	bmaj = imhead(imagename=name_model_image1, mode="get", hdkey="bmaj") 
	bmin = imhead(imagename=name_model_image1, mode="get", hdkey="bmin") 
	bpa = imhead(imagename=name_model_image1, mode="get", hdkey="bpa") 

	imsmooth(imagename="sub_mohit_simobserve/sub_mohit_simobserve.alma.out10.skymodel",kernel="gauss",targetres=False,scale=-1.0,stokes="I",outfile=smooth_modelimage,stretch=False,overwrite=True,major= bmaj,minor=bmin,pa=bpa)
	imregrid(imagename=name_model_image1,template=smooth_modelimage,output=out_file_model)
	immath(imagename=[out_file_model,smooth_modelimage],expr='(IM0-IM1)',outfile=ImageDiff_model)
	xstat = imstat(ImageDiff_model)
	quality = (xstat["medabsdevmed"][0])/noise
	xs1= "niter=" + str(int(k[i])) + " gain=" + str(a[i]) + " multiscale="+str(multiscale)+str(" smallscalebias=")+str(smallscalebias)+str(" weighting=")+str(weighting)+" cyclefactor="+str(cf[i])+"  robust="+str(rb[i])+" minpb="+str(mb[i])+ " sigma=" + str(xstat["sigma"][0]) + " rms=" +str(xstat["rms"][0]) +" medabsdevmed="+ str(xstat["medabsdevmed"][0])+ " quality_factor=" + str(quality)
	
	fits_image00=str("sub_model_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
	fits_image01=str("regrid_model_clean_image.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
	fits_image02=str("imagediff_model.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
	exportfits(fitsimage=fits_image00, imagename=name_model_image1, overwrite=True)  
	exportfits(fitsimage=fits_image01, imagename=out_file_model, overwrite=True)  
	exportfits(fitsimage=fits_image02, imagename=ImageDiff_model, overwrite=True)  
	
	clean(vis="sub_mohit_simobserve/sub_mohit_simobserve.alma.out10.noisy.ms",imagename=name_image, mode="channel",niter=int(k[i]),gain=float(a[i]),threshold="0.0mJy",nchan=1,imsize=[2000, 2000],cell=['0.3arcsec', '0.3arcsec'], robust= float(rb[i]), minpb = float(mb[i]), cyclefactor=float(cf[i]))
	xstat2 = imstat(name_image1)
	noise = xstat2["medabsdevmed"][0]
	bmaj = imhead(imagename=name_image1, mode="get", hdkey="bmaj") 
	bmin = imhead(imagename=name_image1, mode="get", hdkey="bmin") 
	bpa = imhead(imagename=name_image1, mode="get", hdkey="bpa") 

	imsmooth(imagename="sub_mohit_simobserve/sub_mohit_simobserve.alma.out10.skymodel",kernel="gauss",targetres=False,scale=-1.0,stokes="I",outfile=smooth,stretch=False,overwrite=True,major= bmaj,minor=bmin,pa=bpa)

	imregrid(imagename=name_image1,template=smooth,output=out_file)
	immath(imagename=[out_file,smooth],expr='(IM0-IM1)',outfile=ImageDiff)
	xstat = imstat(ImageDiff)
	quality = (xstat["medabsdevmed"][0])/noise
	xs2= " quality_factor_without_model=" + str(quality)+"\n"
	xs = xs1 + xs2
	hd.write(str(xs))
	fits_image0=str("sub_mohit1_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
	fits_image1=str("regrid_sub_mohit1_image.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
	fits_image2=str("imagediff.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
	exportfits(fitsimage=fits_image0, imagename=name_image1, overwrite=True)  
	exportfits(fitsimage=fits_image1, imagename=out_file, overwrite=True)  
	exportfits(fitsimage=fits_image2, imagename=ImageDiff, overwrite=True)  
#print(imagename,fitsimage)
	
	rmtables("sub_mohit1_clean.niter*")
	rmtables("imagediff*")
	rmtables("regrid_sub_mohit1_image.niter*")
	rmtables("smoothed*")
	
	rmtables("sub_model_clean.niter*")
	rmtables("imagediff_model*")
	rmtables("regrid_model_image.niter*")
	rmtables("smoothed_modelimage*")
hd.close()
