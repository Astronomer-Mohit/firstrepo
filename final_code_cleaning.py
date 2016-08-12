import random
from numpy import*
data = loadtxt(text_file,delimiter = ",",unpack=True) 
import numpy as np
from astropy.table import Table
import matplotlib.pyplot as plt

def cleaning(value,str_ms,text_file,image,sky_model)
	s111 = len(data[0,:])	
	qw34 = np.arange(s)
	k = 1e1**(3+data[0,:]*2)         #No. of interation
	a = data[1,:]                    #GAIN
	cf = (1+data[2,:]*4)             #cyclefactor
	ms = data[3,:]                   #multiscale
	mb = (0.001+ data[4,:]*0.499)    #minpb
	rb = data[5,:]                   #rb
	K = data[6,:] 		         #used with weighting
	sm = data[7,:] 			 #smallscalebias
	wt = ("natural","uniform","briggs") 
	imsmooth(imagename=image, kernel="gauss", targetres=False, scale=-1.0, stokes="I", outfile="smooth_modelimage_70", stretch=False, overwrite=True, major='70arcsec', minor='70arcsec', pa='0deg')
	hd = open("sub_image_cleaning.txt","w")
# for cleaning with model image	
	for i in qw34:
		if value == 0 or value == -1 :
			name_image  = str("sub_image_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")	
			name_image1 = str("sub_image_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")+str(".image")
			out_file    = str("regrid_sub_image_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")+str(".image")
			ImageDiff   = str("imagediff")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
			smooth      = str("smoothed")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
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
			
			clean(vis=str_ms,imagename=name_model_image, modelimage="smooth_modelimage_70", mode="channel",niter=int(k[i]),gain=float(a[i]),threshold="0.0mJy",nchan=1,imsize=[2000, 2000],cell=['0.3arcsec', '0.3arcsec'], robust= float(rb[i]), minpb = float(mb[i]), cyclefactor=float(cf[i]))
			xstat_model = imstat(name_model_image1)
			noise = xstat_model["medabsdevmed"][0]
			bmaj = imhead(imagename=name_model_image1, mode="get", hdkey="bmaj") 
			bmin = imhead(imagename=name_model_image1, mode="get", hdkey="bmin") 
			bpa = imhead(imagename=name_model_image1, mode="get", hdkey="bpa") 

			imsmooth(imagename= sky_model,kernel="gauss",targetres=False,scale=-1.0,stokes="I",outfile=smooth_modelimage,stretch=False,overwrite=True,major= bmaj,minor=bmin,pa=bpa)
			imregrid(imagename=name_model_image1,template=smooth_modelimage,output=out_file_model)
			immath(imagename=[out_file_model,smooth_modelimage],expr='(IM0-IM1)',outfile=ImageDiff_model)
			xstat = imstat(ImageDiff_model)
			quality = (xstat["medabsdevmed"][0])/noise
			xs1= "niter=" + str(int(k[i])) + " gain=" + str(a[i]) + " multiscale="+str(multiscale)+str(" smallscalebias=")+str(smallscalebias)+str(" weighting=")+str(weighting)+" cyclefactor="+str(cf[i])+"  robust="+str(rb[i])+" minpb="+str(mb[i])+ " sigma=" + str(xstat["sigma"][0]) + " rms=" +str(xstat["rms"][0]) +" medabsdevmed="+ str(xstat["medabsdevmed"][0])+ " quality_factor=" + str(quality)
	
	#fits_image00=str("cleaned_images/cleaned/sub_model_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
	#fits_image01=str("cleaned_images/regrid/regrid_model_clean_image.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
	#fits_image02=str("cleaned_images/difference/imagediff_model.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
	#exportfits(fitsimage=fits_image00, imagename=name_model_image1, overwrite=True)  
	#exportfits(fitsimage=fits_image01, imagename=out_file_model, overwrite=True)  
	#exportfits(fitsimage=fits_image02, imagename=ImageDiff_model, overwrite=True)  
			rmtables("ub_image_clean.niter*")
			rmtables("imagediff*")
			rmtables("regrid_sub_image_clean.niter*")
			rmtables("smoothed*")
			if value == 0:
				hd.write(str(xs1))
		if value == 1 or value == -1 :	

			smooth_modelimage= str("smoothed_modelimage")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
			name_model_image =  str("sub_model_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
			name_model_image1 = str("sub_model_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")+str(".image")
			out_file_model    = str("regrid_model_image.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")+str(".image")
			ImageDiff_model   = str("imagediff_model")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".image")
			
			clean(vis=str_ms,imagename=name_image, mode="channel",niter=int(k[i]),gain=float(a[i]),threshold="0.0mJy",nchan=1,imsize=[2000, 2000],cell=['0.3arcsec', '0.3arcsec'], robust= float(rb[i]), minpb = float(mb[i]), cyclefactor=float(cf[i]))
			xstat2 = imstat(name_image1)
			noise = xstat2["medabsdevmed"][0]
			bmaj = imhead(imagename=name_image1, mode="get", hdkey="bmaj") 
			bmin = imhead(imagename=name_image1, mode="get", hdkey="bmin") 
			bpa = imhead(imagename=name_image1, mode="get", hdkey="bpa") 

			imsmooth(imagename=sky_model,kernel="gauss",targetres=False,scale=-1.0,stokes="I",outfile=smooth,stretch=False,overwrite=True,major= bmaj,minor=bmin,pa=bpa)

			imregrid(imagename=name_image1,template=smooth,output=out_file)
			immath(imagename=[out_file,smooth],expr='(IM0-IM1)',outfile=ImageDiff)
			xstat = imstat(ImageDiff)
	
			quality = (xstat["medabsdevmed"][0])/noise
			xs2= "niter=" + str(int(k[i])) + " gain=" + str(a[i]) + " multiscale="+str(multiscale)+str(" smallscalebias=")+str(smallscalebias)+str(" weighting=")+str(weighting)+" cyclefactor="+str(cf[i])+"  robust="+str(rb[i])+" minpb="+str(mb[i])+ " sigma=" + str(xstat["sigma"][0]) + " rms=" +str(xstat["rms"][0]) +" medabsdevmed="+ str(xstat["medabsdevmed"][0])+" quality_factor_without_model=" + str(quality)+"\n"
