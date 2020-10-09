from pprint import pprint
from typing import List, Callable, Dict, Any

class VyDebugLevel():
    MIN: int = 0
    NONE: int = 0
    SILENT: int = 0
    TALK: int = 1
    VERBOSE: int = 2
    NOISY: int = 3
    BLARING: int = 4
    CACOPHONOUS: int = 5
    MAX: int = 5

def noPrint(*args, **kwargs):
    return

class VyDebug():
    def __init__(self, level: int=0):
        self.prints: List[Callable] = [noPrint] * (VyDebugLevel.MAX + 1) 
        self.level = level

    def __getattr__(self, attr: str):
        if attr == 'level':
            return self._level
        if attr.startswith('print'):
            suffix = attr[5:]
            if suffix in [str(_) for _ in range(VyDebugLevel.MAX + 1)]:
                return self.prints[int(suffix)]
        return super().__getattr__(attr)

    def __setattr__(self, attr: str, value: Any):
        if attr == 'level':
            assert type(value) == int
            value = max(value, -1)
            value = min(value, VyDebugLevel.MAX)
            self._level : int = value
            self.setPrints()
        else:
            super().__setattr__(attr, value)

    def setPrints(self):
        for idx in range(self.level + 1):
            self.prints[idx] = pprint
        for idx in range(self.level + 1, VyDebugLevel.MAX + 1):
            self.prints[idx] = noPrint
