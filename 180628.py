# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:07:13 2018

@author: Terry
"""


'''
Q1
'''
print("="*5,"Q1作业","="*5)

citycode = ['010','021','022','023','024','025','027','028','029','020']
print(citycode)


'''
Q2
'''
print("="*5,"Q2作业","="*5)

q2_list = [1,2,3,4,5,6,7,8,9]
q2_a1 = q2_list[1::2] 
q2_a2 = (q2_list[:3:2] + q2_list[3:4] + q2_list[4::2])[::-1]
q2_a3 = q2_list[:4]
q2_a4 = q2_a3[::-1] 
print(q2_a1)
print(q2_a2)
print(q2_a3)
print(q2_a4)


'''
Q3
'''
print("="*5,"Q3作业","="*5)
q3_dic = {
        "Tom" : '1234567890',
        "Jerry" : '0987654321'
        }
print(q3_dic)


'''
Q4
'''
print("="*5,"Q4作业","="*5)
q4_dic = {
        "lang" : 'python',
        "number" : '100'
        }

print(q4_dic)
q4_a1 = q4_dic['lang']
print(q4_a1)

key_list=[]
value_list=[]

for key,value in q4_dic.items():
    key_list.append(key)
    value_list.append(value)
 
get_value = '100'
if get_value in value_list:
    get_value_index = value_list.index(get_value)
    print("%s 的键：%s" % (get_value , key_list[get_value_index]) )
else:
    print("你要查询的值%s不存在" %get_value)
       
q4_a3 = len(q4_dic)
print(q4_a3)

q4_dic['City'] = "Shanghai"
print(q4_dic)

del q4_dic['City']
print(q4_dic)

q4_dic['number'] = "200"
print(q4_dic)

print('city' in q4_dic.keys())



'''
Q5
'''
print("="*5,"Q5作业","="*5)
q5_dic = {
        "China" : 'Beijing',
        "USA" : 'Washington,D.C.',
        "Japan" : 'Tokyo',
        "Germany" : 'Berlin',
        "Russia" : 'Moscow'
        }

q5_key_list = list(q5_dic.keys())
q5_value_list = []

for q5_i in q5_key_list:
    q5_value_list.append(q5_dic[q5_i])
        
for q5_j in q5_key_list:
    print(q5_j)      
q5_get_value = input("请参考以上清单输入要查的城市名称：" )


if q5_get_value in q5_key_list:
    q5_get_value_index = q5_key_list.index(q5_get_value)
    print("%s 的首都是：%s" % (q5_get_value , q5_value_list[q5_get_value_index]) )
else:
    print("你要查询的城市%s不在字典内" %q5_get_value)

    