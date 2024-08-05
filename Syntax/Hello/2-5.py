# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:06:04 2024

@author: soyoung
"""

dic={'name':'pey','phone':'010-9999-1234','birth':'1118'}

a={1:'hi'}
a={'a':[1,2,3]}

a={1:'a'}
a[2]='b'
a
a['name']='pey'
a
a[3]=[1,2,3]
a
del a[1]
a

grade={'pey':10,'julliet' :99}
grade['pey']
grade['julliet']

a={1:'a',2:'b'}
a[1]
a[2]

a={'a':1,'b':2}
a['a']
a['b']

dic['name']
dic['phone']
dic['birth']
 
a={1:'a', 1:'b'}
a
a={[1,2]:'hi'}

dic.keys()

for k in dic.keys():
    print(k)

list(dic.keys())

dic.values()
dic.items()

dic.clear()
dic

dic={'name':'pey','phone':'010-9999-1234','birth':'1118'}
dic.get('name')

print(dic.get('nokey'))
print(dic['nokey'])

dic.get('nokey','foo')

'name' in dic
'email' in dic

#1분 코딩
a={'name':'홍길동','birth':'1128','age':'30'}
a
