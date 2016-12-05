Modular Python

In order for a module or package to be reusable, it has to meet the following requirements:
* It must function as a standalone unit
* If your package is intended to be included as part of the source code for another system, you must use relative imports to load the other modules within your package
* Any external dependencies must be clearly noted
*

There are three things that distinguish an excellent reusable module from a poor one:
* It attempts to solve a general problem (or range of problems), rather than just performing a specific task
* It follows standard conventions that make it easier to use the module elsewhere
* The module is clearly documented so that other people can easily understand and use it
*

Python Style Guide --> https://www.python.org/dev/peps/pep-0008/

the Python Package Index (https://pypi.python.org/pypi) provides a huge repository of shared modules and packages. You can search for a package by name or keyword, or you can browse through the repository by topic, license, intended audience, development status, and so on.

A high-quality reusable module or package will alwaysinclude documentation. This documentation will both explain what the module does and how it works, and include examples so that readers can immediately see how to use this module or package within their own programs.

https://www.python.org/dev/peps/pep-0008/#id45

A docstring is a Python string that gets attached to a module or function. This is used specifically for documentation purposes, and there is a very special Python syntax for creating docstrings:

In Python, you can use three quote characters to mark a string that goes across more than one line of the Python source file. These triple-quoted strings can be used in various places, including docstrings. If a module starts with a triple-quoted string, then this string is used as the documentation for the module as a whole. Similarly, if any function starts with a triple-quoted string, then this string is used as documentation for that function.

Docstrings are typically used to describe what a module or function does, the parameters that are needed, and what information is returned. Any noteworthy aspects of the module or function should also be included, for example unexpected side effects, usage examples, and so on.

Use 4 spaces per indentation level.
Continuation lines should align wrapped elements either vertically using Python's implicit line joining inside parentheses, brackets and braces, or using a hanging indent [7] . When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line.
Yes:
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
var_one, var_two, var_three,
var_four):
print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
var_one, var_two,
var_three, var_four)
No:
# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
var_one, var_two, var_three,
var_four):
print(var_one)
The 4-space rule is optional for continuation lines.

Tabs should be used solely to remain consistent with code that is already indented with tabs.
Python 3 disallows mixing the use of tabs and spaces for indentation.
Python 2 code indented with a mixture of tabs and spaces should be converted to using spaces exclusively.


Should a line break before or after a binary operator?
For decades the recommended style was to break after binary operators. But this can hurt readability in two ways: the operators tend to get scattered across different columns on the screen, and each operator is moved away from its operand and onto the previous line. Here, the eye has to do extra work to tell which items are added and which are subtracted:
# No: operators sit far away from their operands
income = (gross_wages +
taxable_interest +
(dividends - qualified_dividends) -
ira_deduction -
student_loan_interest)
To solve this readability problem, mathematicians and their publishers follow the opposite convention. Donald Knuth explains the traditional rule in his Computers and Typesetting series: "Although formulas within a paragraph always break after binary operations and relations, displayed formulas always break before binary operations" [3] .
Following the tradition from mathematics usually results in more readable code:
# Yes: easy to match operators with operands
income = (gross_wages
+ taxable_interest
+ (dividends - qualified_dividends)
- ira_deduction
- student_loan_interest)
In Python code, it is permissible to break before or after a binary operator, as long as the convention is consistent locally. For new code Knuth's style is suggested.

* Imports should usually be on separate lines, e.g.: Yes: import os
* import sys
*
* No: import sys, os
*  It's okay to say this though: from subprocess import Popen, PIPE
*  
* Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants. Imports should be grouped in the following order:
1. standard library imports
2. related third party imports
3. local application/library specific imports
* You should put a blank line between each group of imports. 
* Absolute imports are recommended, as they are usually more readable and tend to be better behaved (or at least give better error messages) if the import system is incorrectly configured (such as when a directory inside a package ends up on sys.path ): import mypkg.sibling
* from mypkg import sibling
* from mypkg.sibling import example
*  However, explicit relative imports are an acceptable alternative to absolute imports, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose: from . import sibling
* from .sibling import example
*  Standard library code should avoid complex package layouts and always use absolute imports. Implicit relative imports should never be used and have been removed in Python 3. 
* When importing a class from a class-containing module, it's usually okay to spell this: from myclass import MyClass
* from foo.bar.yourclass import YourClass
*  If this spelling causes local name clashes, then spell them import myclass
* import foo.bar.yourclass
*  and use "myclass.MyClass" and "foo.bar.yourclass.YourClass". 
* Wildcard imports ( from import * ) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API (for example, overwriting a pure Python implementation of an interface with the definitions from an optional accelerator module and exactly which definitions will be overwritten isn't known in advance). 

* Avoid trailing whitespace anywhere. Because it's usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker. Some editors don't preserve it and many projects (like CPython itself) have pre-commit hooks that reject it. 
* Always surround these binary operators with a single space on either side: assignment ( = ), augmented assignment ( += , -= etc.), comparisons ( == , < , > , != , <> , <= , >= , in , not in , is , is not ), Booleans ( and , or , not ). 
* If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator. Yes: i = i + 1
* submitted += 1
* x = x*2 - 1
* hypot2 = x*x + y*y
* c = (a+b) * (a-b)
*  No: i=i+1
* submitted +=1
* x = x * 2 - 1
* hypot2 = x * x + y * y
* c = (a + b) * (a - b)
*  
* Don't use spaces around the = sign when used to indicate a keyword argument or a default parameter value. Yes: def complex(real, imag=0.0):
* return magic(r=real, i=imag)
*  No: def complex(real, imag = 0.0):
* return magic(r = real, i = imag)
*  
* Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present. (See Function Annotationsbelow for more about function annotations.) Yes: def munge(input: AnyStr): ...
* def munge() -> AnyStr: ...
*  No: def munge(input:AnyStr): ...
* def munge()->PosInt: ...
*  
* When combining an argument annotation with a default value, use spaces around the = sign (but only for those arguments that have both an annotation and a default). Yes: def munge(sep: AnyStr = None): ...
* def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
*  No: def munge(input: AnyStr=None): ...
* def munge(input: AnyStr, limit = 1000): ...
*  
* Compound statements (multiple statements on the same line) are generally discouraged. Yes: if foo == 'blah':
* do_blah_thing()
* do_one()
* do_two()
* do_three()
*  Rather not: if foo == 'blah': do_blah_thing()
* do_one(); do_two(); do_three()
*  
* While sometimes it's okay to put an if/for/while with a small body on the same line, never do this for multi-clause statements. Also avoid folding such long lines! Rather not: if foo == 'blah': do_blah_thing()
* for x in lst: total += x
* while t < 10: t = delay()
*  Definitely not: if foo == 'blah': do_blah_thing()
* else: do_non_blah_thing()
*
* try: something()
* finally: cleanup()
*
* do_one(); do_two(); do_three(long, argument,
* list, like, this)
*
* if foo == 'blah': one(); two(); three() 
Function names should be lowercase, with words separated by underscores as necessary to improve readability.
mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.
Function and method arguments
Always use self for the first argument to instance methods.
Always use cls for the first argument to class methods.
If a function argument's name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus class_ is better than clss . (Perhaps better is to avoid such clashes by using a synonym.)
