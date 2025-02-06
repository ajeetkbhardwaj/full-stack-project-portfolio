# Python Interview Quest
##### Quest :  Local Enclosed Global Built-In Rules

**Quest-1 :** The `stock_info( )` function is defined. Using the appropriate attribute of the `stock_info( )` function, display
the names of all arguments to this function to the console.
An example of calling the function:
print(stock_info('ABC', 'USA', 115, '$'))
Company: ABC
Country: USA
Price: $ 115
Tip: Use the code attribute of the function.

```
# output : ('company', 'country', 'price', 'currency')
def stock_info(company, country, price, currency):
    return f'Company: {company} \n Country: {country} \n Price: {currency}{price}'

print(stock_info.__code__.co_varnames)
print(stock_info('Jio', 'India', 453, 'Rs'))

```
**Quest-2 :** Using the built-ins module import the sum( ) function. Then display its documentation of this function.
Call the function on the list below and print the result to the console.
[-4, 3, 2]
Expected result:
Help on built-in function sun in nodule built-ins:
sum(iterable, /, start=0)
Return the sun of a 'start' value (default: 0) plus an iterable of numbers
When the Iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may reject non-numeric types.
1

**Quest-3 :** . A global variable counter is given with an incorrectly implemented update_counter() function.
Correct the implementation of the update_counter ( ) function so that you can modify the counter
variable from this function. Then call the update_counter ( ) function.
Tip: Use the global statement.
Expected result:
 2

**Quest-4 :** 4. The following global variables are given:
• counter
• dot_counter
and incorrectly implemented update_counters ( ) function. Correct the implementation of the
update_counters ( ) function so that you can modify the values of the given global variables from this
function. Then call update_counters() 40 times.
In response, print the value of the counter and dot_counter global variables to the console as shown below.
Tip: Use the global statement.

**Quest-5 :** A display_info() function was implemented. This function has an incorrectly implemented internal
update_counter( ) function. Correct the implementation of this function so that you can modify non-local
variables: counter and dot_counter from the internal function
update_counter() .
In response, call dispiay_info( ) with the number_of_updates argument set to 10.
Tip: Use the nonlocal statement.
Expected result:
110

##### Quest : Namespace and Scope

**Quest-6 :** Import the built-in datetime module and display the namespace of this module (sorted alphabetically) as
given below.
Tip: Use the _dict_ attribute of the datetime module.

Expected Output :
MAXYEAR
MINYEAR
UTC
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
date
datetime
datetime_CAPI
sys
time
timedelta
timezone
tzinfo

**Quest-7 :** The Product class is given below. Display the namespace (value of the _dict_ attribute) of
this class as shown below.
Expected result:
__module__
__init__
__repr__
get_id
__dict__
__weakref__
__doc__
```
import uuid
class Product:
 def __init__(self, product_name, price):
 self.product_id = self.get_id()
 self.product_name = product_name
 self.price = price
 def __repr__(self):
 return f"Product(product_name='{self.product_name}', price={self.price})"
@staticmethod
 def get_id():
 return str(uuid.uuid4().fields[-1])[:6]
```
**Quest-8 :** The Product class is specified. An instance of this class named product was created. Display the
namespace (value of the _dict_ attribute) of this instance as shown below.
Expected result:
{'product_name': 'Mobile Phone1, 'product_id': '54274', 'price': 2900}
import uuid
class Product:
 def __init__(self, product_name, product_id, price):
 self.product_name = product_name
 self.product_id = product_id
 self.price = price
 def __repr__(self):
 return f"Product(product_name='{self.product_name}', price={self.price})"
product = Product('Mobile Phone', '54274', 2900)


**Quest-9 :** Implement a function called stick( ) that takes any number of bare arguments and return an object of type
str being a concatenation of all arguments of type str passed to the function with the '#' sign (see below).
Example:
[IN]: stick('sport', 'summer', 4, True)
[OUT]: 'sport#summer’
As an answer call the stick( ) function in the following ways (print the result to the console):
• stick('sport', 'summer')
• stick(3, 5, 7)
stick(False, 'time'. True, 'workout', [], 'gym')

**Quest-10 :**
Implement a function called dispiay_info() which prints the name of the company (as shown below) and
if the user also passes an argument named price , it prints the price (as shown below).
Example I:
[IN]: dlsplay_info(company='Amazon')
Company name: Apple
Example II:
[IN]: display_info(company='Amazon', price=1140)
Company name: Amazon Price: $ 1140
In response, call display_info() as shown below:
display_info(company='CD Projekt', price=100)
Expected result:
Company name: CD Projekt Price: $ 100
def display_info(company, **kwargs):
 pass