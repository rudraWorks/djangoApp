# i have created by me
from django.http import HttpResponse
import random
from cv2 import cv2 
import numpy as np
import time
from django.shortcuts import render

fileContents=open('mysite/me.txt','r').read()
img=cv2.imread("D:/vs_python/opencv tut/me.png")
arr=np.zeros((5,5),np.float)
tm=time.ctime()

# def index(request):
#     return HttpResponse("<h1 id='h1' style='color:red' >i</h1><script>var t=0;h=document.getElementById('h1');var int=setInterval(function(){h.textContent=++t;},1000);</script>")

# def about(request):
#     dtext=(request.GET.get('text','default'))
#     return HttpResponse(f"you sent {djtext}")

# def me(request):
#     params={'name':'rudra','location':'mars'}
#     return render(request,'index.html',params)

def analyze(request):
    
    return render(request,'index.html')
    # return HttpResponse("analyze")

def result(request):
 try:
    djtext=request.GET.get('text','default')
    ischeck=request.GET.get('checkbox','off')
    iscapital=request.GET.get('capitalize','off')
    isremovenewline=request.GET.get('newlineremove','off')
    charcount=request.GET.get('charcount','0')
    punctList='''!,"':;?<>.|\{-}_!'''
    analyzedText=""
    if ischeck=='on':
        for i in djtext:
            if i not in punctList:
                analyzedText+=i 
    else:
        analyzedText=djtext

    if iscapital=='on':
        analyzedText=analyzedText.upper()

    if isremovenewline=='on':
        analyzedTextTemp=""
        for i in analyzedText:
            if i=='\n' or i=='\r':
               analyzedTextTemp+=' '
            else:
                analyzedTextTemp+=i
        analyzedText=analyzedTextTemp
    
    if charcount=='on':
     charcount=len(analyzedText)
    
    params={'text':djtext,'ischeck':ischeck,'isremovenewline':isremovenewline,'anl_text':analyzedText,'charcount':charcount}
    return render(request,'result.html',params)
 except Exception as e:
     return HttpResponse(e)

def data(request):
    return render(request,'data.txt')

def bootstrp(request):
    return render(request,'bootstrp.html')