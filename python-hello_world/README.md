# Python - Hello, World

## Text Sequence Type — str

> Textual data in Python is handled with **`str`** objects, or strings. Strings are immutable sequences of Unicode code points. 

This means:
- Every piece of text in Python is an instance of the `str` class.
- Once you create a string, you cannot change it directly.
- A code point is a particular position in a table, where the position has been assigned a meaning.


https://docs.python.org/3.13/library/stdtypes.html#string-methods
### Regular methods
1. capitalize
1. casefold
1. center
1. count
1. encode
1. endswith
1. expandtabs
1. find
1. format
1. format_map
1. index
1. isalnum
1. isalpha
1. isascii
1. isdecimal
1. isdigit
1. isidentifier
1. islower
1. isnumeric
1. isprintable
1. isspace
1. istitle
1. isupper
1. join
1. ljust
1. lower
1. lstrip
1. maketrans
1. partition
1. removeprefix
1. removesuffix
1. replace
1. rfind
1. rindex
1. rjust
1. rpartition
1. rsplit
1. rstrip
1. split
1. splitlines
1. startswith
1. strip
1. swapcase
1. title
1. translate
1. upper
1. zfill



### Dunder methods
1. \_\_len__
    ```python
        s = str('Measure this!').__len__()
    ```
    Provide syntactic sugar for this
    ```python
        s = len('Measure this!')
    ```

1. \_\_add__
    ```python
        s = str().__add__('String').__add__(' ').__add__('concatenation')
    ```
    Provide syntactic sugar for this
    ```python
        s = 'String' + ' ' + 'concatenation'
    ```

1. \_\_mul__
    ```python
        s = str().__add__('Repeat ').__mul__(2).__mul__(3)
    ```
    Provide syntactic sugar for this
    ```python
        s = 'Repeat ' * 2 * 3
    ```

1. \_\_rmul__
    ```python
        s = str().__add__('Repeat ').__mul__(2).__mul__(3)
    ```
    Provide syntactic sugar for this
    ```python
        s = 'Repeat ' * 2 * 3
    ```

1. \_\_mod__
    ```python
        s = str().__add__('%s %s, %s').__mod__(('Hi', 'there', 'silly'))
    ```
    Provide syntactic sugar for this
    ```python
        s = '%s %s, %s' % ('Hi', 'there', 'silly')
    ```

1. \_\_dir__


1. \_\_class__
1. \_\_contains__
1. \_\_delattr__
1. \_\_doc__
1. \_\_eq__
1. \_\_format__
1. \_\_ge__
1. \_\_getattribute__
1. \_\_getitem__
1. \_\_getnewargs__
1. \_\_getstate__
1. \_\_gt__
1. \_\_hash__
1. \_\_init__
1. \_\_init_subclass__
1. \_\_iter__
1. \_\_le__
1. \_\_lt__
1. \_\_ne__
1. \_\_new__
1. \_\_reduce__
1. \_\_reduce_ex__
1. \_\_repr__
1. \_\_setattr__
1. \_\_sizeof__
1. \_\_str__

1. \_\_subclasshook__
    ```
        NotImplemented
    ```

1. \_\_rmod__
    ```
        NotImplemented
    ```