#fits_image0=str("cleaned_images/cleaned/without/sub_without_model_clean.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
#	fits_image1=str("cleaned_images/regrid/without/regrid_sub_without_model_image.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
#	fits_image2=str("cleaned_images/difference/without/imagediff_without_model.niter")+str(int(k[i]))+str(".g")+str(a[i])+str(".iter")+ str(i)+str(".fits")
#	exportfits(fitsimage=fits_image0, imagename=name_image1, overwrite=True)  
#	exportfits(fitsimage=fits_image1, imagename=out_file, overwrite=True)  
#	exportfits(fitsimage=fits_image2, imagename=ImageDiff, overwrite=True)  
			if value == 1:
				hd.write(str(xs2))
	
			rmtables("sub_model_clean.niter*")
			rmtables("imagediff_model*")
			rmtables("regrid_model_image.niter*")
			rmtables("smoothed_modelimage*")
			if value == -1:
				hd.write(str(xs1+xs2))
	hd.close()

def printing(file_txt)
	hd = open(file_txt)
	count =0
	for y in hd:
		count = count +1
	hd.close()
	hd = open(file_txt)
	k = hd.read()
#print(k.split())
	w = 0
	w1 = 0
	w2 = 0
	w3 = 0
	w4 = 0
	w5 = 0
	w6 = 0
	w7 = 0
	w8 = 0
	w9 = 0
	w10 =0
	a = np.arange(count)
	b = np.arange(count)*1.0
	d = np.arange(count)*1.0
	f = np.arange(count)*1.0
	g = np.arange(count)*1.0
	h = np.arange(count)*1.0
	i = np.arange(count)*1.0
	j = np.arange(count)*1.0
	k1 = np.arange(count)*1.0
	k2 = np.arange(count)*1.0
	k3 = np.arange(count)*1.0
	k22 = np.arange(count)
	c =[]
	e =[]

	for a1 in k.split():
		if a1.startswith("niter="):
			l = a1
			a11 = l.split("=")
			#print(a11[1])
			a[w] = int(a11[1])
			w = w+1
	for a1 in k.split():
		if a1.startswith("gain="):
			l = a1
			a11 = l.split("=")
			b[w1] = float(a11[1])
			w1 = w1+1
	for a1 in k.split():
		if a1.startswith("multiscale="):
			l = a1
			a11 = l.split("=")
			#print(a11[1])
			c.append(a11[1])
	for a1 in k.split():
		if a1.startswith("smallscalebias="):
			l = a1
			a11 = l.split("=")
			d[w2] = float(a11[1])
			w2 = w2+1
	for a1 in k.split():
		if a1.startswith("weighting="):
			l = a1
			a11 = l.split("=")
			e.append(a11[1])
	for a1 in k.split():
		if a1.startswith("cyclefactor="):
			l = a1
			a11 = l.split("=")
			f[w3] = float(a11[1])
			w3 = w3+1
	for a1 in k.split():
		if a1.startswith("robust="):
			l = a1
			a11 = l.split("=")
			g[w4] = float(a11[1])
			w4 = w4+1
	for a1 in k.split():
		if a1.startswith("minpb="):
			l = a1
			a11 = l.split("=")
			h[w5] = float(a11[1])
			w5 = w5+1
	for a1 in k.split():
		if a1.startswith("sigma="):
			l = a1
			a11 = l.split("=")
			i[w6] = float(a11[1])
			w6 = w6+1
	for a1 in k.split():
			if a1.startswith("rms="):
			l = a1
			a11 = l.split("=")
			j[w7] = float(a11[1])
			w7 = w7+1
	for a1 in k.split():
		if a1.startswith("medabsdevmed="):
			l = a1
			a11 = l.split("=")
			k1[w8] = float(a11[1])
			w8 = w8+1
	for a1 in k.split():
		if a1.startswith("quality_factor="):
			l = a1
			a11 = l.split("=")
			k2[w9] = float(a11[1])
			w9 = w9+1
	for a1 in k.split():
		if a1.startswith("quality_factor_without_model="):
			l = a1
			a11 = l.split("=")
			k3[w10] = float(a11[1])
			w10 = w10+1

	k222= np.arange(count)*0
	a1 = np.arange(count)*0
	t = Table([a, b, c, d, e, f, g, h, i, j, k1, k2, k3], names=('Niter', 'gain', 'Multiscale', 'smallscalebias', 'weighting', 'cyclefactor', 'robust', 'minpb', 'sigma','RMS' ,'MAD', 'Quality_factor', 'quality_factor_without_model'), meta={'name': 'first table'})
	for a in k22:
		if t[a]['Multiscale']=='[]':
			k222[a] = 1
		for a in k22:
			if t[a]['weighting']=='briggs':
				a1[a] = 2 
			if t[a]['weighting']=='uniform':
				a1[a] = 1
			if t[a]['weighting']=='natural':
				a1[a] = 0

