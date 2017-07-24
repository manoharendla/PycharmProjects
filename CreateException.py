class TempException(RuntimeError):
    def __init__(self,args):
        self.args=args


def raiseError():
    try:
        raise TempException("Bad Hostanme")
    except TempException,e:
        print e

raiseError()


