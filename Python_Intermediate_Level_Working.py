#!/usr/bin/env python
# coding: utf-8

# PYTHON MEDİUM LEVEL PROBLEM SOLVING

# In[18]:


#INCOME ACCOUNT
def income(info):
    revenue = info["selling"]*info["stock"]-info["cost"]*info["stock"]
    return round(revenue)


# In[19]:


bil={"cost":32.67,"selling":45,"stock":1200}
income(bil)


# In[45]:


#UNREPEATED(a function that remove the repeater element)
def repeat(liste):
    liste2 = list()
    for i in range(len(liste)):
        if liste.count(liste[i]) == 1:
            liste2.append(liste[i])
    return liste2


# In[46]:


list1=[5,5,2,4,4,4,9,9,9,1]
repeat(list1)


# In[2]:


#WINNER(İF there is True, end up the list with 'Pong!', else end up the list with 'Ping!')
def tenis(liste,true):
    new_list = list()
    for i in range(len(liste)-1):
        new_list.append("Ping!")
        new_list.append("Pong!")
    if true == True:
        new_list.append("Ping!")
        new_list.append("Pong!")
    else:
         new_list.append("Ping!")
    return new_list


# In[4]:


ping=["ping!","ping!","ping!"]
tenis(ping,True)


# In[34]:


#Converting from binary to decimal.
def decimall(binary):
    poww = 7
    number = 0
    for i in range(len(binary)):
        number += binary[i] * 2**poww
        poww -= 1
    return number


# In[35]:


decimall([1,0,1,1,0,1,0,1])


# In[8]:


#İF there is 7 in the list, return with 'Boom!'
def evraka(liste):
    for i in liste:
        if "7" in str(i):
            return "Boom!"
    return "There's no in the list."


# In[10]:


evraka([1,3,5,5])


# In[3]:


#CHANGE TİME FORMAT(From 12 hour time format to 24 hour time format.)
def clock(time):
    if len(time)>5:
        cl,ti = time.split()
        if ti == "pm":
            c,l = cl.split(":")
            c = str(int(c)+12)
            return c+":"+l
        elif ti == "am":
            if cl == "12:00":
                return "00:00"
            return cl
    c,l = time.split(":")
    if int(c) <= 12:
        return c+":"+l+" am"
    c = str(int(c)-12)
    return c+":"+l+" pm"


# In[4]:


clock("03:17 am")


# In[48]:


#camelCase(a funtion that make first word lower and all of next words first letter is capital.)
def case(string1):
    string1 = string1.replace("_"," ")
    string = string1.split(" ")
    string[0] = string[0].lower()
    for i in range(1,len(string)):
        string[i] = string[i].title()
    return "".join(string)


# In[49]:


case("LOW high_HİGH")


# In[71]:


#HIDDEN STRING(take hidden word and its hidden letters and return the original word!)
def hidden(string,hid):
    new = ""
    string = list(string)
    hid = list(hid)
    k = 0
    for i in string:
        if i != "*":
            new += i
        else:
            new += hid[k]
            k += 1
    return new
def hidden2(string,hid):#SECOND SOLVE
    new = string.replace("*","{}")
    return new.format(*hid)


# In[73]:


print(hidden("m*rh*ba","ea"))
print(hidden2("m*rh*ba","ea"))


# In[41]:


#SUDOKU(a function that check the sudoku true or false.)
def is_sudoku(sudoku):
    summ = 0
    for i in sudoku:
        for s in i:
            if s < 1 or s > 9:
                return False
            summ += s
    return summ == 45
def is_sudoku2(sudoku):#SECOND SOLVE
    sudoku = [i for x in sudoku for i in x]
    return sorted(sudoku) == [1,2,3,4,5,6,7,8,9]


# In[43]:


print(is_sudoku([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))
print(is_sudoku2([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))


# In[11]:


#CHESS(a function that show 2 vizier can take each other or not in a chess match.)
def chess(move):
    letters = "ABCDEFGH"
    p1 = move[0] #player 1
    p2 = move[1] #player 2
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return True #if it's True it can take each other
    case1 = letters.index(p1[0]) 
    case2 = letters.index(p2[0])
    hor = abs(case1-case2)
    vert = abs(int(p1[1])-int(p2[1]))
    if hor == vert :
        return True #if it's True it can take each other
    else:
        return False #if it's False it can't take each other


# In[12]:


chess(["A1","H3"])


# In[ ]:




