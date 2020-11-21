string=input()
new_string=""
count=0
for i in string:
    if i not in new_string:
        count+=1
        new_string+=i
    else:
        continue
print(count)
