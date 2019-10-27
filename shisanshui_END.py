import random
import math
import requests
import json
url='http://api.revth.com/auth/login'
data={
        "username": "zhb",
        "password": "031702534"
    }
headers={
    "Content-Type":"application/json"
}
response=requests.post(url=url,headers=headers,data=json.dumps(data),verify=False)
dicts=dict(json.loads(response.text))
token=dicts["data"]["token"]
print(dicts)
print(token)


url='http://api.revth.com/game/open'
data={
        "username": "zhb",
        "password": "031702534"
    }
headers={
    "X-Auth-Token":token
}
response=requests.post(url=url,headers=headers,data=json.dumps(data),verify=False)
dicts=dict(json.loads(response.text))
print(dicts)
get=dicts["data"]["card"]
id=dicts["data"]["id"]
print(get)
mypai=get.split(" ")
#检验2行
print("输出十三张牌")
print(mypai)
def paixu(list):
    temp=[]
    length=len(list)
    for i in range(length):
        if list[i][1] == 'A':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == 'K':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == 'Q':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == 'J':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == '1':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == '9':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == '8':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == '7':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == '6':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == '5':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == '4':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == '3':
            temp.append(list[i])
    for i in range(length):
        if list[i][1] == '2':
            temp.append(list[i])
    return temp
def heitao(mypai):
    "黑桃列表"
    heitaolist=[]
    for i in range(len(mypai)):
        if mypai[i][0]=='$':
            heitaolist.append(mypai[i])
    return heitaolist
heitaolist=heitao(mypai)
#检验2行
print("输出黑桃列表")
print(heitaolist)
def hongtao(mypai):
    "红桃列表"
    hongtaolist=[]
    for i in range(len(mypai)):
        if mypai[i][0]=='&':
            hongtaolist.append(mypai[i])
    return hongtaolist
hongtaolist=hongtao(mypai)
#检验2行
print("输出红桃列表")
print(hongtaolist)
def meihua(mypai):
    "梅花列表"
    meihualist=[]
    for i in range(len(mypai)):
        if mypai[i][0]=='*':
            meihualist.append(mypai[i])
    return meihualist
meihualist=meihua(mypai)
#检验2行
print("输出梅花列表")
print(meihualist)
def fangkuai(mypai):
    "方块列表"
    fangkuailist=[]
    for i in range(len(mypai)):
        if mypai[i][0]=='#':
            fangkuailist.append(mypai[i])
    return fangkuailist
fangkuailist=fangkuai(mypai)
#检验2行
print("输出方块列表")
print(fangkuailist)
def zhadan(mypai):
    "炸弹"
    zhadan = []
    zhadanA = []
    zhadanK = []
    zhadanQ = []
    zhadanJ = []
    zhadan10 = []
    zhadan9 = []
    zhadan8 = []
    zhadan7 = []
    zhadan6 = []
    zhadan5 = []
    zhadan4 = []
    zhadan3 = []
    zhadan2 = []
    for i in range(len(mypai)):
        if mypai[i][1]=='A':
            zhadanA.append(mypai[i])
        elif mypai[i][1]=='2':
            zhadan2.append(mypai[i])
        elif mypai[i][1]=='3':
            zhadan3.append(mypai[i])
        elif mypai[i][1]=='4':
            zhadan4.append(mypai[i])
        elif mypai[i][1]=='5':
            zhadan5.append(mypai[i])
        elif mypai[i][1]=='6':
            zhadan6.append(mypai[i])
        elif mypai[i][1]=='7':
            zhadan7.append(mypai[i])
        elif mypai[i][1]=='8':
            zhadan8.append(mypai[i])
        elif mypai[i][1]=='9':
            zhadan9.append(mypai[i])
        elif mypai[i][1]=='1':
            zhadan10.append(mypai[i])
        elif mypai[i][1]=='J':
            zhadanJ.append(mypai[i])
        elif mypai[i][1]=='Q':
            zhadanQ.append(mypai[i])
        else :
            zhadanK.append(mypai[i])
    if len(zhadanA)==4:
        zhadan.append(zhadanA)
    if len(zhadanK)==4:
        zhadan.append(zhadanK)
    if len(zhadanQ)==4:
        zhadan.append(zhadanQ)
    if len(zhadanJ)==4:
        zhadan.append(zhadanJ)
    if len(zhadan10)==4:
        zhadan.append(zhadan10)
    if len(zhadan9)==4:
        zhadan.append(zhadan9)
    if len(zhadan8)==4:
        zhadan.append(zhadan8)
    if len(zhadan7)==4:
        zhadan.append(zhadan7)
    if len(zhadan6)==4:
        zhadan.append(zhadan6)
    if len(zhadan5)==4:
        zhadan.append(zhadan5)
    if len(zhadan4)==4:
        zhadan.append(zhadan4)
    if len(zhadan3)==4:
        zhadan.append(zhadan3)
    if len(zhadan2)==4:
        zhadan.append(zhadan2)
    return zhadan
zhadan1=zhadan(mypai)
#检验2行
print("输出炸弹列表")
print(zhadan1)
def santiao(mypai):
    "三条"
    santiao = []
    santiaoA = []
    santiao2 = []
    santiao3 = []
    santiao4 = []
    santiao5 = []
    santiao6 = []
    santiao7 = []
    santiao8 = []
    santiao9 = []
    santiao10 = []
    santiaoJ = []
    santiaoQ = []
    santiaoK = []
    for i in range(len(mypai)):
        if mypai[i][1] == 'A':
            santiaoA.append(mypai[i])
        elif mypai[i][1] == '2':
            santiao2.append(mypai[i])
        elif mypai[i][1] == '3':
            santiao3.append(mypai[i])
        elif mypai[i][1] == '4':
            santiao4.append(mypai[i])
        elif mypai[i][1] == '5':
            santiao5.append(mypai[i])
        elif mypai[i][1] == '6':
            santiao6.append(mypai[i])
        elif mypai[i][1] == '7':
            santiao7.append(mypai[i])
        elif mypai[i][1] == '8':
            santiao8.append(mypai[i])
        elif mypai[i][1] == '9':
            santiao9.append(mypai[i])
        elif mypai[i][1] == '1':
            santiao10.append(mypai[i])
        elif mypai[i][1] == 'J':
            santiaoJ.append(mypai[i])
        elif mypai[i][1] == 'Q':
            santiaoQ.append(mypai[i])
        else:
            santiaoK.append(mypai[i])
    if len(santiaoA) == 3:
        santiao.append(santiaoA)
    if len(santiaoK) == 3:
        santiao.append(santiaoK)
    if len(santiaoQ)== 3:
        santiao.append(santiaoQ)
    if len(santiaoJ) == 3:
        santiao.append(santiaoJ)
    if len(santiao10) == 3:
        santiao.append(santiao10)
    if len(santiao9)== 3:
        santiao.append(santiao9)
    if len(santiao8) == 3:
        santiao.append(santiao8)
    if len(santiao7) == 3:
        santiao.append(santiao7)
    if len(santiao6) == 3:
        santiao.append(santiao6)
    if len(santiao5) == 3:
        santiao.append(santiao5)
    if len(santiao4) == 3:
        santiao.append(santiao4)
    if len(santiao3) == 3:
        santiao.append(santiao3)
    if len(santiao2) == 3:
        santiao.append(santiao2)
    return santiao
