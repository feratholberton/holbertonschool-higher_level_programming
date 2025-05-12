# Python - Hello, World

## Text Sequence Type — str

> Textual data in Python is handled with **`str`** objects, or strings. Strings are immutable sequences of Unicode code points. 

This means:
- Every piece of text in Python is an instance of the `str` class.
- Once you create a string, you cannot change it directly.
- A code point is a particular position in a table, where the position has been assigned a meaning.

[Python String Methods](https://docs.python.org/3.13/library/stdtypes.html#string-methods)

### Regular methods
1. upper
    > Return a copy of the string with all the cased characters converted to uppercase.

1. lower
    > Return a copy of the string with all the cased characters converted to lowercase.

1. capitalize
    > Return a copy of the string with its first character capitalized and the rest lowercased.

1. title
    > Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

1. casefold
    > Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.

1. swapcase
    > Return a copy of the string with uppercase characters converted to lowercase and vice versa. 

1. strip
1. lstrip
1. rstrip
1. removeprefix
1. removesuffix

1. center
1. ljust
1. rjust

1. count
    > Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
    >
    >If sub is empty, returns the number of empty strings between characters which is the length of the string plus one.

1. find
    > Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

1. index
    > Like find(), but raise ValueError when the substring is not found.

1. rfind
    > Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.

1. rindex
    > Like rfind() but raises ValueError when the substring sub is not found.

1. join
    > Return a string which is the concatenation of the strings in iterable. A TypeError will be raised if there are any non-string values in iterable, including bytes objects. The separator between elements is the string providing this method.

1. format
1. replace
1. expandtabs
1. format_map

1. partition
1. rpartition
1. split
1. rsplit
1. splitlines
1. zfill
1. maketrans
1. translate

1. startswith
1. endswith
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

1. encode

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