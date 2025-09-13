arr=[1,1,3,5,7,7,8,9]
krr=[]
def sort(arr,i,target):
    global krr
    if(i==len(arr)):
        return krr 
    elif(arr[i]==target):
        krr.append(i)  
        return sort(arr,i+1,target)
    else:
        return sort(arr,i+1,target)               
print(sort(arr,0,1))
