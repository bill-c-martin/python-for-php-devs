<!-- omit in toc -->
# Python: for PHP Developers

This is a broad overview of Python from a PHP developer's perspective, with code examples to tinker with.

## Table of Contents
- [Install Python and Friends](#install-python-and-friends)
  - [Setup Virtual Environment](#setup-virtual-environment)
- [Python vs PHP Language Comparisons](#python-vs-php-language-comparisons)
  - [Hello World](#hello-world)
  - [Indentation](#indentation)
  - [Numbers](#numbers)
  - [Strings](#strings)
  - [Lists](#lists)
  - [String Formatting](#string-formatting)
  - [String Operations](#string-operations)
  - [Assignments](#assignments)
  - [Arithmetic](#arithmetic)
  - [Concatenation](#concatenation)
  - [Type Checking](#type-checking)
  - [Conditions](#conditions)
  - [Loops](#loops)
  - [Functions](#functions)
  - [Classes](#classes)
  - [Dictionaries](#dictionaries)
  - [Modules and Packages](#modules-and-packages)
  - [Numpy Arrays](#numpy-arrays)
  - [Pandas Basics](#pandas-basics)
  - [Generators](#generators)
  - [List Comprehensions](#list-comprehensions)
  - [Lambda functions](#lambda-functions)
  - [Multiple Function Arguments](#multiple-function-arguments)
  - [Regular Expressions](#regular-expressions)
  - [Exception Handling](#exception-handling)
  - [Sets](#sets)
  - [Serialization](#serialization)
  - [Partial functions](#partial-functions)
  - [Code Introspection](#code-introspection)
  - [Closures](#closures)
  - [Decorators](#decorators)
  - [Map, Filter, Reduce](#map-filter-reduce)

## Install Python and Friends

In Ubuntu:

```bash
sudo apt update
sudo apt -y upgrade

# Confirm python 3.* is installed, else install it
python3 -V

# Get le friends too
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

### Setup Virtual Environment

Install `venv`:

```bash
sudo apt install -y python3-venv
```

Clone this repo, and in the root directory, setup a virtual environment:

```bash
python3 -m venv env
```

Activate the virtual environment:
```bash
source env/bin/activate
```

Test run one of the `.py` files in this repo:

```bash
python3 code/01-hello.py
```

To exit the virtual environment:

```bash
deactivate
```

## Python vs PHP Language Comparisons

These are examples inspired by [learningpython.org](https://www.learnpython.org/), but show the equivalent code for PHP.

Each section has a corresponding `.py` file in this repo that you can tinker with.

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

Like PHP, Python is dynamically-typed.

Floats suck less in Python.

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


### Modules and Packages

Go over things like:

from pandas import read_csv
from sklearn.model_selection import train_test_split

#### PHP

```php
```

#### Python

```py
```
### Numpy Arrays

#### PHP

```php
```

#### Python

```py
```
### Pandas Basics

#### PHP

```php
```

#### Python

```py
```
### Generators

#### PHP

```php
```

#### Python

```py
```
### List Comprehensions

#### PHP

```php
```

#### Python

```py
```
### Lambda functions

#### PHP

```php
```

#### Python

```py
```
### Multiple Function Arguments

#### PHP

```php
```

#### Python

```py
```
### Regular Expressions

#### PHP

```php
```

#### Python

```py
```
### Exception Handling

#### PHP

```php
```

#### Python

```py
```
### Sets

#### PHP

```php
```

#### Python

```py
```
### Serialization

#### PHP

```php
```

#### Python

```py
```
### Partial functions

#### PHP

```php
```

#### Python

```py
```
### Code Introspection

#### PHP

```php
```

#### Python

```py
```
### Closures

#### PHP

```php
```

#### Python

```py
```
### Decorators

#### PHP

```php
```

#### Python

```py
```
### Map, Filter, Reduce

#### PHP

```php
```

#### Python

```py
```
