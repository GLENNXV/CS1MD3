# Q1a

def q1a(): return "a"

# Q1b

def q1b(): return "b"

# Q2 

if a == b:
    d = 1
else
    d = f(a, b)

# Q3a

# ['Alice', 'Bob', 'Eve']

# Q3b

# Dictionaries are mutable and indexed with arbitrary literals, tuples are immutable and indexed with integers.

# Q4a

# x is local to the function and does not exist in the context of the print statement

# Q4b

# l is mutable.  b is a pointer to l, not a new, distinct copy of it.  

# Q5 

# There's no base case so it will never terminate.

# Q6 

def q6(): return "d"

# Q7a

def q7a(): return "d"

# Q7b

def q7b(): return "c"

# Q8 

def q8(): return "b"

# Q9

def q9(): return "d"

# Q10

q10_answer = "%B %d, %Y" # Replace with your answer

import datetime
today = datetime.datetime(2018, 4, 21)
print(today.strftime(q10_answer))

# Q13a

def decode1(c, x):
    
    s = ''
    
    for i, k in enumerate(c):
        if i % x == 0: s+= k
            
    return s

# Q13b

def decode2(c, xs):
    s = ''
    for i in range(len(c)): 
        for x in xs: 
            if i % x == 0: s += c[i]; break 
    return s
# Q14 

def gradelist(d, f):
    
    for k in d:
        
        d[k] = f(d[k])
        
    return d

# Q15

class Student:
    
    
    def __init__(self, n):
        
        self.number = n
        self.grades = dict()
        
    def addCourse(self, c, g):
        
        if c in self.grades and self.grades[c] > g:
            pass
        else:
            self.grades[c] = g
            
    def getGrade(self, c):
        
        return self.grades[c]
    
    def canTake(self, c, l):
        
        if c in self.grades: 
            raise Warning
            
        allowed = True
        for k in l:
            if k in self.grades and self.grades[k] < 50:
                allowed = False
            elif k not in self.grades:
                allowed = False
                
        return allowed

def popular_course(l, c):
    
    return [k for k in l if c in k.grades]

# Q16a
        
import csv

dates = []
arrests = []

with open('drug_arrests.csv', 'r') as fh:
    
    rd = csv.DictReader(fh)
    
    for row in rd:
        dates.append(int(row['year']))
        arrests.append(int(row['arrests']))

# Q16c
# This topic was never covered, incidentally.

import matplotlib.pyplot as plt
%matplotlib inline

plt.scatter(dates, arrests)
plt.show()
plt.scatter(dates, cars)
plt.show()
plt.scatter(cars, arrests)
plt.show()