santiao1=santiao(mypai)
#检验2行
print("输出三条列表")
print(santiao1)
def duizi(mypai):
    "对子"
    santiao = []
    santiaoA = []
    santiao2 = []
    santiao3 = []
    santiao4 = []
    santiao5 = []
    santiao6 = []
    santiao7 = []
    santiao8 = []
    santiao9 = []
    santiao10 = []
    santiaoJ = []
    santiaoQ = []
    santiaoK = []
    for i in range(len(mypai)):
        if mypai[i][1] == 'A':
            santiaoA.append(mypai[i])
        elif mypai[i][1] == '2':
            santiao2.append(mypai[i])
        elif mypai[i][1] == '3':
            santiao3.append(mypai[i])
        elif mypai[i][1] == '4':
            santiao4.append(mypai[i])
        elif mypai[i][1] == '5':
            santiao5.append(mypai[i])
        elif mypai[i][1] == '6':
            santiao6.append(mypai[i])
        elif mypai[i][1] == '7':
            santiao7.append(mypai[i])
        elif mypai[i][1] == '8':
            santiao8.append(mypai[i])
        elif mypai[i][1] == '9':
            santiao9.append(mypai[i])
        elif mypai[i][1] == '1':
            santiao10.append(mypai[i])
        elif mypai[i][1] == 'J':
            santiaoJ.append(mypai[i])
        elif mypai[i][1] == 'Q':
            santiaoQ.append(mypai[i])
        else:
            santiaoK.append(mypai[i])
    if len(santiaoA) == 2:
        santiao.append(santiaoA)
    if len(santiaoK) == 2:
        santiao.append(santiaoK)
    if len(santiaoQ) == 2:
        santiao.append(santiaoQ)
    if len(santiaoJ) == 2:
        santiao.append(santiaoJ)
    if len(santiao10) == 2:
        santiao.append(santiao10)
    if len(santiao9) == 2:
        santiao.append(santiao9)
    if len(santiao8) == 2:
        santiao.append(santiao8)
    if len(santiao7) == 2:
        santiao.append(santiao7)
    if len(santiao6) == 2:
        santiao.append(santiao6)
    if len(santiao5) == 2:
        santiao.append(santiao5)
    if len(santiao4) == 2:
        santiao.append(santiao4)
    if len(santiao3) == 2:
        santiao.append(santiao3)
    if len(santiao2) == 2:
        santiao.append(santiao2)
    return santiao
duizi1 = duizi(mypai)
# 检验2行
print("输出对子列表")
print(duizi1)
def delectpai(mypai,list):
    index=[]
    mypailongth=len(mypai)
    listlongth=len(list)
    for i in range(mypailongth):
        for j in range(listlongth):
            if(mypai[i]==list[j]):
                index.append(mypai[i])
    indexlength=len(index)
    for k in range(indexlength):
        a=index[k]
        mypai.remove(a)
    return mypai
