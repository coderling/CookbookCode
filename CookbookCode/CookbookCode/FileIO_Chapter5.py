#####################################################
## file name:FileIO_Chapter5
## create time:2016/6/19 20:44:30
## email:coderling@gmail.com
#####################################################

#test os.path
import os

def testPath():
    path = "'/Users/beazley/Data/data.csv"
    basename = os.path.basename(path)
    print(basename)

    dirname = os.path.dirname(path)
    print(dirname)

    joinPath = os.path.join('temp', 'data', os.path.basename(path))
    print(joinPath)

    newpath = '~/Data/data.csv'    userpath = os.path.expanduser(newpath)
    print(userpath)

    splitpath = os.path.splitext(newpath)
    print(splitpath)

if __name__ == "__main__":
    testPath()


