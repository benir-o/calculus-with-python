# 1. Limits in Python
In this series, we examine the behaviour of a graph in relation to an increase or decrease in the input of our function.

The following equation cannot allow for x to take 2, as our function becomes undefined.

## Equation
## $y= \frac {3(x-2)} {x-2}$
<br> The equation can be used to examine the behaviour of the graph as x approaches 2. 
We can also model this with python code as follows.

```python
x=2
h= 0.00001
y_right= (3*((x+h)-2)/((x+h) -2))
y_left=(3*((x-h)-2))/((x-h)-2)

print("y_right: ",y_right)
print("y_left: ",y_left)

if round(y_right) != round(y_left):
    print("Limit does not exist at x=",x)
```

