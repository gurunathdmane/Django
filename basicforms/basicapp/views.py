from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.files.storage import FileSystemStorage
from . import forms
import csv, io

# Create your views here.

def home(request):
    return render(request,'basicapp/home.html')

def portf(request):
    return render (request,'basicapp/portfoliopage.html')


def form_name_view(request):

    form=forms.FormName()
    return render(request,'basicapp/form_page.html',{'form':form})
def upload(request):
    context = {}
    if request.method=='POST':
        upload_file=request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
    return render(request,'basicapp/upload.html',context)


from django.shortcuts import render
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
from django.http import HttpResponse
import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import io
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib
matplotlib.use('TkAgg')
import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

df1=pd.read_csv('/Users/gurunathmane/Desktop/Desktop_files/RA- Informatics Institute/GiniCurve-master/FourEclipse.txt',delimiter='\t',header=None,names=['x','y','class'])
    # plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    # gini value
def gini(array):
    # """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq: http://www.statsdirect.com/help/content/image/stat0206_wmf.gif
    # from: http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    array = array.flatten() #all values are treated equally, arrays must be 1d
    if np.amin(array) < 0:
        array -= np.amin(array) #values cannot be negative
    array += 0.000001 #values cannot be 0
    array = np.sort(array) #values must be sorted
    index = np.arange(1,array.shape[0]+1) #index per array element
    n = array.shape[0]#number of array elements
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array)))
     #Gini coefficient
angle_list= [x for x in range(0,360)]
ginival=[]
for x in angle_list:
    a=df1[['x','y']][0:5000]

        #Input n x 2
#     a=bb[0:5000]

    #z axis points
    b=np.array([[math.cos(math.radians(x))],[math.sin(math.radians(x))]])
    dot=np.dot(a,b)
    ginival.append(gini(dot))

def mat_graph(request):
    fig=Figure()
    canvas=FigureCanvas(fig)
    # xc=np.linspace(0,2.0*np.pi,360)
    # ax1=plt.subplot(111,polar=True)
    # ax1.plot(xc,ginival,label='mean',color='xkcd:salmon')
    # ax1.set_ylim(0,0.28)
    # ax1.set_yticks(np.linspace(0,0.28,4))
    # ax1.set_rlabel_position(90)
    # ax1.set_xticks(np.linspace(0,2.0*np.pi,17)[:-1])
    #
    # plt.grid(True)
    # plt.legend()
    # plt.show()
    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r

    ax = plt.subplot(111, projection='polar')
    ax.plot(theta, r)
    ax.set_rmax(2)
    ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
    ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
    ax.grid(True)

    ax.set_title("A line plot on a polar axis", va='bottom')
    plt.show()
    # # plt.axis([0, 6, 0, 20])
    # # plt.show()
    buf=io.BytesIO()
    plt.savefig(buf,format='png')
    plt.close(fig)
    response=HttpResponse(buf.getvalue(),content_type='image/png')
    return response
