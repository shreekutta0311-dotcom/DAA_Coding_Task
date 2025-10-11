##>For Input > Search for String "the" and return its indicesString from user 

str= input("enter the string:")
search_str="enter"
index = []
i=0
while i < len(str):
    if str[i:i+len(search_str)] == search_str:
        index.append(i)
    i += 1
print("The indices of 'enter' is: ",index)

