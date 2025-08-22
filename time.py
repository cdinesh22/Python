import time
import sys
h=3
m=40
s=0
ms=0
while(True):
    sys.stdout.write(f"\r {h:02d} : {m:02d} :{s:02d} : {ms:02d}")   #\r means it will bring cursor to begining
    sys.stdout.flush()
    print()
    time.sleep(0.01)
    ms=ms+1
    if(ms==60):
        ms=0
        s=s+1
    if(s==60):
        s=0
        m=m+1
    if(m==60):
        s=0
        h=h+1
    if(h==12):
        h=0
        s=0
        m=0
        
