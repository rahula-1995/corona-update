from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Report

import request
import json


#from selenium import webdriver
#from bs4 import BeautifulSoup
import time
#from selenium.webdriver.chrome.service import Service

#from selenium.common.exceptions import InvalidSessionIdException
#GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
#CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

#service = Service(CHROMEDRIVER_PATH)


#service = Service('/Users/Dell pc/Desktop/chromedriver')
#service.start()
#driver = webdriver.Remote(service.service_url)


import requests



def world(country):
    worlddata = requests.get('https://coronaupdate-api.herokuapp.com/worlddata/')
    data1 = worlddata.json()
    worlddict = {}
    for ele in data1:
        s = []
        for key, value in ele.items():
            s.append(value)
        worlddict[s[0]] = s[1:]
    ra=worlddict['India']

    return worlddict,ra

def indi(state):
    statedata = requests.get('https://coronaupdate-api.herokuapp.com/indiadata/')
    data2 = statedata.json()

    statedict = {}
    for ele in data2:
        s = []
        for key, value in ele.items():
            s.append(value)
        statedict[s[0]] = s[1:]

    districtdata = requests.get('https://coronaupdate-api.herokuapp.com/districtdata/')
    data3 = districtdata.json()

    districtdict = {}
    for ele in data3:
        s = []
        for key, value in ele.items():
            s.append(value)
        districtdict[s[0]] = s[1:]

    maindatas = requests.get('https://coronaupdate-api.herokuapp.com/indiahead/')
    data4 = maindatas.json()

    #maindata = []
    #for ele in data4:
        #for key, value in ele.items():
            #maindata.append(value)


    return statedict,districtdict


#def update(dd):
    #driver.get("https://timesofindia.indiatimes.com/india/coronavirus-india-live-updates-madhya-pradesh-covid-19-tally-rises-to-20-five-test-positive-in-indore/liveblog/74820018.cms")
    #content1 = driver.page_source
    #soup1 = BeautifulSoup(content1)
    #red = []
    #for a in soup1.findAll('div', attrs={'class': '_1KydD'}):

        #red.append(a.text)
    #f = {}
    #for i in range(len(red)):
        #f[i + 1] = red[i]
    #return f

def about(request):
    #ww=update('dd')
    if (request.GET.get('age')):
        age=int(request.GET.get('age'))
    else:
        age=int(30)
    abroad = request.GET.get('age1')
    fever = request.GET.get('age2')
    cough = request.GET.get('age3')
    sb = request.GET.get('age4')
    rn = request.GET.get('age5')
    tiredness = request.GET.get('age6')
    if fever == 'Y' and cough == 'Y' and sb == 'Y' and tiredness == 'Y' and rn == 'N':
        results = ("you have been infected with coronavirus")
    elif (age) > 60 and abroad == "Y" and fever == "Y" and cough == "Y":
        results = ("you have been infected with coronavirus")

    elif fever == "Y" and cough == "Y" and sb == "N" and rn == "N" and tiredness == "Y":
        results = ("you have flu")

    elif fever == "N" and cough == "Y" and sb == "N" and rn == "Y" and tiredness == "N":
        results = ("you have cold")

    else:
        results = ("you have seasonal illness,nothing to worry")
    if request.GET.get('age11') and request.GET.get('age12') and request.GET.get('age13') and request.GET.get('age14') and request.GET.get('age15'):
        sus = Report()
        sus.informer_name = request.GET.get('age11')
        sus.informer_mobile = request.GET.get('age12')
        sus.suspect_mobile = request.GET.get('age13')
        sus.suspect_name = request.GET.get('age14')
        sus.suspect_adress = request.GET.get('age15')
        sus.save()
        return render(request, 'covid/result.html')


    return render_to_response('covid/about.html', {'result':results})




def india(request):
    ee, er = indi('Bihar')
    nm,ra=world('abc')


    z1=ra[0]
    z2=ra[1]
    z3=ra[2]
    z4=ra[3]
    fg = request.GET.get('state')
    fg=str(fg)
    if fg in ee:
        cn=ee[fg]
        d0="Status for"+str(fg)
        d1=cn[0]
        d2=cn[2]
        d3=cn[3]
    else:
        d0="Please type the state name"
        d1=0
        d2=0
        d3=0
    fh = request.GET.get('district')
    fh=str(fh)
    if fh in er:
        dn=er[fh]
        e0="Status for"+str(fh)
        e1=dn[0]

    else:
        e0="Please type the district name"
        e1=0


    return render_to_response('covid/india.html',{'z1':z1,'z2':z2,'z3':z3,'z4':z4,'state':ee,'district':er,'d0':d0,'d1':d1,'d2':d2,'d3':d3,'e0':e0,'e1':e1})

def index(request):
    s=world('USA')
    #ee,er,ra=indi('Bihar')
    tv=s['World']
    tc=tv[0]
    ta=tv[1]
    tr=tv[2]
    td=tv[3]
    fv = request.GET.get('country')
    if fv in s:
        bn=s[fv]
        c0="Status for"+str(fv)
        c1=bn[0]
        c2=bn[1]
        c3=bn[2]
    else:
        c0="Please type the country name"
        c1=0
        c2=0
        c3=0

    return render_to_response('covid/home.html',{'world':s,'wc1':tc,'wc2':td,'wc3':tr,'wc4':ta,'c1':c1,'c2':c2,'c3':c3,'c0':c0})