#print(t)
	t.show_in_browser(jsviewer=True)
#t.show_in_browser()
	f, axarr = plt.subplots(4, 2)
	k = min(t[:]['quality_factor_without_model'])
	1 = max(t[:]['quality_factor_without_model'])
	y1 = t[:]['quality_factor_without_model']
	#niter
	plt.xlim((0.9*min(t[:]['Niter'])),1.1*max(t[:]['Niter']))
	x = (t[:]['Niter'])
	y = t[:]['Quality_factor']
	axarr[0, 0].set_yscale('log')
	axarr[0, 0].set_xscale('log')
	axarr[0, 0].scatter(x, y ,s=80, c='r', marker=">",label='with model')
	axarr[0, 0].set_yscale('log')
	axarr[0, 0].set_xscale('log')
	axarr[0, 0].scatter(x, y1, s=80, c='b',label='without model')
	axarr[0, 0].set_xlabel('No. of iterations')
	axarr[0, 0].set_ylabel('Quality Factor')
	axarr[0, 0].set_title('No. of Iterations versus Quality plot (Log scale)')
	axarr[0, 0].legend(loc='upper left')
	axarr[0, 0].set_ylim((0.9*(k),1.1*(k1)))
	
#robust
	axarr[0, 1].set_xlim((0.9*min(t[:]['robust'])),1.1*max(t[:]['robust']))
	x = (t[:]['robust'])
	y = t[:]['Quality_factor']
	axarr[0, 1].set_xlabel('Robust')
	axarr[0, 1].scatter(x,y,s=80, c='r', marker=">",label='with model')
	axarr[0, 1].scatter(x, y1, s=80, c='b', marker=(5, 0),label='without model')
	axarr[0, 1].set_ylabel('Quality Factor')
	axarr[0, 1].set_title("Robust versus Quality plot")
	axarr[0, 1].legend(loc='upper left');

