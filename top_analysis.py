import sys
from datetime import datetime
for line in iter(sys.stdin.readline, ""):
    d=datetime.now()
    print(d.strftime("%Y/%m/%d %H:%M:%S.")+("%06d"%d.microsecond)+" "+line, end='', flush=True)