def lianxu(list):
    lianxulist=[]
    numA = []
    num2 = []
    num3 = []
    num4 = []
    num5 = []
    num6 = []
    num7 = []
    num8 = []
    num9 = []
    num10 = []
    numJ = []
    numQ = []
    numK = []
    for i in range(len(list)):
        if list[i][1]=='A':
            numA.append(list[i])
        if list[i][1]=='K':
            numK.append(list[i])
        if list[i][1]=='Q':
            numQ.append(list[i])
        if list[i][1]=='J':
            numJ.append(list[i])
        if list[i][1]=='1':
            num10.append(list[i])
        if list[i][1]=='9':
            num9.append(list[i])
        if list[i][1]=='8':
            num8.append(list[i])
        if list[i][1]=='7':
            num7.append(list[i])
        if list[i][1]=='6':
            num6.append(list[i])
        if list[i][1]=='5':
            num5.append(list[i])
        if list[i][1]=='4':
            num4.append(list[i])
        if list[i][1]=='3':
            num3.append(list[i])
        if list[i][1]=='2':
            num2.append(list[i])
    if len(numA)!=0 and len(numK)!=0 and len(numQ)!=0 and len(numJ)!=0 and len(num10)!=0:
        lianxulist.append(numA[0])
        lianxulist.append(numK[0])
        lianxulist.append(numQ[0])
        lianxulist.append(numJ[0])
        lianxulist.append(num10[0])
        return lianxulist
    elif len(numK)!=0 and len(numQ)!=0 and len(numJ)!=0 and len(num10)!=0 and len(num9)!=0:
        lianxulist.append(numK[0])
        lianxulist.append(numQ[0])
        lianxulist.append(numJ[0])
        lianxulist.append(num10[0])
        lianxulist.append(num9[0])
        return lianxulist
    elif len(numQ)!=0 and len(numJ)!=0 and len(num10)!=0 and len(num9)!=0 and len(num8)!=0:
        lianxulist.append(numQ[0])
        lianxulist.append(numJ[0])
        lianxulist.append(num10[0])
        lianxulist.append(num9[0])
        lianxulist.append(num8[0])
        return lianxulist
    elif len(numJ)!=0 and len(num10)!=0 and len(num9)!=0 and len(num8)!=0 and len(num7)!=0:
        lianxulist.append(numJ[0])
        lianxulist.append(num10[0])
        lianxulist.append(num9[0])
        lianxulist.append(num8[0])
        lianxulist.append(num7[0])
        return lianxulist
    elif len(num10)!=0 and len(num9)!=0 and len(num8)!=0 and len(num7)!=0 and len(num6)!=0:
        lianxulist.append(num10[0])
        lianxulist.append(num9[0])
        lianxulist.append(num8[0])
        lianxulist.append(num7[0])
        lianxulist.append(num6[0])
        return lianxulist
    elif len(num9)!=0 and len(num8)!=0 and len(num7)!=0 and len(num6)!=0 and len(num5)!=0:
        lianxulist.append(num9[0])
        lianxulist.append(num8[0])
        lianxulist.append(num7[0])
        lianxulist.append(num6[0])
        lianxulist.append(num5[0])
        return lianxulist
    elif len(num8)!=0 and len(num7)!=0 and len(num6)!=0 and len(num5)!=0 and len(num4)!=0:
        lianxulist.append(num8[0])
        lianxulist.append(num7[0])
        lianxulist.append(num6[0])
        lianxulist.append(num5[0])
        lianxulist.append(num4[0])
        return lianxulist
    elif len(num7)!=0 and len(num6)!=0 and len(num5)!=0 and len(num4)!=0 and len(num3)!=0:
        lianxulist.append(num7[0])
        lianxulist.append(num6[0])
        lianxulist.append(num5[0])
        lianxulist.append(num4[0])
        lianxulist.append(num3[0])
        return lianxulist
    elif len(num6)!=0 and len(num5)!=0 and len(num4)!=0 and len(num3)!=0 and len(num2)!=0:
        lianxulist.append(num6[0])
        lianxulist.append(num5[0])
        lianxulist.append(num4[0])
        lianxulist.append(num3[0])
        lianxulist.append(num2[0])
        return lianxulist
    else:
        return lianxulist
#jinayan
print("连续")
print(lianxu(mypai))
dunlist=[]
def huase5(list1,list2,list3,list4):
    list =[]
    if len(list1)>=5:
        list.append(list1)
    if len(list2)>=5:
        list.append(list2)
    if len(list3)>=5:
        list.append(list3)
    if len(list4)>=5:
        list.append(list4)
    return list
#检验2行
print("花色大于5的列表")
print(huase5(heitaolist,hongtaolist,meihualist,fangkuailist))
huase=huase5(heitaolist,hongtaolist,meihualist,fangkuailist)
#同花顺的个数
if len(huase)==2:
    if len(lianxu(huase[0]))==5 and len(lianxu(huase[1]))==5:
        dunlist.append(lianxu(huase[0]))
        dunlist.append(lianxu(huase[1]))
        mypai=delectpai(mypai,lianxu(huase[0]))
        mypai=delectpai(mypai,lianxu(huase[1]))
    elif len(lianxu(huase[0]))==5 and len(lianxu(huase[1]))==0:
        dunlist.append(lianxu(huase[0]))
        mypai=delectpai(mypai,lianxu(huase[0]))
    elif len(lianxu(huase[0])) == 0 and len(lianxu(huase[1])) == 5:
        dunlist.append(lianxu(huase[1]))
        mypai=delectpai(mypai, lianxu(huase[1]))
    else:
        pass
