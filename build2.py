## Build2.py
import sys
from dependency2 import dependencies

buildDone=[]
dLib=[]

def deCycle(lib):
    if lib not in buildDone:
        print('build:'f'{lib}')
        buildDone.append(lib)
        print(buildDone)
        print('============================================================================================================================================================')
    if len(dependencies[lib])!=0:
        for de in dependencies[lib]:
            deCycle(de)

libList = list(map(str,input('Enter Libraries: ').split(',')))
for i in libList:
    print('\n')
    a = i.replace(" ","").lower()
    print('=============================================================================================================================================================')
    # print(a)
    
    for key in dependencies.keys():
        # print(key)
        if key in a:
            lib=key
            print('Building',lib,'\n')
            deCycle(lib)
            print('Build Done.')
            break

    else:
        print('No Math Lib of this name: ',a)
        num = int(input("want to add this lib Press 1 else press 0: "))
        if num==1:
            libName = input('Lib name: ').replace(" ","").lower()
            if libName in dependencies.keys():
                num2 = int(input('Lib Already Available\nWant to run Press 1 else press 0: '))
                if num2==1:
                    deCycle(libName)
                continue
            orderList = list(enumerate(dependencies.keys()))
            for i in range(len(orderList)):
                print(orderList[i][0]," : ",orderList[i][1])
            # dLib= list(map(str,input('Enter dependencies: ').replace(" ","").split(',')))
            dLibNum= list(map(int,input('Select dependencies: ').split(' ')))
            for i in dLibNum:
                dLib.append(orderList[i][1])

            # opening a file
            with open("dependency.py","rb+") as f:
                f.seek(-1,2)
                f.truncate()

            with open("dependency.py","a+") as fh:
                fh.write("'{}':{},".format(libName,dLib))
                fh.write('\n}')
            f.close()
                
            # file part done
            print('Added',libName)
        else:
            print('Invalid Lib')
