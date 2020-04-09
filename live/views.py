from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Report
import request
import json


from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service

service = Service('/Users/Dell pc/Desktop/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)


def world(country):
    driver.get("https://www.worldometers.info/coronavirus/")
    content1 = driver.page_source
    soup1 = BeautifulSoup(content1)
    r = []
    for a in soup1.findAll('div', attrs={'class': 'maincounter-number'}):
        r.append(a.text)
    rows = soup1.find_all('tr')

    s = {}
    for row in rows:
        cells = row.find_all('td')

        if len(cells) == 13:
            if cells[0].text not in s:
                s[cells[0].text] = [cells[1].text, cells[3].text, cells[6].text]

    return s,r

def indi(state):
    driver.get("https://www.covid19india.org/")
    time.sleep(2)
    content1 = driver.page_source
    soup1 = BeautifulSoup(content1)
    ty = soup1.find_all('tr', attrs={'class': 'state'})
    ee = {}
    for row in ty:
        cells = row.find_all('td')

        if cells[0].text not in ee:
            li = []
            for ele in cells:
                f = ele.find_all('span', attrs={'class': 'table__count-text'})
                for ele in f:
                    li.append(ele.text)

            ee[cells[0].text] = li
    tx = soup1.find_all('tr', attrs={'class': 'district'})
    er = {}
    for row in tx:
        cells = row.find_all('td')

        if cells[0].text not in er:
            li = []
            for ele in cells:
                f = ele.find_all('span', attrs={'class': 'table__count-text'})
                for ele in f:
                    li.append(ele.text)

            er[cells[0].text] = li
    tt = soup1.find_all('div', attrs={'class': 'Level'})
    ra = []
    for ele in tt:
        cc = ele.find_all('h1')
        for ele in cc:
            ra.append(ele.text)

    return ee,er,ra


def update(dd):
    driver.get("https://timesofindia.indiatimes.com/india/coronavirus-india-live-updates-madhya-pradesh-covid-19-tally-rises-to-20-five-test-positive-in-indore/liveblog/74820018.cms")
    content1 = driver.page_source
    soup1 = BeautifulSoup(content1)
    red = []
    for a in soup1.findAll('div', attrs={'class': '_1KydD'}):

        red.append(a.text)
    f = {}
    for i in range(len(red)):
        f[i + 1] = red[i]
    return f

def about(request):
    ww=update('dd')
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
        results = ("you have covid")
        flag = False
    elif (age) > 60 and abroad == "Y" and fever == "Y" and cough == "Y":
        results = ("you have covid")
        flag = False
    elif fever == "Y" and cough == "Y" and sb == "N" and rn == "N" and tiredness == "Y":
        results = ("you have flu")
        flag = False
    elif fever == "N" and cough == "Y" and sb == "N" and rn == "Y" and tiredness == "N":
        results = ("you have cold")
        flag = False
    else:
        results = ("you have seasonal illness,nothing to worry")
    if request.GET.get('age11') and request.GET.get('age12') and request.GET.get('age13') and request.GET.get('age14') and request.GET.get('age15'):
        sus = Report()
        sus.name = request.GET.get('age11')
        sus.mobile = request.GET.get('age12')
        sus.susceptm = request.GET.get('age13')
        sus.suspectname = request.GET.get('age14')
        sus.suspectadress = request.GET.get('age15')
        sus.save()
        return render(request, 'covid/result.html')



    return render_to_response('covid/about.html', {'red': ww,'result':results})

def suspect(request):
    print("rahul")
    if request.method == "POST":
        if request.POST.get('age11') and request.POST.get('age12') and request.POST.get('age13') and request.POST.get('age14') and request.POST.get('age15'):
            sus=Report()
            sus.name=request.POST.get('age11')
            sus.mobile=request.POST.get('age12')
            sus.susceptm=request.POST.get('age13')
            sus.suspectname=request.POST.get('age14')
            sus.suspectadress=request.POST.get('age15')
            sus.save()
            return render(request,'covid/result.html')
        return render(request, 'covid/india.html')
    else:
        return render(request,'covid/home.html')


def india(request):
    ee, er, ra = indi('Bihar')

    z1=ra[0]
    z2=ra[1]
    z3=ra[2]
    z4=ra[3]
    fg = request.GET.get('state')
    print(fg)
    fg=str(fg)
    if fg in ee:
        cn=ee[fg]
        d0="Status for"+str(fg)
        d1=cn[0]
        d2=cn[1]
        d3=cn[2]
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
    s,r=world('USA')
    #ee,er,ra=indi('Bihar')
    tv=s['World']
    to=r[0]
    t1=r[1]
    t2=r[2]
    t3=tv[2]
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

    return render_to_response('covid/home.html',{'world':s,'wc1':to,'wc2':t1,'wc3':t2,'wc4':t3,'c1':c1,'c2':c2,'c3':c3,'c0':c0})

