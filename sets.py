#sets
#declaration of sets

s1={"hello","regh","wallo"}

#add elements(emplace in c++)
s1.add("new_;xijc")
print(s1)

s2={"tupo","poo","uio"}

#update or analogous to s1=s1+s2 compared to strings in Python
s1.update(s2);
print(s1)

#clearinng one 
se={"fw","jk","gr"}
se.clear()
print(se,"empty se")

#intersection()->Return a set that contains the items that exist in both set
inter=s1.intersection(s2)
print("intersection->",inter)

#pop() method for removing elements in set
num={1,3,4,5,7,9}
num.pop()
print("after poping 9->",num)

#union dos same kind of operation of update
#but returns new set
s3=s1.union(s2);
print(s3)

#output
#{'wallo', 'regh', 'hello', 'new_;xijc'}
#{'tupo', 'uio', 'regh', 'wallo', 'new_;xijc', 'poo', 'hello'}
#set() empty se
#intersection-> {'poo', 'tupo', 'uio'}
#after poping 9-> {3, 4, 5, 7, 9}
#{'uio', 'poo', 'tupo', 'regh', 'wallo', 'new_;xijc', 'hello'}
