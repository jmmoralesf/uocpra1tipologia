from bs4 import BeautifulSoup
import requests
import sys
import csv

def storeURL(str):
    page = requests.get(str)
    soup = BeautifulSoup(page.content)
    newline=[]
    company=[]
    categoria=[]
    web=[]
    phone=[]
    loca=[]
    companydata=soup.find_all('a',href=True)
    
    m=int(len(companydata)/5)
    for n in range(0,m):
        company.append(companydata[1+n*5].text)
        categoria.append((companydata[2+n*5].text).lstrip())
        web.append((companydata[3+n*5].text).lstrip())
        loca.append((companydata[4+n*5].text).lstrip())
    phonet=soup.find_all('div',{'class':'blog-meta'})
    s=len(phonet)
    for w in range(0,s):
        phonete=phonet[w].text
        phonete=phonete[-11:-4]
        phone.append(phonete.rstrip())
    for w in range(0,s):
        newline=company[w]+","+categoria[w]+","+web[w]+","+loca[w]+","+phone[w]
        #print(newline)
        myfile2.writerow(newline)
    return
def enlaces(enlace):
    page = requests.get(enlace)
    soup = BeautifulSoup(page.content)
    lin=[]
    lin2=[]
    for link in soup.find_all('a',href=True):
        li=link.get('href')
        if('categoryposts/' in li):
            lin.append(li)
    ## Se limpian links repetidos
    for link in lin:
        if (link not in lin2):
            lin2.append(link)
    return lin2;
def enlaces2(enlace):
    page = requests.get(enlace)
    soup = BeautifulSoup(page.content)
    lin=[]
    lin2=[]
    lin4=[]
    
    for link in soup.find_all('a',href=True):
        li=link.get('href')
        if('categoryposts_ajax/6/list' in li):
            lin.append(li)
    ## Se limpian links repetidos
    for link in lin:
        if (link not in lin2):
            lin2.append(link)
    n=len(lin2)        
    for s in range (0,n):
        tempolin=lin2[s].replace("categoryposts_ajax/6/list","categoryposts_ajax/20/list")
       
        lin4.append(tempolin)
    return lin4; 
lin3=enlaces("http://www.paginasamarillasdepanama.com")
n=len(lin3)
lin4=[]
m=0
for m in range (0,n):
    lin4.append(enlaces2(lin3[m]))
    m=m+1
n2=len(lin4)

with open("yellowpanama.csv", 'w',newline='') as myfile:
    myfile2 = csv.writer(myfile, delimiter=' ',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for s in range (0,n2):
        enlace3=' '.join(lin4[s])
        storeURL(enlace3)
    myfile.close()

    
