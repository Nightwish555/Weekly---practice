__author__="Nightwish"
__title__="正则表达式"

import re

text="JGood is a handsome boy,he is cool"
print(re.findall("\w+oo\w+",text))

