'''
Sia Ham, 1730812
Tuesday, Feburary 5
R. Vincent, instructor
Assignment - Exercise 2 (Stacks)
'''


class stack(list):
    '''A very simple stack class derived from a Python list.'''
    def isEmpty(self):
        '''return True if the stack is empty.'''
        return self == []

    def push(self, value):
        '''Add a value to the stack.'''
        self.append(value)

    def top(self):
        '''Check the top of the stack, without changing the stack.'''
        if self.isEmpty():
            raise ValueError("Stack underflow")
        return self[-1]

    def pop(self):
        '''Remove the top of the stack, returing the value found there.'''
        if self.isEmpty():
            raise ValueError("Stack underflow")
        return super().pop()
''' no matcing right parenthesis / mismatched brackets / extra right parenthesis'''


file = open (input('Please enter the name of the file for syntax check:'))
L = ['(', '[', '{'] #list of left sides of the bracket
R = [')', ']', '}'] #list of right sides of the bracket

s = stack () # define the initial stack
l = 1 #define the initial line number
for line in file:
    for c in line:
        if c in L:  #add to the stack, if c is left side of bracket
            s.push (c)
        else:
            if s != []: # condition when stack is not empty, which means if there is at least one left side of the bracket in the stack.
                if c in R: #if c is the right side of the bracket, check whether it makes pair with the left side of the bracket
                    if c == ')':
                        x = '('
                        if x == s.top(): #check whether the right side of the bracket makes pair
                            s.pop() #remove the top of the stack if brackets are matched
                        else:
                            raise ValueError ("Mismatched in the line",l)
                            
                    elif c == ']':
                        x = '['
                        if x == s.top(): #check whether the right side of the bracket makes pair
                            s.pop() #remove the top of the stack if brackets are matched
                        else:
                            raise ValueError ("Mismatched in the line",l)
                            
                    elif c == '}':
                        x = '{'
                        if x == s.top(): #check whether the right side of the bracket makes pair
                            s.pop() #remove the top of the stack if brackets are matched
                        else:
                            raise ValueError ("Mismatched in the line",l)
                            
            else:
                if c in R: #raise error when right side of the bracket is added first
                    raise ValueError ("There is at least one extra (right side of the) bracket in the line", l)
                  

    l +=1 #count line number
        
file.close()
#after removing all the paired brackets in the stack,
if s.isEmpty() == True:
    print ("No error is detected") #if stack is empty, no error has been detected
else:   
        if s.top() in L: 
            raise ValueError ("Unclosed brackets in the line", l) #if the left side of bracket is left in the stack, indicate that the there is at least one unclosed bracket
        
        elif s.top() in R:
            raise ValueError ("Extra brackets in the line", l) #if the right side of bracket is left in the stack, indicate that the there is at least one extra bracket

    

