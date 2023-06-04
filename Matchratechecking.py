string1=input("Enter the first string:")
string2=input("Enter the second string:")


special_chars = "!@#$%^&*()-_+=[]{}|\\;:'\",.<>/?`~"
numeric_chars = "0123456789"



for char in special_chars:
   string1=string1.replace(char, "")


for char in numeric_chars:
    string1=string1.replace(char, "")
    
print(string1.lower())

for char in special_chars:
    string2=string2.replace(char, "")
    
for char in numeric_chars:
    string2=string2.replace(char, "")
    
print(string2.lower())

length1=len(string1)
length2=len(string2)
total_chars=max(length1,length2)
matched_chars=0

for i in range(total_chars):
    if i<length1 and i<length2 and string1[i]==string2[i]:
        matched_chars+=1
        
match_rate=(matched_chars/total_chars) * 100     
print("Match rate:",match_rate,"%")



