# Data Validation

## Pattern 1

For syntax validation when checking input.

```python
isinstance(val, type)
```

```python
flagName = False
while not flagName:
    if [Do check here]:
        flagName = True
    else:
        print('error message')
```
