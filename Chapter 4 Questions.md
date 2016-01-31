1.What is []? 
**[] is a list with no items.**

2.How would you assign the value 'hello' as the third value in a list stored  in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].) 
**spam[2] = ‘hello’**

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd']. 

3.What does spam[int('3' * 2) / 11] evaluate to? 
**33/11 = 3 = ’d’**

4.What does spam[-1] evaluate to?
**’d’ - it is the last item in the list.**

5.What does spam[:2] evaluate to? 
**[‘a’, ‘b’]**

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True]. 
	
6.What does bacon.index('cat') evaluate to? 
**1**

7.What does bacon.append(99) make the list value in bacon look like? 
**[3.14, 'cat', 11, 'cat', True, 99]**

8.What does bacon.remove('cat') make the list value in bacon look like? 
**[3.14, 'cat', 11, True,]**

9.What are the operators for list concatenation and list replication? 
**concatenation = +**
**replication = ***

10.What is the difference between the append() and insert() list methods? 
**append() adds list items to the end of a list. insert() adds them at a specified point**

11.What are two ways to remove values from a list?
**The “del” statement and “remove()” list method both work.**

12.Name a few ways that list values are similar to string values. 
**Both ca be used in for loops, can be concatenated, and can be replicated.**

13.What is the difference between lists and tuples? 
**A tuple is a list of items that is not meant to be changed. Tuples use parentheses instead of brackets.**

14.How do you type the tuple value that has just the integer value 42 in it? 
**(42,)**

15.How can you get the tuple form of a list value? How can you get the list form of a tuple value? 
**Use the tuple() and list() functions to swap them.**

16.Variables that “contain” list values don’t actually contain lists directly. What do they contain instead? 
**They contain references to list values.**

17.What is the difference between copy.copy() and copy.deepcopy()? 
**copy.copy() is used to make a duplicate copy of a mutable value like a list or dictionary, not just a  copy of a reference. copy.deepcopy() will duplicate lists contained within lists as well.**
