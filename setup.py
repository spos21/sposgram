import os, math, sys

#os_bit = (round(math.log(sys.maxint,2)+1)) #get the bit

os.system("apt-get install python-pip && sudo apt-get install tor")  #installing dependencies
os.system("pip install -U selenium")
os.system("pip install PySocks")
os.system("pip install pyvirtualdisplay && apt-get install xvfb")

#print("\n \n {} \n \n".format(os_bit))



os.system('firefox -v > tmp')                  # store result of firefox -v in tmp
result   =  open('tmp', 'r').read()            # result var reads the output
marker   = result.find('Firefox') + 8          # marker marks the 8th letter from the word "Firefox"
version  = result[marker:].splitlines()[0]     # spliting the output, the version is something like aa.bb.cc
a,b,c = version.split(".")                     # a is the var with the aa
os.remove('tmp')                               # removing the temporary file

FirefoxVersion = int(a)
second = 0

if FirefoxVersion  < 54:

    first = 19
    second = 1
    os_bit = 64

elif FirefoxVersion == 53 or FirefoxVersion == 54:

    first = 19

elif FirefoxVersion > 54:

    first = 19


os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz ".format(first,second,first,second,os_bit))
os.system("tar -xvf geckodriver-v0.31.0-linux64.tar.gz".format(first,second,os_bit))
os.system("rm geckodriver-v0.31.0-linux64.tar.gz".format(first,second,os_bit))
os.system("chmod +x geckodriver")
os.system("mv geckodriver /usr/local/bin/")
os.system ("chmod +x sposgram && chmod +x setup.py")
