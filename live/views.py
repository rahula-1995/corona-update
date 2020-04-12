from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from .models import Report,State,District,Country,headWorld,headIndia
from rest_framework.views import APIView
from rest_framework import status
from .serialiser import Countrysearializer,Statesearializer,Districtsearializer,headWorldsearializer,headindiasearializer
from rest_framework.response import Response
import request
import json


from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import InvalidSessionIdException
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

service = Service(CHROMEDRIVER_PATH)


#service = Service('/Users/Dell pc/Desktop/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)

class country(APIView):

    def get_object(self, pk):
        try:
            return Country.objects.filter(country_name=pk)
        except Country.DoesNotExist:
            return Response({'message': 'Country not in my list'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk):
        worldl=self.get_object(pk)
        serializer= Countrysearializer(worldl,many=True)
        return Response(serializer.data)

class state(APIView):

    def get_object(self, pk):
        try:
            return State.objects.filter(state_name=pk)
        except State.DoesNotExist:
            return Response({'message': 'state not in my list'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk):
        worldl=self.get_object(pk)
        serializer=Statesearializer(worldl,many=True)
        return Response(serializer.data)

class district(APIView):

    def get_object(self, pk):
        try:
            return District.objects.filter(district_name=pk)
        except District.DoesNotExist:
            return Response({'message': 'district not in my list'}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request,pk):
        worldl=self.get_object(pk)
        serializer=Districtsearializer(worldl,many=True)
        return Response(serializer.data)

class headworld(APIView):



    def get(self, request):
        worldl=headWorld.objects.all()
        serializer=headWorldsearializer(worldl,many=True)
        return Response(serializer.data)

class headindia(APIView):


    def get(self, request):
        worldl=headIndia.objects.all()
        serializer=headindiasearializer(worldl,many=True)
        return Response(serializer.data)

class countryall(APIView):


    def get(self, request):
        worldl=Country.objects.all()
        serializer= Countrysearializer(worldl,many=True)
        return Response(serializer.data)

class stateall(APIView):

    def get(self, request):
        worldl=State.objects.all()
        serializer=Statesearializer(worldl,many=True)
        return Response(serializer.data)


class districtall(APIView):


    def get(self, request):
        worldl = District.objects.all()
        serializer = Districtsearializer(worldl, many=True)
        return Response(serializer.data)





def world(country):
    driver.get("https://www.worldometers.info/coronavirus/")
    content1 = driver.page_source
    soup1 = BeautifulSoup(content1)
    r = []
    for a in soup1.findAll('div', attrs={'class': 'maincounter-number'}):
        r.append(a.text)
    rows = soup1.find_all('tr')

    worlddict = {}
    for row in rows:
        cells = row.find_all('td')

        if len(cells) == 13:
            if cells[0].text not in worlddict:
                worlddict[cells[0].text] = [cells[1].text, cells[3].text,cells[5].text, cells[6].text]

    for key,value in worlddict.items():
        if len(Country.objects.filter(country_name=key))>0:

            c=Country.objects.filter(country_name=key)
            c.update(country_case=value[0])
            c.update(country_active_case=value[3])
            c.update(country_recovered_case=value[2])
            c.update(country_death_case=value[1])

        else:
            c=Country()
            c.country_name=key
            c.country_case=value[0]
            c.country_active_case=value[3]
            c.country_recovered_case=value[2]
            c.country_death_case=value[1]
            c.save()


    return worlddict,r

def indi(state):
    driver.get("https://www.covid19india.org/")
    time.sleep(2)
    content1 = driver.page_source
    soup1 = BeautifulSoup(content1)
    statedata = soup1.find_all('tr', attrs={'class': 'state'})
    statedict = {}
    for row in statedata:
        cells = row.find_all('td')

        if cells[0].text not in statedict:
            li = []
            for ele in cells:
                f = ele.find_all('span', attrs={'class': 'table__count-text'})
                for ele in f:
                    li.append(ele.text)

            statedict[cells[0].text] = li

    for key,value in statedict.items():
        if len(State.objects.filter(state_name=key))>0:

            c=State.objects.filter(state_name=key)
            c.update(state_case=value[0])

            c.update(state_recovered_case=value[1])
            c.update(state_death_case=value[2])

        else:
            c=State()
            c.state_name=key
            c.state_case=value[0]

            c.state_recovered_case=value[1]
            c.state_death_case=value[2]
            c.save()

    districtdata = soup1.find_all('tr', attrs={'class': 'district'})
    districtdict = {}
    for row in districtdata:
        cells = row.find_all('td')

        if cells[0].text not in districtdict :
            li = []
            for ele in cells:
                f = ele.find_all('span', attrs={'class': 'table__count-text'})
                for ele in f:
                    li.append(ele.text)

            districtdict[cells[0].text] = li

    for key,value in districtdict.items():
        if len(District.objects.filter(district_name=key))>0:

            c=District.objects.filter(district_name=key)
            c.update(district_cases=value[0])

        else:
            c=District()
            c.district_name=key
            c.district_cases=value[0]

            c.save()

    tt = soup1.find_all('div', attrs={'class': 'Level'})
    ra = []
    for ele in tt:
        cc = ele.find_all('h1')
        for ele in cc:
            ra.append(ele.text)


    if (headIndia.objects.count())>0:

        headIndia.confirmed_india_case=ra[0]
        headIndia.active_india_case = ra[1]
        headIndia.india_death_case=ra[2]
        headIndia.recovered_india_case = ra[3]
    else:
        c=headIndia()
        c.confirmed_india_case=ra[0]
        c.active_india_case=ra[1]
        c.india_death_case=ra[2]
        c.recovered_india_case=ra[3]

        c.save()

    return statedict,districtdict,ra


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



    return render_to_response('covid/about.html', {'red': ww,'result':results})




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

