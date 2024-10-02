## Problem statement
You are given multiple lines of code written in a made up lisp-like programming language. Your task is to write a simple interpreter given the definition of the available functions, interpret the code we will provide and return to us everything printed to the console. In case a program terminates with an error, return everything printed to the console before the error and the printed error message. Error message is printed to the console automatically when error is thrown.
 
### Assumptions:
 
1. The input consists only functions defined in this document.
2. Each function invocation is wrapped in brackets (see examples below).
3. There is a space between function name and argument(s). Function arguments are space separated.
4. Functions never mutate original arguments but instead return a copy.
5. Calling a function with an incorrect number of arguments will result in an error.
6. If a single expression raises multiple errors, you can treat it as a single error.
7. No semicolons at the end of the line.

// in the examples is used to denote a comment. It will not appear in the actual code.

## Supported data types:
1. String: provided in double quotes (")
2. Boolean: true and false
3. Number: can be integer or decimal.
4. Null

## Printing to console
Can be done with method puts which accepts a single String argument. Providing an argument of any type other than String will result in an error. This function returns null
 
### Example:
 
#### Input:
 
(puts "hello world")

#### Output:
 
hello world

## Variable assignment

Set function accepts a constant variable name and a single argument of any type. Returns null. Variable names will be given in camel case containing only alphabets.
 
### Example:
 
(set x 5)

Assigning a new value to an existing variable will result in an error. Incorrect order of the arguments will result in an error.
 
## String operations

### Concatenation
concat function accepts 2 arguments of String type. Passing argument of any other type will result in an error. Returns a new String created by appending second argument to the first.
 
#### Example:
 
(concat "ab" "c")
// returns: "abc"
### Lowercase
lowercase function returns a copy of an input String converted to lower case. Providing an argument of any type other than String will result in an error.
 
#### Example:
 
(lowercase "ABC")
// returns "abc"

### Uppercase
uppercase function returns a copy of an input String converted to upper case. Providing an argument of any other type than string will result in an error.
 
#### Example:
 
(uppercase "abc")
// returns "ABC"

### Substring replacement
replace function returns a new String obtaining by replacing each substring of target in source with replacement String. Source String remains unchanged
 
#### Arguments:
 
source: String

target: String

replacement: String

If target String is not present in the source, returns source String
 
Providing argument(s) of any type other than String will result in an error.
 
#### Example::
 
(replace "abcdef" "abc" "123")
// returns "123def"

(replace "abc" "xyz" "123")
// returns "abc"

### Substring
substring function returns a substring specified by given range indices with start inclusive and end index exclusive.
 
#### Arguments:
 
source: String

start: Non-negative number, inclusive

end: Non-negative number, exclusive

First character of String is at index 0.
 
#### Example:
 
(substring "abcdef" 0 3)
// returns "abc"

Providing argument(s) of incorrect type will result in an error. When at least one of the indices is out of bounds an error is thrown.
 
## Number operations
NOTE: Each function below should return result accurate to 4 dps.
 
### Addition
add function accepts at least 2 arguments of numeric type and returns a new number by adding all arguments.
 
#### Example:
 
(add 1 2)
// returns 3

(add 1 2 3 4 5)
// returns 15

Providing at least one argument of a type other than number will result in an error.
 
### Subtraction
subtract function accepts at 2 arguments of numeric type and returns a new number by subtracting the second argument from the first one.
 
#### Example:
 
(subtract 10 2)
// returns 8

(subtract 1 2)
// returns -1

Providing at least one argument of a type other than number will result in an error.
 
### Multiplication
multiply function accepts at least 2 arguments of numeric type and returns a new number by multiplying all arguments.
 
#### Example:
 
(multiply 2 3)
// returns 6

(multiply 2.0 3)
// returns 6.0

(multiply 2 2.5)
// returns 5.0

(multiply 1 2 3 4 5)
// returns 120

Providing at least one argument of a type other than number will result in an error.
 
### Division
divide function accepts two arguments of numeric type: dividend and divisor. Providing at least one argument of a type other than number will result in an error. If both operands are integer then it should perform integer division. Division by zero will result in an error.
 
#### Example:
 
(divide 6 2)
// returns 3

(divide 1 2)
// returns 0

(divide 1.0 2)
// returns 0.5

### Absolute value

abs function accepts a single argument of numeric type. Returns an absolute value of the provided argument. Providing an argument of a type other than number will result in an error.
 
#### Example:
 
(abs -1)
// returns 1

(abs 1)
// returns 1 

### Max
max function accepts a variable number of arguments (at least 2) of numeric type. Returns the largest number among the provided arguments.
 
Providing no arguments will result in an error.
 
Providing an argument of a type other than number will result in an error.
 
#### Example:
 
(max 1 -2)
// returns 1

(max 1 2 3 4 5)
// returns 5

### Min
min function accepts a variable number of arguments (at least 2) of numeric type. Returns the smallest number among the provided arguments.
 
Providing no arguments will result in an error.
 
Providing an argument of a type other than number will result in an error.
 
#### Example:
 
(min 1 2)
// returns 1

(min 5 4 3 2 1)
// returns 1

### Greater than
gt function accepts 2 numeric arguments. Returns true if the first argument has greater value than the second, otherwise returns false.
 
Providing no arguments will result in an error.
 
Providing an argument of a type other than number will result in an error.
 
#### Example:
 
(gt 1 2)
// returns false

(gt 2 1)
// returns true

### Lower than
lt function accepts 2 numeric arguments. Returns true if the first argument has smaller value than the second, otherwise returns false.
 
Providing an argument of a type other than number will result in an error.
 
Providing no arguments will result in an error.
 
Providing an argument of a type other than number will result in an error.
 
#### Example:
 
(lt 1 2)
// returns true

(lt 2 1)
// returns false

For Number operations involving decimals please keep your console outputs to minimum required decimal points (no trailing 0s except for the first) with a max of 4. For example:
 
(add 10.0 10) should return 20.0 (not 20)
 
(divide 10 3.0) should return 3.3333
 
(divide 10 4.0) should return 2.5
 
## Equality check operations
Can be performed on String, Number and null
 
equal returns true if value and type of two arguments are equal.
 
### Arguments:
 
first: String | Number | Boolean | null

second: String | Number | Boolean | null

### Examples:
 
(equal 2 2.0)
// returns true

(equal 2 "2")
// returns false

(equal null null)
// returns true

not_equal returns true if value or type of two arguments are different.
 
### Arguments:
 
first: String | Number | Boolean | null

second: String | Number | Boolean | null

### Examples:
 
(not_equal 2 2.0)
// returns false

(not_equal 2 "2")
// returns true

(not_equal null 5)
// returns true

## Conversion to String

str function accepts a single argument of String, Number, Boolean types or null and converts it to String.
 
### Examples:
 
(str 5)
// returns "5"

(str null)
// returns "null"

## Error Handling
All errors are unrecoverable (i.e. the evaluation stops on the first error). Once the error occurs, the error message is printed to the console. The error message contains a String ERROR at line and line number where error was raised.
 
### Example:
 
#### Input:
 
(divide 1 0)  // line 1

#### Output:
 
ERROR at line 1
 
## Examples (viewable at /examples)
### Case 1
(puts "Hello World")

(puts (str 5))

(puts (concat "ABC " (str true)))

### Expected result:
 
Hello World
5
ABC true

### Case 2
(set v "Hello World")
(puts (concat v ", Student"))

### Expected result:
 
Hello World, Student
## Input format
 
As shown in the problem definition, the input code can span multiple lines. You will receive input as a JSON key/value pair, where value is a String array, as in this example. Keep in mind that quotes(") will be escaped in the input your application will receive:
 
{
  "expressions": [
    "(puts \"Hello\")",
    "(puts \"World!\")"
  ]
}