elif len(huase)==1:
    if len(lianxu(huase[0]))==5:
        dunlist.append(lianxu(huase[0]))
        mypai = delectpai(mypai, lianxu(huase[0]))
print("同花顺")
print(dunlist)
#炸弹
zhadan=zhadan(mypai)
zhadanlength=len(zhadan)
if zhadanlength==0:
    pass
elif zhadanlength==1:
    dunlist.append(zhadan[0])
    mypai=delectpai(mypai, zhadan[0])
else:
    dunlist.append(zhadan[0])
    dunlist.append(zhadan[1])
    mypai = delectpai(mypai, zhadan[0])
    mypai = delectpai(mypai, zhadan[1])
print("炸弹")
print(dunlist)
#葫芦
santiaolength=len(santiao(mypai))
duizilength=len(duizi(mypai))
if santiaolength>=2:
    if duizilength>=2:
        a=[santiao(mypai)[0][0],santiao(mypai)[0][1],santiao(mypai)[0][2],duizi(mypai)[duizilength-1][0],duizi(mypai)[duizilength-1][1]]
        dunlist.append(a)
        b=[santiao(mypai)[1][0],santiao(mypai)[1][1],santiao(mypai)[1][2],duizi(mypai)[duizilength-2][0],duizi(mypai)[duizilength-2][1]]
        dunlist.append(b)
        mypai=delectpai(mypai,a)
        mypai=delectpai(mypai,b)
    elif duizilength==1:
        a = [santiao(mypai)[0][0], santiao(mypai)[0][1], santiao(mypai)[0][2], duizi(mypai)[duizilength - 1][0], duizi(mypai)[duizilength - 1][1]]
        dunlist.append(a)
        mypai = delectpai(mypai,a)
    else:
        pass
elif santiaolength == 1:
    if duizilength >= 1:
        a = [santiao(mypai)[0][0], santiao(mypai)[0][1], santiao(mypai)[0][2], duizi(mypai)[duizilength - 1][0], duizi(mypai)[duizilength - 1][1]]
        dunlist.append(a)
        mypai = delectpai(mypai, a)
    else:
        pass
else:
    pass
print("葫芦")
print(dunlist)
#同花
mypai=paixu(mypai)
heitaolength=len(heitao(mypai))
hongtaolength=len(hongtao(mypai))
meihualength=len(meihua(mypai))
fangkuailength=len(fangkuai(mypai))
if heitaolength>=5:
    a=[heitao(mypai)[0],heitao(mypai)[1],heitao(mypai)[2],heitao(mypai)[3],heitao(mypai)[4]]
    dunlist.append(a)
    mypai = delectpai(mypai,a)
if hongtaolength>=5:
    a=[hongtao(mypai)[0],hongtao(mypai)[1],hongtao(mypai)[2],hongtao(mypai)[3],hongtao(mypai)[4]]
    dunlist.append(a)
    mypai = delectpai(mypai,a)
if meihualength>=5:
    a=[meihua(mypai)[0],meihua(mypai)[1],meihua(mypai)[2],meihua(mypai)[3],meihua(mypai)[4]]
    dunlist.append(a)
    mypai = delectpai(mypai,a)
if fangkuailength>=5:
    a=[fangkuai(mypai)[0],fangkuai(mypai)[1],fangkuai(mypai)[2],fangkuai(mypai)[3],fangkuai(mypai)[4]]
    dunlist.append(a)
    mypai = delectpai(mypai,a)
