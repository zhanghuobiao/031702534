#-*-coding:utf-8-*-
import re
while 1:
    str=input()
    if str=='END':
       break
tel=re.search("\d{11}",str).group()
#print(tel)
str=re.sub("\d{11}","",str)
#print(str) delete telephone
str=re.sub(".\!","",str)
name=re.search(".+\,",str).group()
name=re.sub(",","",name)
#print(name)
str=re.sub(".+\,","",str)
#print(str) delete name
s1=re.search(".+省",str).group()
#print(s1)
str=re.sub(".+省","",str)
s2=re.search(".+市",str).group()
str=re.sub(".+市","",str)
#print(s2)
s3=re.search(".+[区县]",str).group()
str=re.sub(".+[区县]","",str)
#print(s3)
s4=re.search(".+[道镇乡]",str).group()
str=re.sub(".+[道镇乡]","",str)
#print(s4)
s5=re.search(".+\.",str).group()
str=re.sub(".+\.","",str)
s5=re.sub("\.","",s5)
#print(s5)
print("[{\"姓名\":\""+name+"\",\""+tel+"\",\"地址\":[\""+s1+"\",\""+s2+"\",\""+s3+"\",\""+s4+"\",\""+s5+"\"]}")

