#%% Quest-1

# output : ('company', 'country', 'price', 'currency')
def stock_info(company, country, price, currency):
    return f'Company: {company} \n Country: {country} \n Price: {price}{currency}'

print(stock_info.__code__.co_varnames)
print(stock_info('Jio', 'India', 453, 'Rs'))


# %% Quest-2

import builtins

help(builtins.sum)
print(builtins.sum([-4, 3, 2]))

# %% Quest-3

"""counter = 1
def update_counterv1():
    counter += 1
    #code
print(update_counterv1()) """ 
counter = 1
def update_counterv2():
    global counter
    counter += 1
    print(counter)

print(update_counterv2())
print(counter)

# %% Quest-4 
counter = 0
dot_counter = ''
def update_counterv3():
    global counter, dot_counter
    counter += 1
    dot_counter += '.'

# function `update_counterv3()` should call 40 times
[update_counterv3() for _ in range(40)]
print(counter)
print(dot_counter)

# %% Quest-5 

def display_info(num_of_updates=1):
    counter = 100
    dot_counter = ''
    def update_counterv4():
        nonlocal counter, dot_counter
        counter += 1
        dot_counter += '.'
    [update_counterv4() for _ in range(num_of_updates)]
    print(counter)
    print(dot_counter)
    
display_info(10)
# %% Quest-6 

import datetime

for name in sorted(datetime.__dict__):
    print(name)

# %% Quest-7
import uuid

class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price
    def __repr__(self):
         return f"Product(product_name='{self.product_name}', price = {self.price}')"
        
    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]
    
for name in Product.__dict__:
    print(name)
# %%
import uuid

class Productv2:
    def __init__(self, product_name, product_id, price):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        
    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})" 
product = Productv2('Mobile Phone', '54274', 2900)

print(product.__dict__)
# %%

def stick(*args):
    args = [arg for arg in args if
            isinstance(arg, str)]
    result= '#'.join(args)
    return result

print('sport', 'summer')
print(stick(4, 3, 6))
print(False, True, 'time', 'gym', 'exercise', '[]', 'getout')

# %% Quest-10

def display_info(company, **kwargs):
    print(f'Company name: {company}')
    if 'price' in kwargs:
        print(f"Price: Rs {kwargs['price']}")
        
display_info(company='CD projekt', price=100)

# %% Quest-11 :
