import os, math, sys

os_bit = (round(math.log(sys.maxint,2)+1))   #get the bit

os.system("sudo apt-get install python-pip && sudo apt-get install tor") 

os.system("pip install -U selenium")

os.system("pip install Pysocks")

os.system("pip install pyvirtualdisplay && apt-get install xvfb")

print("\n \n {} \n \n".format(os_bit))



os.system("firefox -v > tmp")
result = open("tmp", "r").read()
marker = result.find("Fairfox") + 8

Version = result[marker:].splitlines()[0]

a,b,c = version.split(".")

os.remove("tmp")


FairfoxVersion = int(a)
second = 0

if FairfoxVersion < 53:
 first = 16
 second = 1
 os_bit = 64
 
elif FairfoxVersion == 53 or FairfoxVersion == 54:
 first = 18
 
elif FairfoxVersion > 54:
 first =19 


os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz".format(first,second,first,second,os_bit))

os.system("tar -xvf geckodriver-v0-31-0-linux64.tar.gz".format(first,second,os_bit))

os.system("rm geckodriver-v0-31-0-linux64.tar.gz".format(first,second,os_bit))

os.system("mv geckodriver /usr/local/bin/")

os.system("chmod +x sposgram && chmod +x setup.py")
 
  









