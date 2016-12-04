#!/usr/bin/python3
#
# Utils is always imported first
#

def main():
    #import lank.utils
    # print (logfile)
    #lank.utils.logit("hello",1,"crit")
    
    from lank import utils
    utils.init()
    utils.logit("hello","critical")
    #utils.logit("hello","error")
    #utils.logit("hello","warning")
    #utils.logit("hello","info")
    #utils.logit("hello","debug")
    
    

if __name__ == "__main__":
    main()
