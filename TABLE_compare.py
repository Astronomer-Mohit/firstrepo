
from astropy.table import Table
import numpy as np
import numpy as np
import matplotlib.pyplot as plt

hd = open("sub_image_cleaning.txt")
count =0
for y in hd:
	count = count +1
hd.close()
hd = open("sub_image_cleaning.txt")
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
t = Table([a, b, c, d, e, f, g, h, i, j, k1, k2, k3], names=('Niter', 'gain', 'Multiscale', 'smallscalebias', 'weighting', 'cyclefactor', 'robust', 'minpb', 'sigma','RMS' ,'MAD', 'Quality factor', 'quality_factor_without_model'), meta={'name': 'first table'})
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
k = min(t[:]['quality_factor_without_model'])
k1 = max(t[:]['quality_factor_without_model'])
plt.ylim((0.9*(k),1.1*(k1)))
y1 = t[:]['quality_factor_without_model']
#niter
plt.xlim((0.9*min(t[:]['Niter'])),1.1*max(t[:]['Niter']))
x = (t[:]['Niter'])
y = t[:]['Quality factor']
plt.yscale('log')
plt.xscale('log')
plt.scatter(x,y,s=80, c='r', marker=">",label='with model')
plt.yscale('log')
plt.xscale('log')
plt.scatter(x, y1, s=80, c='b', marker=(5, 0),label='without model')
plt.xlabel('No. of iterations')
plt.ylabel('Quality Factor')
plt.title("No. of Iterations versus Quality plot (Log scale)")
plt.legend(loc='upper left');
plt.show()
#robust
plt.xlim((0.9*min(t[:]['robust'])),1.1*max(t[:]['robust']))
x = (t[:]['robust'])
y = t[:]['Quality factor']
plt.xlabel('Robust')
plt.scatter(x,y,s=80, c='r', marker=">",label='with model')
plt.scatter(x, y1, s=80, c='b', marker=(5, 0),label='without model')
plt.ylabel('Quality Factor')
plt.title("Robust versus Quality plot")
plt.legend(loc='upper left');
plt.show()
#gain
plt.xlim((0.9*min(t[:]['gain'])),1.1*max(t[:]['gain']))
x = (t[:]['gain'])
y = t[:]['Quality factor']
plt.xlabel('Gain')
plt.ylabel('Quality Factor')
plt.scatter(x,y,s=80, c='r', marker=">",label='with model')
plt.scatter(x, y1, s=80, c='b', marker=(5, 0),label='without model')
plt.title("Gain versus Quality plot")
plt.legend(loc='upper left');
plt.show()
#Multiscale
plt.scatter(k222,y,s=80, c='r', marker=">",label='with model')
plt.scatter(k222, y1, s=80, c='b', marker=(5, 0),label='without model')
plt.xlabel('Multiscale')
plt.ylabel('Quality Factor')
plt.title("Multiscale versus Quality plot")
plt.legend(loc='upper left');
plt.show()
#smallscalebias
plt.xlim((0.9*min(t[:]['smallscalebias'])),1.1*max(t[:]['smallscalebias']))
x = (t[:]['smallscalebias'])
y = t[:]['Quality factor']
plt.xlabel('smallscalebias')
plt.scatter(x,y,s=80, c='r', marker=">",label='with model')
plt.scatter(x, y1, s=80, c='b', marker=(5, 0),label='without model')
plt.ylabel('Quality Factor')
plt.title("Smallscalebias versus Quality plot")
plt.legend(loc='upper left');
plt.show()
#weighting
plt.scatter(a1,y,s=80, c='r', marker=">",label='with model')
plt.scatter(a1, y1, s=80, c='b', marker=(5, 0),label='without model')
plt.xlabel('Weighting')
plt.ylabel('Quality Factor')
plt.title("Weighting versus Quality plot")
plt.legend(loc='upper left');
plt.show()
#cyclefactor
plt.xlim((0.9*min(t[:]['cyclefactor'])),1.1*max(t[:]['cyclefactor']))
x = (t[:]['cyclefactor'])
y = t[:]['Quality factor']
plt.xlabel('cyclefactor')
plt.ylabel('Quality Factor')
plt.scatter(x,y,s=80, c='r', marker=">",label='with model')
plt.scatter(x, y1, s=80, c='b', marker=(5, 0),label='without model')
plt.title("cyclefactor versus Quality plot")
plt.legend(loc='upper left');
plt.show()
#minpb
plt.xlim((0.9*min(t[:]['minpb'])),1.1*max(t[:]['minpb']))
x = (t[:]['minpb'])
y = t[:]['Quality factor']
plt.xlabel('minpb')
plt.scatter(x,y , s=80, c='r', marker=">",label='with model')
plt.scatter(x,y1, s=80, c='b', marker=(5, 0), label='without model')
plt.ylabel('Quality Factor')
plt.title("minpb versus Quality plot")
plt.legend(loc='upper left');
plt.show()
