TASK-1:
we start with try and except to handle the file not found error

inside it, we open file in read mode, read all the lines and store them in variable 'a' as a list
and create a for loop, and a variable s to keep record of the line 
if else keeps checking for the last line
if it is the last line, there will be no '\n' or line change so we print the whole thing
which was not the case if 'if' statements where we were excluding the last character ('\n')


TASK-2:
we open the file, ask for input, write it with a +'\n' to that it changes the line in the text file
same with the other part
we close the file and then reopen in read mode, iterate through all the lines and print it
