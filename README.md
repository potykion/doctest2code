# doctest2code

Converts doctest to code • https://doctest2code.herokuapp.com

Sample input:

```python
>>> sum_ = 0
>>> for number in range(5):
...   sum_ += number
>>> sum_
10
```

Sample output:

```python
sum_ = 0
for number in range(5):
  sum_ += number
assert sum_ == 10
```