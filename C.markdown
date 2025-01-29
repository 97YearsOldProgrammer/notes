- **writing codes**
  - remember to end up each line with the semi-column (;)
﻿
- **building container in C **
  - give the container type first ; like char
      - char : 'character';
     - int     :  'integer';
     - double: 'decimal';
  - name the container then ; like char charcterName[]
  - variables tored [] = "something"; (without the array we could only include once character)
﻿
**how to use a container in C**
- insert a `placeholder` %(type)
  - string:     %s
  - single character: %c
  - integer:   %d
  - demical: %f
  - double(sort of demical): &lf
- *order of place holder matters*
﻿
**Math calculation in C**
- pretty much the same what we used in python as math
- btw we are not doing the calculation in the part of output, btw the place of using placeholder
﻿
**function in C**
- print function
  - *printf*
     - print out the character--"something"
     - print out the demical --"%d", 500 (require a place holder)
- math
  - pow(a,b) :  calculating a power of b
  - sqrt(a)    : calculating square root of a
  - ceil(a)     : round a up 
  - floor(a)  : round a down
﻿
**comment in C**
- /*  (comment between)  */ 
﻿
**constant in C** (unchanged container)
- const -building holder

**input function in C** (something similar like input from python)

```
double gpa;
printf("Enter your gpa:");
scanf("%lf", &gpa);
printf("Your gpa is", age);

return 0;
```
- we have to assign none variable first ( and in C we don't require to assign NOne to the variable first
- we need to use scanf function collect the variable input, and move the pointer to the variable name
  - ways to overcome this; like we want to collect both first name and last name
  - we could do this ```scanf(%s%s, variable1, variable2) ```
- different than python
  - the scanf input would only collect user input whenever it reach the first space
  - for string assign, we need ```char name[10]``` like array type and length
- when getting a character from user; we shall use `scanf(" %c") there is a space before percent notation

*fgets*
- this specifically collect line of input from the user ; used for string
- ```fgets( variable name, length, stdin);```
- difference than scanf
  -  this one would replace a new line once we call this variable out
>
**array in C** (actually different data structure from python)

- example for a list of integer(shouldn't be list?) ```int Numbers[] = {1, 2, 3, 4, 5};```
- call out certain number ```printf("%d", Numbers[0]);```
  - the indices is the same as list in python, like 0 for first item
- array could be modified ```container[x] = something; ```
- there is also one thing different than python
  - like we could assign values in arrary not in order, like if array[0] = None, we could also assign arrary[1] in C
  - C require assigning memeory for this container; like container[x]; x means the size of this arrary
- ** function in C**

- *void* () ; not returning value function 
  - void() { }

- uh, normal def in python, looks weird here
  - (return value type) container_name function_name(parameter)
  - inside the input value gonna be also container_name name_container[] array there 
  - if we wanna use the parameter, we shall also do the placeholder and , container name stuff like usually what gonna do in C
  - return is the same in python; format just in ordinary C way

- if condition
  - the boolean notation is the same >=, ==, !=, <=
  - ** if elif else structure**
  - ``` if( boolean expression){what ever u wanna do}```
  - ``` else if( boolean expression){whatever to do}: the elif is else if in C```
  - ``` else{ what ever u wanna do}```
  - **logical operatior**
  - 
  - ``` &&: means and boolean in python```
  - ``` ||: means or boolean in python```
  - ``` ! : the negation operator, basically *not* in python```
- **switch function in C** ( like function way of dictionary )

```
switch(variable){ 
case 'A':
   doing something;
   break;
case 'B':
   doing something;
   break;
default : 
   exit function
}```
- default
  - something like exit function
- case
  - like key as library in python

**struct** ( dictionary in C)
```
struct containername{
    variablename containername[];
    similar stuff;
    we could do char, int, double; here;
}; ```
- string in C
  - an array of character
  - strcpy( destination of storage, "input string");

**repetitive function in C**

- *While loop*
```
int index = 1;
while(index <= 5){
    dosomething;
    exit function ( like index = index + 1; or index++;)
}
```
- *Do while loop*
  - basically, while loop could be used as a sort of condition for function in C, not in python
```
int index = 6;
do {
    function to do;
    exit condition;
}while(index <= 5)
```