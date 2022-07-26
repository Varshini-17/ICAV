# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cgi import test
from email.utils import collapse_rfc2231_value
import json

from django.shortcuts import render,redirect
import os, sys

# Create your views here.
from .models import *
from django.http.response import HttpResponse, JsonResponse
from django.apps import apps
import csv

def index(request):

    return render(request,"home.html")

def readcsv():
    with open("/home/varsh/Desktop/ICAV/demo/app/data/books.csv", "r") as file:
        reader = csv.reader(file)
        column_names = next(reader)
        reader=list(reader)[:]
    return (column_names,list(reader))

def endpoint1(request):
    if request.method=='POST':
    	c=int(request.POST.get("count1"))
    l=1
    l1=[]
    dict={}
    col,reader=readcsv()
    data = {col: [] for col in col}
    for row in reader:
        if l<=c:
            dict_from_list = {col[i]: row[i] for i in range(len(col))}
            l1.append(dict_from_list)
            l+=1
    res={"books":l1}
    return JsonResponse(res,safe=False)

def endpoint2(request):
    if request.method=='POST':
        coll=request.POST.get("col")
        vall=request.POST.get("val")
    fil_col=coll
    fil_val=vall
    print("fbjrdng",type(fil_col),fil_val)
    l1=[]
    col,reader=readcsv()
    # d2=filter((lambda x: x["authors"] in ("Jesse Grant", "05FT", "66DM")), list(reader))
    for row in reader:
        d2={col[i]: row[i] for i in range(len(col))}
        # ("authors","Jesse Grant")
        try:
            if fil_col in col:
                if (fil_col,fil_val) in d2.items():
                    print("vhvh",d2['id'])
                    l1.append(d2)
            else:
                l1="Column doesn't exist"
        except:
            print("Not found")
     
        

    return JsonResponse(l1,safe=False)
