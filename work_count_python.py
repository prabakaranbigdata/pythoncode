f=open("C:\\Users\\Nova15\\Desktop\\sandbox","r")
if f.mode == 'r':
    contents =f.read()    
print(contents)
contents_split = contents.split()
print(contents_split)
varia_dict={}
caunt_var = 0
for elements in contents_split:
    temp=varia_temp.get(elements)
    if(temp is None):
       varia_dict[elements]=1
    else:
        temp=int(temp)
        temp+=1
        varia_dict[elements]=temp
print(varia_temp)