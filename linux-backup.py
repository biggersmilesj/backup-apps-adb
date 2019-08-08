from subprocess import PIPE, Popen
import os, sys

try:
    path =  os.getcwd() + "/Apks"
    os.mkdir(path)
    print("Folder Created\n\n")
    pass

except:
    print("Folder Created\n\n")
    pass

os.chdir(path)

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

for i in range(3):
    cmdline("adb devices")

print("Fetching Packages list from device\n\n")

list=cmdline("adb shell pm list packages -f -3")

applist = str(list).split("\\npackage:")
applist[0]=applist[0][applist[0].find(":")+1:]
applist[-1]=applist[-1][:applist[-1].find("\\")]

print("Packages are fethced\n\n")

print("Copying Started\n\nTotal "+str(len(applist))+" Apps")

y=1
for i in applist:
    print(i)
    name=i[i.find("base.apk")+9:]
    name=str(name)+".apk"
    print(str(y)+ " : "+name)	
    i=i[:i.find("base.apk")+8]
    cmdline("adb pull  "+i)
    os.rename("base.apk",name)
    y=y+1
