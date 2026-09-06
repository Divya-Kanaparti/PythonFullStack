#REGULAR EXPRESSIONS
import re
#to define pattern
pattern=re.compile(r'\d')
str="hello raju i am 21 years old."
#finditer gives object to get values we use for loop
m=pattern.finditer(str)
print(m)
for i in m:
    print(i)
    print(i.start()," ",i.end()," ",i.group())
#eg:2
n=re.finditer(r'\d',"raju12rani123")
for i in m:
    print(i)
    print(i.start()," ",i.end()," ",i.group())
#eg:3
p="ababbcabb"
m=re.match(r'ab',p)
print(m.start())
print(m.end())
print(m.group())
#eg:4
m=re.match(r'c','ababbcabb')
print(m)
if m!=None:
    print("matched")
    print(m.start()," ",m.end()," ",m.group())
else:
    print("not matched")
#eg:5
#complete string mush match the pattern
m=re.fullmatch(r'ababbcabb','ababbcabb')
print(m)
if m!=None:
    print("matched")
    print(m.start()," ",m.end()," ",m.group())
else:
    print("not matched")
#eg:6
#search-matches if any where 
m=re.fullmatch(r'c','ababbcabb')
print(m)
if m!=None:
    print("matched")
    print(m.start()," ",m.end()," ",m.group())
else:
    print("not matched")
#eg:7
#split
m=re.split(r'\d','raju1ramya23harish')
print(m)
#eg:8
pattern='phoneno:+91-67935-32982'
m=re.sub(r'\d',"#",pattern)
print(m)
#eg:9
pattern='phoneno:+91-67935-32982'
m=re.subn(r'\d',"#",pattern)
print(m)
#eg:10
string="i am codegnan"
#print vowels from string
m=re.findall(r'[aeiou]',string)
print(m)
#print consonants
m=re.findall(r'[^aeiou]',string)
print(m)
#eg:11
string="i am codegnan23@gmail.com"
#print vowels from string
m=re.findall(r'\W',string)
print(m)
#eg:12
m=re.findall(r'ab{2}','a abb acc add abbb')
print(m)
#email matching
email = "divya@gmail.com"
pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
if re.match(pattern, email):
    print("Valid Gmail")
else:
    print("Invalid Gmail")