# Reference: 
# https://science.nasa.gov/climate-change/effects/

# Create a dictionary
my_dict = {}
climate_change_impact = {
  'Climate': ['global temperatures rise', 'sea level rise', 'glaciers are shrinking', 'carbon dioxide rises', 'snow is melting earlier'],
  'Food': ['challenges for farming', 'heat-related health issues', 'harm livestock'],
  'Water': ['flooding', 'stronger and more frequent abnormally heavy precipitation events', 'drought', 'plants need more water', 'less snow overall'],
  'Infrastructure': ['more indoor cooling', 'flooding shuts down highways and major business areas', 'sea level rise affects coastal infrastructure (e.g., roads, bridges, water supplies)']
} 
my_yogurt = {
  'kefir': 6.9,
  'filmjolk': 4.6,
  'regular yogurt': 3.7
}
print(climate_change_impact['Infrastructure'])
print(climate_change_impact['Infrastructure'][0])
print(my_yogurt['filmjolk'])
print(my_yogurt.get['filmjolk2']) # None

def make_dict(**kwargs):
    return kwargs

make_dict(alpha = 1, beta = 2, gamma = 6)
# {'alpha': 1, 'beta': 2, 'gamma': 6}

# Obtain items
print(my_yogurt.items())
# dict_items([('kefir', 6.9), ('filmjolk', 4.6), ('regular yogurt', 3.7)])
print(my_yogurt.keys())
# dict_keys(['kefir', 'filmjolk', 'regular yogurt'])
print(my_yogurt.values())
# dict_values([6.9, 4.6, 3.7])

# Add new item
my_yogurt['filmjolk2': 5.6]
print(my_yogurt.items())

# Modify the value
my_yogurt['regular yogurt'] = 3.5
print(my_yogurt['regular yogurt'])

# Delete a dictionary
del my_yogurt

# Remove a key-value pair
del my_yogurt['regular yogurt']

# Empty a dictionary
my_yogurt.clear()

# Iterate a dictionary
for key, value in my_yogurt.items():
  print(f'\nproduct: {key}')
  print(f'price: {value}')

for key, value in my_yogurt.items():
  print(f"The price of the {key} is {value}.")

# Iterate the key
for key in my_yogurt:
  print(f'\nproduct: {key}')

# Iterate the value
for value in my_yogurt.values():
  print(f'\nprice: {value}')
