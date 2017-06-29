from lxml import html
import myvariables as myvar
import requests
import os

LOOKUP_STR = myvar.LOOKUP_STRING

PAGES_LIST = myvar.PAGES_LIST

def main():
    print("\nSubito.it Scraper - Luca Scotton 2017\n")
    print("Looking for:",LOOKUP_STR,"\n\n")
    found = list()
    for p in PAGES_LIST:
        tmp = parsepage(p,LOOKUP_STR)
        for (item,link,date,pos) in tmp:
            print(date,"\t",pos,"\t",item,"\n\t\t\t\t\t",link,"\n")
        found += tmp
    os.system("pause")

def parsepage (url,stringa):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    items = tree.xpath('//div[@class="item_list_section item_description"]/h2/a/text()')
    prices = tree.xpath('//div[@class="item_list_section item_description"]/span[@class="item_price"]/text()')
    links = tree.xpath('//div[@class="item_list_section item_description"]/h2/a/@href')
    datetimes = tree.xpath('//div[@class="item_list_section item_description"]/span/time/text()')
    raw_positions = tree.xpath('//div[@class="item_list_section item_description"]/span/span//text()')
    positions = list()
    found = list()
    
    #Rimuovo spazi all'inizio e fine di ogni nome e rende tutto minuscolo
    items = [i.strip().lower() for i in items]

    for (i, p) in enumerate(raw_positions):
        if (i%2 is 0):
            positions.append(p+raw_positions[i+1])
            
    for (i, item) in enumerate(items):
        if (item.find(stringa) is not -1):
            found.append((item,links[i],datetimes[i],positions[i]))

    return found

def getAnnounces():
    found = list()
    for p in PAGES_LIST:
        found += parsepage(p,LOOKUP_STR)
    return found

#main()
