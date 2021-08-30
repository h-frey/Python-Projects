
def addTwoNumbers(l1,l2):
        l1.reverse()
        l2.reverse()
        num="".join(str(x) for x in l1)
        num1="".join(str(y) for y in l2)
        sum_=int(num)+int(num1)
        sum_list=[int(i) for i in str(sum_)]
        sum_list.reverse()
        return(sum_list)
        
print(addTwoNumbers([2,4,3],[5,6,4]))
list1 = [9,9,9,9,9,9,9], list2 = [9,9,9,9]
print(addTwoNumbers(list1,list2))