from enum import Enum
class 關係(Enum):
    泄=0
    幫=1
    生=2
    克=3
    耗=4






class 五行(Enum):
    木=0
    火=1
    土=2
    金=3
    水=4
    def calc(self,other):
        num=abs(self.value-other.value)
        num= num if num <3 else 5-num
        print(num)
        if num==1 :
            return '生'
        elif num==2:
            return '克'
    def 關係(self,other):
        if self is other:
            return 關係.幫
        elif (self.value+1)%5==other.value:
            return 關係.生
        elif (self.value+2)%5==other.value:
            return 關係.克
        elif (self.value-1)%5==other.value:
            return 關係.泄
        else:
            return 關係.耗
if __name__=='__main__':
    for item in 五行:
        for item_1 in 五行:
            result=item.關係(item_1)
            print(item,result,item_1)

