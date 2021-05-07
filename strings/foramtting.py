'''
String .format() method
General Form:
    <template>.format(<positional_argument(s)>, <keyword_argument(s)>)

    <template> --> String containing replacement fields. Template's replacement fields are included in {}.
    <positional_argument(s)> and <keyword_argument(s)> --> specify the values that
        are inserted in place of the replacement values.
'''

# Include curly brace as literal by doubling them.
print('{{{}}}'.format('foo'))

'''
Positional arguments
'''
print('{0} {1} cost ${2}'.format(6, 'bananas', 1.4))
print('{1} {0} cost ${2}'.format(6, 'bananas', 1.4))  # order of positional numbers matter
print('{} {} cost ${}'.format(6, 'bananas', 1.4))  # omitted positional numbers

# Format ignores extra arguments
print('{} {}'.format('foo', 'bar', 'baz'))

'''
Keyword arguments
'''
print('{quantity} {item} cost ${cost}'.format(quantity=6, item='bananas', cost=1.4))
print('{quantity} {item} cost ${cost}'.format(cost=1.4, quantity=6, item='bananas'))  # keyword order does not matter


'''
Replacement fields consists of 3 components
    {[<name>][!<conversion>][:<format_spec>]}
    
    <name>	        Specifies the source of the value to be formatted
    <conversion>	Indicates which standard Python function to use to perform the conversion
    <format_spec>	Specifies more detail about how the value should be converted
    
    Each component is optional and can be omitted.
'''

# <name>
# indicates which argument from the argument list is inserted into the Python format string in the given location.
# It’s either a number for a positional argument or a keyword for a keyword argument.
x, y, z = 1, 2, 3
print('{0}, {1}, {baz}'.format(0, 1, baz=9))  # simple variables

my_list = ['a', 'b', 'c']
print('{0[0]}, {0[2]}'.format(my_list))  # Using lint indices to replace names.

z = 3+5j
print('real = {0.real}, imag = {0.imag}'.format(z))  # Using objects in formatting names

# <conversion>
# Python can format an object as a string using three different built-in functions:
#   str()       !s	Convert with str()
#   repr()      !r	Convert with repr()
#   ascii()     !a	Convert with ascii()
print('{0!s}'.format(20))
print('{0!r}'.format(21))
print('{0!a}'.format(22))

# <format_spec>
# It contains information that exerts fine control over how values are formatted
# prior to being inserted into the template string.
#   :[[<fill>]<align>][<sign>][#][0][<width>][<group>][.<prec>][<type>]
# The 10 sub components
#   :	    Separates the <format_spec> from the rest of the replacement field
#   <fill>	Specifies how to pad values that don’t occupy the entire field width
#           <any character>
#   <align>	Specifies how to justify values that don’t occupy the entire field width
#           "<" left-aligned within the available space
#           ">" right-aligned within the available space
#           "=" padding to be placed after the sign (if any) but before the digits.
#           "^" centered within the available space
#   <sign>	Controls whether a leading sign is included for numeric values
#           "+"     indicates that a sign should be used for both positive as well as negative numbers.
#           "-"     indicates that a sign should be used only for negative numbers (this is the default behavior).
#           space   indicates that a leading space should be used on positive numbers, and a minus sign on negative
#                   numbers.
#   #	    Selects an alternate output form for certain presentation types
#           Only valid for integer, float, complex and Decimal types
#   0	    Causes values to be padded on the left with zeros instead of ASCII space characters
#   <width>	Specifies the minimum width of the output
#   <group>	Specifies a grouping character for numeric output
#   .<prec>	Specifies the number of digits after the decimal point for floating-point presentation types,
#           and the maximum output width for string presentations types
#   fill        ::=  <any character>
#   align       ::=  "<" | ">" | "=" | "^"
#   sign        ::=  "+" | "-" | " "
#   width       ::=  integer
#   precision   ::=  integer
#   <type>	Specifies the presentation type, which is the type of conversion performed on the corresponding argument
#       Possible <type> values
#       b	    Binary integer
#       c	    Single character
#       d	    Decimal integer
#       e or E	Exponential
#       f or F	Floating point
#       g or G	Floating point or Exponential
#       o	    Octal integer
#       s	    String
#       x or X	Hexadecimal integer
#       %	    Percentage
print('{:d}'.format(1000))  # d - Decimal integer
print('{:f}'.format(4.1))  # f - Floating point
print('{:s}'.format('blah blah'))  # s - String
print('{:x}'.format(1000))  # x - Hexadecimal
print('{:%}'.format(0.7))  # % - Percentage
print('{:b}'.format(123))  # b - Binary
print('{0:<8s}'.format('foo'))  # Left align string
print('{0:<8d}'.format(123))  # Left align digit
print('{0:>8s}'.format('foo'))  # Right align string
print('{0:>8d}'.format(123))  # Right align digit
print('{0:+8d}'.format(123))  # Sign
print('{0:=+8d}'.format(123))  # Sign with padding
print('{0:-6d}'.format(123))  # Sign only negative numbers
print('{0:-6d}'.format(-123))  # Sign only negative numbers
print('{0: d}'.format(123))  # Space for positive number
print('{0: d}'.format(-123))  # Sign only negative numbers
print('{0:*^8s}'.format('foo'))  # Fill with * and center

# (#) Causes inclusion of an explicit base indicator to the left of the value
print('Binary -> b formats to {0:b}, #b formats to {0:#b}'.format(16))  # Alternate representation
print('Octal -> o formats to {0:o}, #o formats to {0:#o}'.format(16))  # Alternate representation
print('Hexadecimal -> x formats to {0:x}, #x formats to {0:#x}'.format(16))  # Alternate representation

# For floating-point or exponential presentation types, the hash character forces the output to contain a decimal point
# even if the output consists of a whole number
print('{0:.0f}, {0:#.0f}'.format(123))
print('{0:.0e}, {0:#.0e}'.format(123))


