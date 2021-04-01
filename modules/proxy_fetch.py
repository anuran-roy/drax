import requests
from lxml.html import fromstring
import sys
from datetime import datetime
import os
#class ProxyError(Exception):
#    '''Proxy source(s) not found.'''
#    pass

def get_proxies():
    try:
        urls = [
            'https://free-proxy-list.net/'
        ]

        proxies = set()
        for url in urls:
            response = requests.get(url)
            parser = fromstring(response.text)
            
            for i in parser.xpath('//tbody/tr')[:10]:
                if i.xpath('.//td[7][contains(text(),"yes")]'):
                    #Grabbing IP and corresponding PORT
                    proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                    proxies.add(proxy)
        return proxies
    except Exception as ex:
        #raise ProxyError
        print(f"Error occured while fetching proxies from online. Error details: {ex}")
        return None        

def read_from_file(path):
    try:
        fopen=open(path,'r');
        proxies=fopen.readlines()
        return proxies
    except Exception as ex:
        #raise ProxyError
        print(f"Error occured while fetching proxies from online. Error details: {ex}")
        return None    

def write_to_file(addr):
    try:
        nn="./modules/proxies"+str(datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))+".txt"
        os.rename("./modules/proxies.txt",nn)
        fw=open('./modules/proxies.txt','a')
        addr=list(addr)
        fw.writelines(addr)
        fw.close()
    except Exception as ex:
        print(f"Error writing to buffer file. Error details: {ex}")    

def run():
    while True:
        prx=input("drax>proxy: ")
        if prx=="exit":
            print("Exiting Drax...")
            sys.exit()
        if prx=="back":
            break
        try:
            if prx=="help":
                print(open("./modules/proxy_help.txt","r").read())
            else:
                if prx=="get online":
                    print("Getting proxies from online")
                    resp=get_proxies()
                    if resp is not None:
                        write_to_file(resp)
                    else:
                        print("There's some problem with scraping the IP addresses.")
                elif prx=="read file":
                    resp=read_from_file(input("Enter absolute path of IP addresses."))
                    if resp is not None:
                        write_to_file(resp)
                    else:
                        print("There's some problem with reading the file.")    
        except Exception as e:
            print(f"Some error occured! Error details: {e}")