print("同花")
print(dunlist)
#三条
santiaolength=len(santiao(mypai))
if santiaolength>=3:
    a=[santiao(mypai[0][0]),santiao(mypai[0][1]),santiao(mypai[0][2]),santiao(mypai[santiaolength-1][0]),santiao(mypai[santiaolength-1][1])]
    b=santiao(mypai)[1]
    dunlist.append(a)
    dunlist.append(b)
    mypai=delectpai(mypai,a)
    mypai=delectpai(mypai,b)
elif santiaolength==2:
    a = santiao(mypai)[0]
    b = santiao(mypai)[1]
    dunlist.append(a)
    dunlist.append(b)
    mypai = delectpai(mypai, a)
    mypai = delectpai(mypai, b)
elif santiaolength==1:
    a = santiao(mypai)[0]
    dunlist.append(a)
    mypai = delectpai(mypai, a)
else:
    pass
print("三条")
print(dunlist)
print(duizi(mypai))
#两对
duizilength=len(duizi(mypai))
print(duizilength)
if duizilength==5:
    a=[duizi(mypai)[0][0],duizi(mypai)[0][1],duizi(mypai)[3][0],duizi(mypai)[3][1]]
    b=[duizi(mypai)[1][0],duizi(mypai)[1][1],duizi(mypai)[4][0],duizi(mypai)[4][1]]
    c=[duizi(mypai)[2][0],duizi(mypai)[2][1]]
    dunlist.append(a)
    dunlist.append(b)
    dunlist.append(c)
    mypai = delectpai(mypai, a)
    mypai = delectpai(mypai, b)
    mypai = delectpai(mypai, c)
elif duizilength==4:
    a=[duizi(mypai)[0][0],duizi(mypai)[0][1],duizi(mypai)[3][0],duizi(mypai)[3][1]]
    b=[duizi(mypai)[1][0],duizi(mypai)[1][1]]
    c=[duizi(mypai)[2][0],duizi(mypai)[2][1]]
    dunlist.append(a)
    dunlist.append(b)
    dunlist.append(c)
    mypai = delectpai(mypai, a)
    mypai = delectpai(mypai, b)
    mypai = delectpai(mypai, c)
elif duizilength==3:
    a=[duizi(mypai)[0][0],duizi(mypai)[0][1]]
    b=[duizi(mypai)[1][0],duizi(mypai)[1][1]]
    c=[duizi(mypai)[2][0],duizi(mypai)[2][1]]
    dunlist.append(a)
    dunlist.append(b)
    dunlist.append(c)
    mypai = delectpai(mypai, a)
    mypai = delectpai(mypai, b)
    mypai = delectpai(mypai, c)
elif duizilength==2:
    a=[duizi(mypai)[0][0],duizi(mypai)[0][1]]
    b=[duizi(mypai)[1][0],duizi(mypai)[1][1]]
    dunlist.append(a)
    dunlist.append(b)
    mypai = delectpai(mypai, a)
    mypai = delectpai(mypai, b)
elif duizilength==1:
    a=[duizi(mypai)[0][0],duizi(mypai)[0][1]]
    dunlist.append(a)
    mypai = delectpai(mypai, a)
print("对子")
print(dunlist)
print(duizi(mypai))
#补齐
mypai=paixu(mypai)
dunlistlength=len(dunlist)
print("cd")
print(dunlistlength)
if dunlistlength==3:
    if len(dunlist[2])<3:
        length=3-len(dunlist[2])
        for i in range(length):
            a=[mypai[0]]
            dunlist[2].append(mypai[0])
            mypai=delectpai(mypai,a)
    else:
        pass
    if len(dunlist[1])<5:
        length=5-len(dunlist[1])
        for i in range(length):
            a = [mypai[0]]
            dunlist[1].append(mypai[0])
            mypai = delectpai(mypai, a)
    else:
        pass
    if len(dunlist[0])<5:
        length=5-len(dunlist[0])
        for i in range(length):
            a = [mypai[0]]
            dunlist[0].append(mypai[0])
            mypai = delectpai(mypai, a)
    else:
        pass
