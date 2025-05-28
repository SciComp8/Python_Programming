class IntronicVariant:
    def set_variant_info(self, gene, location, description):
        self.gene = gene 
        self.location = location
        self.description = description
        # Alternatively, we can write self.gene, self.location, self.description = gene, location, description

# Why use `self` in Python class method set_variant_info?
# Without self, variables would be local to the method `set_variant_info` and disappear after `set_variant_info` finishes.
# `self` initializes the object when created. `self` ensures values are stored in the object itself, so they persist.

variant = IntronicVariant()
variant.set_variant_info('Gene_XYZ', 'Intron 3', 'A common intronic variant associated with disease M')

print(f"Gene: {variant.gene}")
print(f"Location: {variant.location}")
print(f"Description: {variant.description}")

variant.gene = variant.gene + ' Gene_ABC'
print(f"Gene: {variant.gene}")

# Define attributes in methods
class RNASample:
    def set_name(self, new_name): # Add methods/functions to a class
        self.name = new_name
    def set_expression_values(self, values): # Add methods/functions to a class
        self.expression_values = values
    def calculate_mean_expression(self): # Add methods/functions to a class
        if not self.expression_values:
            return 0
        return sum(self.expression_values) / len(self.expression_values)
    def calculate_max_expression(self): # Add methods/functions to a class
        if not self.expression_values:
            return 0
        return max(self.expression_values)

rna_sample = RNASample()
rna_sample.set_name('Sample_001')
expression_values = [10.1, 16.3, 2.1, 1.1, 10.8]
rna_sample.set_expression_values(expression_values)

mean_expression = rna_sample.calculate_mean_expression()
print(f"Mean Expression: {mean_expression}")

max_expression = rna_sample.calculate_max_expression()
print(f"Max Expression: {max_expression}")

dir(rna_sample) # List all the attributes and methods of an object
help(rna_sample) # Show the documentation of a class associated with an object

# Define attributes in the __init__ constructor
# Why build __init__ constructor? 
# Because we want to avoid defining attributes outside the constructor, making it easier for collaborators to locate all attributes
class RNASample2:
    def __init__(self, new_name, values=None):
        self.name = new_name
        self.expression_values = values
    def calculate_mean_expression(self): 
        if not self.expression_values:
            return 0
        return sum(self.expression_values) / len(self.expression_values)
    def calculate_max_expression(self): 
        if not self.expression_values:
            return 0
        return max(self.expression_values)

rna_sample_2 = RNASample2('Sample_001', [10.1, 16.3, 2.1, 1.1, 10.8])
mean_expression = rna_sample_2.calculate_mean_expression()
print(f"Mean Expression: {mean_expression}")

max_expression = rna_sample.calculate_max_expression()
print(f"Max Expression: {max_expression}")

class Falafel:
    def __init__(self,type='baked'): # use self as the 1st argument in method definition; self refers to the data of a particualr object
        self.ingrediate = ['Chickpeas', 'Onion', 'Parsley', 'Garlic', 'Green Chile Pepper', 'Oil', 'Baking Soda'] # Create the attribute ingrediate
        self.type = type
        if self.type not in ['fried','baked']:
            print('Unrecognized type: ' + str(self.type))
            print('Type will be set to baked')
            self.type = 'baked'
        self.origin = 'Egyptian cuisine'
    def eat(self):
        print('I got eaten')
    def new_origin(self):
        self.origin = 'Levantine cuisine'
        print('I bought' + self.origin)

class MultiFalafel(Falafel): 
    def __init__(self,num=1,num_to_eat=1):
        self.number = num
        self.number_eat = num_to_eat
        if self.number_eat > self.number:
            print('Reset the number of falafels eaten '+str(num_to_eat)+' to the total number of falafels '+str(num))
            self.number_eat = num
        Falafel.__init__(self)
        print(str(num)+' falafel(s) created')
    def eat(self):
        print(str(self.number_eat)+' falafel(s) got eaten')
        self.remaining = self.number - self.number_eat

def inspect_falafel_class(c):
    if issubclass(c, Falafel):
        print(f"{c.__name__} inherits from the Falafel class")
    else:
        print(f"{c.__name__} does not inherit from the Falafel class")

inspect_falafel_class(MultiFalafel)
# MultiFalafel inherits from the Falafel class

# Test the code
# six_falafels = MultiFalafel(num=6,num_to_eat=7) # Ignore self when calling method on an object
# six_falafels.eat()
# six_falafels.remaining
# six_falafels.type
# six_falafels.ingrediate
# six_falafels.new_origin()

# Build a grandchild class
class SuperFalafel(MultiFalafel):
    def __init__(self, num=1, num_to_eat=1, supersize=False):
        super().__init__(num, num_to_eat) # Call the constructor of the parent class (MultiFalafel)
        self.supersize = supersize
    def eat(self):
        if self.supersize:
            print(f"{str(self.number_eat)} supersized falafel(s) got eaten")
        else:
            super().eat() # Call the eat method of the parent class (MultiFalafel)

# super() tells Python:
# "Hey parent class(es), I’m your child. Please initialize yourself first before I adds anything extra."
# In this case, it calls the __init__() of MultiFalafel (the parent class).
# Python follows the Method Resolution Order to decide which __init__() to call first. 

print(SuperFalafel.__mro__)

super_falafel = SuperFalafel(num=3, num_to_eat=2, supersize=True) # 3 falafel(s) created
super_falafel.eat() # 2 supersized falafel(s) got eaten

