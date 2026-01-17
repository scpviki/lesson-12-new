string=input (" Enter the string ")
char=input("Enter the character you want to find")
i=0
count=0
while (i<len(string)):
    if (string[i]==char):
        count=count+1
    i=i+1
print(f"The number of times {char} occured is {count}")