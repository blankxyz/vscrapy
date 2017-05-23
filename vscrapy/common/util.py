import logging
from urllib import request
from urllib.error import  URLError, HTTPError
from bs4 import BeautifulSoup
import chardet
import socket
socket.setdefaulttimeout(30)

class GetWhois:
    def __init__(self, url):
        self.url = url

    def getDomainInfo(self):
        domain = 'http://whois.chinaz.com/' + self.url

        try:
            response = request.urlopen(domain)
        except URLError as e:
            if isinstance(e.reason, socket.timeout):
                self.log('socket timeout \n'
                         "network meets some problems: \n"
                         "Reason: ", e.reason)
        else:
            if response != None:
                the_page = response.read()
                char = chardet.detect(the_page)
                # 解码为unicode
                the_page.decode(char['encoding'], 'ignore')
                soup = BeautifulSoup(the_page)

                # <div class="div_whois">
                # 因为http://whois.chinaz.com/返回的信息
                # 包含在 <div class="div_whois">标签中，直接获取

                domain = soup.find('div', class="whoisinfo clearfix")

                return domain

if __name__ == '__main__':
    print(GetWhois('www.baidu.com').getDomainInfo())