#gain
	axarr[0, 1].set_xlim((0.9*min(t[:]['gain'])),1.1*max(t[:]['gain']))
	x = (t[:]['gain'])
	y = t[:]['Quality_factor']
	axarr[1, 0].set_xlabel('Gain')
	axarr[1, 0].set_ylabel('Quality Factor')
	axarr[1, 0].scatter(x,y,s=80, c='r', marker=">",label='with model')
	axarr[1, 0].scatter(x, y1, s=80, c='b', marker=(5, 0),label='without model')
	axarr[1, 0].set_title("Gain versus Quality plot")
	axarr[1, 0].legend(loc='upper left');

	#Multiscale
	axarr[1, 1].scatter(k222,y,s=80, c='r', marker=">",label='with model')
	axarr[1, 1].scatter(k222, y1, s=80, c='b', marker=(5, 0),label='without model')
	axarr[1, 1].set_xlabel('Multiscale')
	axarr[1, 1].set_ylabel('Quality Factor')
	axarr[1, 1].set_title("Multiscale versus Quality plot")
	axarr[1, 1].legend(loc='upper left');

#smallscalebias
	axarr[2, 0].set_xlim((0.9*min(t[:]['smallscalebias'])),1.1*max(t[:]['smallscalebias']))
	x = (t[:]['smallscalebias'])
	y = t[:]['Quality_factor']
	axarr[2, 0].set_xlabel('smallscalebias')
	axarr[2, 0].scatter(x,y,s=80, c='r', marker=">",label='with model')
	axarr[2, 0].scatter(x, y1, s=80, c='b', marker=(5, 0),label='without model')
	axarr[2, 0].set_ylabel('Quality Factor')
	axarr[2, 0].set_title("Smallscalebias versus Quality plot")

#weighting
	axarr[2, 1].scatter(a1,y,s=80, c='r', marker=">",label='with model')
	axarr[2, 1].scatter(a1, y1, s=80, c='b', marker=(5, 0),label='without model')
	axarr[2, 1].set_xlabel('Weighting')
	axarr[2, 1].set_ylabel('Quality Factor')
	axarr[2, 1].set_title("Weighting versus Quality plot")
	axarr[2, 1].legend(loc='upper left');

#cyclefactor
	axarr[3, 0].set_xlim((0.9*min(t[:]['cyclefactor'])),1.1*max(t[:]['cyclefactor']))
	x = (t[:]['cyclefactor'])
	y = t[:]['Quality_factor']
	axarr[3, 0].set_xlabel('cyclefactor')
	axarr[3, 0].set_ylabel('Quality Factor')
	axarr[3, 0].scatter(x,y,s=80, c='r', marker=">",label='with model')
	axarr[3, 0].scatter(x, y1, s=80, c='b', marker=(5, 0),label='without model')
	axarr[3, 0].set_title("cyclefactor versus Quality plot")
	axarr[3, 0].legend(loc='upper left');

#minpb
	axarr[3, 1].set_xlim((0.9*min(t[:]['minpb'])),1.1*max(t[:]['minpb']))
	x = (t[:]['minpb'])
	y = t[:]['Quality_factor']
	axarr[3, 1].set_xlabel('minpb')
	axarr[3, 1].scatter(x,y , s=80, c='r', marker=">",label='with model')
	axarr[3, 1].scatter(x,y1, s=80, c='b', marker=(5, 0), label='without model')
	axarr[3, 1].set_ylabel('Quality Factor')
	axarr[3, 1].set_title("minpb versus Quality plot")
	axarr[3, 1].legend(loc='upper left');
	plt.show()
