# Control Flow

### If condition

Syntax:

```
if <condition>:
    <statements>
elif <condition>:
    <statements>
else:
    <statements>
```

For example:

```
age = 15

if age <= 3:
    print('Hello baby!')
elif age < 13:
    print('You are a kid')
elif age < 18:
    print('You are in the teens')
else:
    print('You are an adult or old')

```

In python, every object has a truth value:

Any object can be tested for a truth value in an if or
while condition or as operands of Boolean operations.
The following values are considered to be False:
- `None`
- `False`
- Zero of any numeric type, such as 0, 0.0, 0j
- Any empty sequence like, (), [], '', ""
- Any empty mapping like, {}
- If user-defined classes are assigned to bool or len
functions, then it returns the value of 0, or False.

All other values are considered to be True. Which means that 
objects that can be classified into more than one type,
are considered to be True.