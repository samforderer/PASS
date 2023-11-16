# Lists 
- lists contain multiple elements
- lists are an iterable structure

*The following will print the list of names*
```python
names = ["Sam", "John", "Jesse"]
for i in names:
    print(i)
```

## Indexing List 
- access elements by using index `list[0]`
- negative index to access from end of list
    - `list[-1]` will return last item

## `In` Operator
- use to search for elements in list 
- `if "John" in names:`

## Built-in Functions 
- `len(), max(), min(), sum(), sorted()`
- `list.append(), list.pop(), list.insert(1, "element")`

## Slicing 
- returns a portion of list using `list[:3]`
- does not effect original list 

## List of Lists
- a nested list
- `locations = [['Hamilton', 'Ontario'], ['Vancouver', 'Britis Colombia']]`
- accessed with `location[0][1]`

Textbook exercices page 145-147 #1, 3, 4, 6, 10, page 168 #1-4

# Strings 
- index or negative index `str[4]`
- slice `str[1:]` (start inclusive, stop exclusive)
- loop through string using `in`
- search within string with `in`
- `a.isalpha(), a.isdigit(), a.swapcase(), a.strip()`

# Data Validation
## **Data Type**
- `if s.isdecimal(): do thing`
- check notes for more 

## **Correct Form**
- use slicing

## **range**
- `and` operator is best for checking if value is inside a range of numbers 

    - `if(x >= 20 and x <=40)`
    - `20 <= x <= 40`

- `or` is best checking outside of range

    - `if(x < 20 or x > 40)`

## Data Validation Exercise 
1. write module to validate password. Requires at least:
- one uppercase
- one lowercase 
- one digit 
- no spaces or special characters 
- at least length of 10 

