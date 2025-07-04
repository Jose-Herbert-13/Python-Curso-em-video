import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31m O site não está acessível no momento')
else:
    print('\033[32m O site está acessível')
