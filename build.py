import sys

projectName="test"

def createBuild():
    print("creating new  file")
    
    extension="love"
    try:
        name=projectName+"."+extension
        file=open(name,'a')

        file.close()
    except:
            print("error occured")
            sys.exit(0)

createBuild()
