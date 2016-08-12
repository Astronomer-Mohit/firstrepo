
sp1 = ['1','2','3','4','12','14','15','16']
f1 = ['6016.74820','6030.74830','6035.09340','6049.09350','4660.24140','4750.66000','4765.56180','4829.66000']
n1 = "306_"
a1 = [0,1,2,3,4,5,6,7]
for a in a1:
	clean(vis ="15A-164_20150306_1425687335571/products/15A-164.sb30470022.eb30471620.57087.94667363426.ms",imagename="15A-164_20150306_1425687335571/products/cleaned_images_1/"+n1+sp1[a],niter = 2000,mode="channel",width = 1, start = 1, threshold = "0.05Jy", imsize = [512,512], restfreq = f1[a]+'MHz',spw= sp1[a],cell="0.25arcsec",field='2',outframe="LSRK",mask = "box [ [ 222pix , 222pix] , [294pix, 292pix ] ]")

 
sp2 = ['1','2','3','4','5','6']
f2 = ['1420.40580','1589.00600', '1612.23090','1665.40180','1667.35900','1720.52990']
n2 ='323_'
a2 = [0,1,2,3,4,5]
for a in a2:
	clean(vis ="15A-164_20150323_1427158535826/products/15A-164.sb30469939.eb30508372.57104.97848186342.ms",imagename="15A-164_20150323_1427158535826/products/cleaned_images_1/"+n1+sp2[a],niter = 2000,mode="channel",width = 1, start = 1, threshold = "0.1Jy",mask = "box [ [ 222pix , 222pix] , [294pix, 292pix ] ]", imsize = [512,512],cell="0.5arcsec", restfreq = f2[a]+'MHz',spw= sp2[a],field='2',outframe="LSRK")

a3 = [0,1]
f3 = ['14488.47900','13442.10860']
sp3 = ['1','5']
n3 = '304_'
for a in a3:
	clean(vis ="15A-164_20150304_1425527740664/products/15A-164.sb30300006.eb30470714.57086.054855486116.ms",imagename="15A-164_20150304_1425527740664/products/cleaned_images_1/"+n3+sp3[a],niter = 2000,mode="channel",width = 1, start = 1, threshold = "0.01Jy", imsize = [512,512],mask = "box [ [ 222pix , 222pix] , [294pix, 292pix ] ]", restfreq = f3[a]+'MHz',spw= sp3[a], cell="0.05arcsec",field='2',outframe="LSRK")


