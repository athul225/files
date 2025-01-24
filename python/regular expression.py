#Regular expresions

# 1. split
import re
a="welcome to all"
print(re.split('\s',a))
print(re.split('o',a))

# 2. sub
import re
a="wlecome to all"
print(re.sub('to','TO',a))

# 3.findall
import re
a="welcome to all to"
print(re.findall('to',a)) 

# 4. search
import re
a="Welcome to all 5"
b="we"
c="w"
d="Cr7"
print(re.search('to',a))
print(re.search('l',a))
print(re.search('l.',a))
print(re.search('w.*',b))
print(re.search('w.+',b))
print(re.search('w.?',b))
print(re.search('w.?',c))
print(re.search('[a-z]',a))
print(re.search('[A-Z]',a))
print(re.search('[0-9]',a))
print(re.search('[A-Za-z0-9]',a))
print(re.search('[A-Z][a-z][0-9]',a))
print(re.search('[A-Z][a-z][0-9]',d))
