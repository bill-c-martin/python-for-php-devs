
[learning python](https://www.learnpython.org/)

- [Install Python and friends](#install-python-and-friends)
  - [Boot Up Virtual Environment](#boot-up-virtual-environment)
- [Python for PHP Developers](#python-for-php-developers)
  - [Hello World](#hello-world)
    - [PHP](#php)
    - [Python](#python)
  - [Indentation](#indentation)
    - [PHP](#php-1)
    - [Python](#python-1)
  - [Numbers](#numbers)
    - [PHP](#php-2)
    - [Python](#python-2)
  - [Strings](#strings)
    - [PHP](#php-3)
    - [Python](#python-3)
  - [Lists](#lists)
    - [PHP](#php-4)
    - [Python](#python-4)
  - [String Formatting](#string-formatting)
    - [PHP](#php-5)
    - [Python](#python-5)
  - [String Operations](#string-operations)
    - [PHP](#php-6)
    - [Python](#python-6)
  - [Assignments](#assignments)
    - [PHP](#php-7)
    - [Python](#python-7)
  - [Arithmetic](#arithmetic)
    - [PHP](#php-8)
    - [Python](#python-8)
  - [Concatenation](#concatenation)
    - [PHP](#php-9)
    - [Python](#python-9)
  - [Type Checking](#type-checking)
    - [PHP](#php-10)
    - [Python](#python-10)
  - [Conditions](#conditions)
    - [PHP](#php-11)
    - [Python](#python-11)
  - [Loops](#loops)
    - [PHP](#php-12)
    - [Python](#python-12)
  - [Functions](#functions)
    - [PHP](#php-13)
    - [Python](#python-13)
  - [Classes](#classes)
    - [PHP](#php-14)
    - [Python](#python-14)
  - [Dictionaries](#dictionaries)
    - [PHP](#php-15)
    - [Python](#python-15)

## Install Python and friends

```bash
sudo apt update
sudo apt -y upgrade
python3 -V
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv
```

### Boot Up Virtual Environment

`python3 -m venv my_env` was used to create virtual environment in `environments/my_env/`.

So run:

```bash
source environments/my_env/bin/activate
```

To exit virtual env:

```bash
deactivate
```

## Python for PHP Developers

### Hello World

#### PHP

```php
<?php
echo 'hello world';
```

#### Python

```py
print('hello world')
```

### Indentation

Must use 4 spaces. 

Same as PHP, assuming you're using [PSR standards](https://www.php-fig.org/psr/psr-12/#24-indenting).

Except in Python, not doing so gets you fatal errors, because Python's 4-space indentation replaces the need for `{` and `}` in code blocks.

#### PHP

```php
$x = 1;
if($x == 1) {
    echo 'x is 1';
}
```

#### Python

```py
x = 1
if x == 1:
    print('x is 1');
```

### Numbers

Like PHP, Python is dynamically typed at runtime. But also has explicit type-casting.

Floats suck far less in Python.

#### PHP

```php
$x = 2;
echo $x;

// php is terrible for this
$y = 3.0;
var_dump( number_format((float)$x, 1, '.', '') );

// even when typecasting to float. Still need number_format()
$x = (float) 4;
var_dump( number_format($x, 1, '.', '') );
```

#### Python

```py
x = 2
print(x)

y=3.0
print(x) # prints 3.0

z=float(4)
print(z) # prints 4.0
```

### Strings

#### PHP

```php
# concatenation
echo 'hello' . ' ' . 'world';

# string repeating
str_repeat('Repeat', 3); # prints: RepeatRepeatRepeat
```

#### Python

```py
# string concat is like JS
print('hello' + ' ' + 'world')

# string repeating is like Ruby
print('Repeat' * 3) # prints: RepeatRepeatRepeat
```
### Lists

Python lists are php numeric arrays.

#### PHP

```php
```

#### Python

```py
# append() adds new elements
mylist = []
mylist.append(1)
mylist.append('two')
mylist.append(3.0)

# looping arrays
for x in mylist:
    print(x)

# 
thatlist = [1,2,3,4]

for x in thatlist:
    print(x)

try:
    print(mylist[5])
except:
    print('but accessing elements that don\'t exist throws exceptions')

# + operator concat's list
even = [2,4,6,8]
odd = [1,3,5,7]
print(even + odd)

# repeat lists
print([1,2,3] * 10)
```
### String Formatting

#### PHP

```php
```

#### Python

```py
```

### String Operations

#### PHP

```php
```

#### Python

```py
```

### Assignments

#### PHP

```php
```

#### Python

```py
```

### Arithmetic

#### PHP

```php
```

#### Python

```py
```

### Concatenation

#### PHP

```php
```

#### Python

```py
```

### Type Checking

#### PHP

```php
```

#### Python

```py
```

### Conditions

#### PHP

```php
```

#### Python

```py
```

### Loops

#### PHP

```php
```

#### Python

```py
```

### Functions

#### PHP

```php
```

#### Python

```py
```

### Classes

#### PHP

```php
```

#### Python

```py
```

### Dictionaries

#### PHP

```php
```

#### Python

```py
```