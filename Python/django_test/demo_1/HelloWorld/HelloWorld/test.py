# f = open('/Users/neo/Coding/Python/django_test/demo_1/HelloWorld/HelloWorld/brushing_time.txt','r')
# str = f.read()
# f.close()
# dic = dict(str)
# print(dic)

# with open('/Users/neo/Coding/Python/django_test/demo_1/HelloWorld/HelloWorld/brushing_time.txt','r') as f:
#     dic = []
#     for line in f.readlines():
#         line = line.strip("\n")
#         b = line.split(' ')
#         dic.append(b)
# dic = dict(dic)
# print(dic)

import json
file = open('/Users/neo/Coding/Python/django_test/demo_1/HelloWorld/HelloWorld/brushing_time.txt','r')
js = file.read()
dic = json.loads(js)
print(dic)
print(dic['IUL'])
file.close()
