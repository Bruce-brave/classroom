#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#读取文件内容
with open('report.txt','r',encoding = 'utf8') as f:
    text = f.readlines()


# In[ ]:


print(text)
print(text[1:])


# In[ ]:


#将每个人的成绩按 {姓名：xx ，科目1：分数1，科目2：分数2} 的字典形式存进一个成绩总列表中
item = text[0].strip().split(' ')
print(item)
score_dict_list = []
for i in range(len(text)-1):
    score_dict = {}
    person = text[i+1].strip().split(' ')
    for j in range(len(item)):
        score_dict[item[j]] = person[j]
    score_dict_list.append(score_dict)
print(score_dict_list)


# In[ ]:


#计算每门科目的平均成绩，并将其以{姓名：平均 ，科目1：分数1，科目2：分数2} 的字典形式存入上面的总成绩列表
aver_dict = {'姓名': '平均', '语文': 0, '数学': 0, '英语': 0, '物理': 0, '化学': 0, '生物':0, '政治':0, '历史': 0, '地理': 0}
for i in score_dict_list:
    for j in i:
        if j in item[1:]:
            score = eval(i[j])
            aver_dict[j] += score 
#        print(j,':',aver_dict[j])

for i in aver_dict:
    if i in item[1:]:
        aver_dict[i] = str(int((aver_dict[i])/(len(score_dict_list))))
print(aver_dict)
score_dict_list.append(aver_dict)
print(score_dict_list)


# In[ ]:


#计算每个学生的总分和平均分,并将其存入每个同学对应的成绩字典里
for i in score_dict_list:
    sum_person = 0
    for j in i:
        if j  in item[1:]:
            sum_person += eval(i[j])
    aver_person = '%.2f' %(sum_person/9)
    sum_person = str(sum_person)
    i['总分'] = sum_person
    i['平均分'] = aver_person
    print(i)
print(score_dict_list)


# In[ ]:


#根据总分对学生进行排名，平均成绩放在第0名
def rank_function(a):
    return eval(a['总分'])

new_score_dict_list = sorted(score_dict_list, key = rank_function,reverse=True)
print(new_score_dict_list)
for i in score_dict_list:
    if i['姓名'] == '平均':
        new_score_dict_list.insert(0,i)
print(new_score_dict_list)


# In[ ]:


#将排好的成绩按单科在60分一下替换为不及格
for i in new_score_dict_list:
    for j in i:
        try:
            if eval(i[j]) < 60:
                i[j] = '不及格'
        except:
            pass
print(new_score_dict_list)


# In[ ]:


#打印文件
new_text = []

for i in new_score_dict_list:
    if i['姓名'] != '平均':
        new_text.insert(new_score_dict_list.index(i),list(i.values()))

new_text.insert(0,list(new_score_dict_list[0].keys()))
print(new_text)

#输出到txt文件中
with open('new_report.txt','w+',encoding='utf8') as f:
    for line in new_text:
        for i in line:
                f.write(i)
                if len(i.encode('utf8'))==2:
                    f.write('      ')
                elif len(i.encode('utf8'))==3:
                    f.write('     ')
                elif len(i.encode('utf8')) in [4,5,6]:
                    f.write('    ')
                elif len(i.encode('utf8')) in [7,8,9]:
                    f.write('   ')
        f.write('\n')


# In[ ]:


#测试行
if 3 in [1,2,3]:
    print('yes')
print('数'.encode('utf8'))


# In[ ]:





# In[ ]:




