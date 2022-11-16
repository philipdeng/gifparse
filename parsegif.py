# @Fei

import numpy as np

# global vars
GCExt   = 0xF9
COMMENT = 0xFE
APPExt  = 0xFF
UNKNOWN = 0x01
IMAGE   = 0x2C
EOF     = 59
EXT     = 0x21

class Stream():

    def __init__(self, data) -> None:
        self.data = data
        self.pos = 0
        self.len = len(data)
        self.gif = dict()
        pass

def loadData(path):

    with open(path, "rb") as f:
        data = f.read()
        return data

def dataLoaded(data):
    st = Stream(data)
    return st



def parse(st):
    
    def parseColourTable(count):
        colours = []
        i = 0
        while i < count:
            colours.append(st.data[st.pos:st.pos + 3])
            st.pos += 3
            i += 1
        return colours
    
    # parse 
    st.pos += 6
    st.gif['width'] = st.data[st.pos]
    st.pos += 1
    st.gif['width'] += (st.data[st.pos] << 8)
    st.pos += 1
    st.gif['height'] = st.data[st.pos]
    st.pos += 1
    st.gif['height'] += (st.data[st.pos] << 8)
    st.pos += 1
    st.gif['bitField'] = st.data[st.pos]
    st.pos += 1
    st.gif['colorRes'] = (st.gif['bitField'] & 0b1110000) >> 4
    st.gif['globalColourCount'] = 1 << ((st.gif['bitField'] & 0b111) + 1)
    st.gif['bgColourIndex'] = st.data[st.pos]
    st.pos += 1
    # parse colourtable
    if st.gif['bitField'] & 0b10000000:
        st.gif['globalColourTable'] = parseColourTable(st.gif['globalColourCount'])
    # parseBlock
    pass

def entry():
    
    data = loadData('Wax_fire.gif')
    st = dataLoaded(data)
    res = parse(st)

entry()