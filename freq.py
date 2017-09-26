import re, sys
from collections import Counter
args = sys.argv
f = open(args[1],'r',encoding='utf-8')
fall = f.read()
words=re.split('[\n\t0123456789,.:/ _"()?-]+',fall)
count = Counter(words)
print(count)
f.close
                        
