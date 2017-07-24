import  logging

class LoggingExample:
    logfile="logging.txt"
    logging.basicConfig(filename=logfile,level="DEBUG")
    logging.debug("First Line to the file")

    def readFromFile(self):
        i=0
        with open(LoggingExample.logfile,"a+") as f:
            content=f.read()
            print "Reading from File:"
            print content
        f.close()

    def writeContentToFile(self):
        f =open(LoggingExample.logfile,"a+")
        exampleList = ["q","w","e","r"]
        for i in exampleList:
            f.write(i)

log = LoggingExample()
log.writeContentToFile()
log.readFromFile()