if dunlistlength==2:
    a=[mypai[0]]
    dunlist.append(a)
    mypai = delectpai(mypai, a)
    if len(dunlist[2])<3:
        length=3-len(dunlist[2])
        for i in range(length):
            a=[mypai[0]]
            dunlist[2].append(mypai[0])
            mypai=delectpai(mypai,a)
    else:
        pass
    if len(dunlist[1])<5:
        length=5-len(dunlist[1])
        for i in range(length):
            a = [mypai[0]]
            dunlist[1].append(mypai[0])
            mypai = delectpai(mypai, a)
    else:
        pass
    if len(dunlist[0])<5:
        length=5-len(dunlist[0])
        for i in range(length):
            a = [mypai[0]]
            dunlist[0].append(mypai[0])
            mypai = delectpai(mypai, a)
    else:
        pass
if dunlistlength==1:
    a=[mypai[0]]
    dunlist.append(a)
    mypai = delectpai(mypai, a)
    a = [mypai[0]]
    dunlist.append(a)
    mypai = delectpai(mypai, a)
    if len(dunlist[2])<3:
        length=3-len(dunlist[2])
        for i in range(length):
            a=[mypai[0]]
            dunlist[2].append(mypai[0])
            mypai=delectpai(mypai,a)
    else:
        pass
    if len(dunlist[1])<5:
        length=5-len(dunlist[1])
        for i in range(length):
            a = [mypai[0]]
            dunlist[1].append(mypai[0])
            mypai = delectpai(mypai, a)
    else:
        pass
    if len(dunlist[0])<5:
        length=5-len(dunlist[0])
        for i in range(length):
            a = [mypai[0]]
            dunlist[0].append(mypai[0])
            mypai = delectpai(mypai, a)
    else:
        pass
if dunlistlength==0:
    a=[mypai[0]]
    dunlist.append(a)
    mypai = delectpai(mypai, a)
    a = [mypai[0]]
    dunlist.append(a)
    mypai = delectpai(mypai, a)
    a = [mypai[0]]
    dunlist.append(a)
    mypai = delectpai(mypai, a)
    if len(dunlist[2])<3:
        length=3-len(dunlist[2])
        for i in range(length):
            a=[mypai[0]]
            dunlist[2].append(mypai[0])
            mypai=delectpai(mypai,a)
    else:
        pass
    if len(dunlist[1])<5:
        length=5-len(dunlist[1])
        for i in range(length):
            a = [mypai[0]]
            dunlist[1].append(mypai[0])
            mypai = delectpai(mypai, a)
    else:
        pass
    if len(dunlist[0])<5:
        length=5-len(dunlist[0])
        for i in range(length):
            a = [mypai[0]]
            dunlist[0].append(mypai[0])
            mypai = delectpai(mypai, a)
    else:
        pass
print(dunlist)
datalist=[]
temp=dunlist[2][0]+" "+dunlist[2][1]+" "+dunlist[2][2]
datalist.append(temp)
temp=dunlist[1][0]+" "+dunlist[1][1]+" "+dunlist[1][2]+" "+dunlist[1][3]+" "+dunlist[1][4]
datalist.append(temp)
temp=dunlist[0][0]+" "+dunlist[0][1]+" "+dunlist[0][2]+" "+dunlist[0][3]+" "+dunlist[0][4]
datalist.append(temp)



url='http://api.revth.com/game/submit'

data={
  "id": id,
  "card": datalist
}
headers={
    "X-Auth-Token":token,
    "Content-Type":"application/json"
}
response=requests.post(url=url,headers=headers,data=json.dumps(data),verify=False)






dicts=dict(json.loads(response.text))
print(dicts)









