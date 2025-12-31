# Bin2Dec

![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This is a simple python program based off of the very first program from the [app-ideas](https://github.com/florinpop17/app-ideas/tree/master) repository.

---

## Features

- Converts binary to decimal
- Validates input (Only accepts 0s and 1s) and checks if it is longer than 8 digits
- Raises errors for an invalid input
- It also works as a library (convert() function) or by itself

---

## How to run

1. Make sure you have python installed
2. Clone this repository or download the bin2dec.py file
3. Run the command 'python bin2dec.py' in cmd or equivilent
4. Enter binary number when prompted

## How to use as a library

``` python
from bin2dec import convert

number = convert("1011")
print(number) #This will output 11 if ran
```
---

### Author
Tobie Denby

