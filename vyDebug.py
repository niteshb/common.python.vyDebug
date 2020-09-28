from pprint import pprint

class vyDebugLevel():
    NONE = 0
    SILENT = 0
    TALK = 1
    VERBOSE = 2
    NOISY = 3
    BLARING = 4
    CACOPHONOUS = 5
    MAX = 5

class vyDebug():
    def noPrint(*args, **kwargs):
        return

    def __init__(self, level):
        self.level = level
        self.prints = [vyDebug.noPrint] * (vyDebugLevel.MAX + 1) 
        self.llprint0 = print
        self.llprint1 = vyDebug.noPrint
        self.llprint2 = vyDebug.noPrint
        self.llprint3 = vyDebug.noPrint
        self.llprint4 = vyDebug.noPrint
        self.llprint5 = vyDebug.noPrint
        self.setPrints()

    def setLevel(self, level):
        self.level = level
        self.setPrints()
    
    def __getattr__(self, attr):
        if attr.startswith('print'):
            suffix = attr[5:]
            if suffix in [str(_) for _ in range(vyDebugLevel.MAX + 1)]:
                return self.prints[int(suffix)]


    def setPrints(self):
        for idx in range(self.level + 1):
            self.prints[idx] = print
        for idx in range(self.level + 1, vyDebugLevel.MAX + 1):
            self.prints[idx] = vyDebug.noPrint

