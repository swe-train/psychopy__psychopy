
lastFrame = string(default='both')
skipVersion=string(default='')  #skipping any updates of this version

[coder]
winX = integer(default=100)
winY = integer(default=100)
winH = integer(default=800)
winW = integer(default=600)
auiPerspective = string(default='')
state = option('normal','maxim', default='normal')
fileHistory = list(default=list())  #files in history
prevFiles = list(default=list())  #file open on last save
showIndentGuides = boolean(default=True)
showWhitespace = boolean(default=True)
showEOLs= boolean(default=False)
    
[builder]
fileHistory = list(default=list())  #files in history
prevFiles = list(default=list())  #file open on last quit    
    
    [[frames]]
    
        [[[__many__]]]
        winX = integer(default=50)
        winY = integer(default=50)
        winH = integer(default=600)
        winW = integer(default=800)
        auiPerspective = string(default='')
        state = option('normal','maxim', default='normal')
        lastOpened = integer(default=0)
    
    [[defaultFrame]]
    winX = integer(default=50)
    winY = integer(default=50)
    winH = integer(default=600)
    winW = integer(default=800)
    auiPerspective = string(default='')
    state = option('normal','maxim', default='normal')
    lastOpened = integer(default=0)