my_string= 'Hello world'
print(my_string)
#Index to the character in []
char = my_string[0]
print(char)
substring=my_string[1:5]
print(substring)
#substring=my_string[::-1] reverse the string
# concatenate
greeting='Hello'
name='Tom'
sentence= greeting + " " + name
print(sentence)
for i in greeting:
    print(i)
#string with whitespaces
Greet = '  Hello Person  ' 
print(Greet)   
Greet = Greet.strip()
print(Greet)
print(Greet.upper())
if 'g' in Greet:
    print('Yes')
else:
    print('No')
print("Hello".startswith("He"))  
print("Hello".endswith("llo"))
print("Hello".count("o"))
print("Hello".find("e"))
message= "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)
my_greeting ="how are you doing"
y=my_greeting.split()
print(y)
my="one, two, Three"
d=my.split(",")
print(my)
my_list=['how', 'are', 'you', 'doing']
new_sent = ' '.join(my_list)
new_sent1=''.join(my_list)
print(new_sent)
print(new_sent1)
var=3
myVar='Tom'
mePi = 3.1436543
#tomstring= 'The variable is %s' % myVar
#print(tomstring)
#mynum='The number is %d' % var
#print(mynum)
#me_pi= 'The variable is %f' % mePi
#print(me_pi)
#me_pi ='The Vatiable is %.2f' % mePi
#print(me_pi)
# new method to format
#tomstring='The variable are {} and {} and {:.2f}'.format(myVar, var, mePi)
tomstring=f"The variable are {var} and {myVar} and {mePi}"
print(tomstring)
   
