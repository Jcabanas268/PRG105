# Ingredient Adjuster

# data
# var
servings = 9
chocolate = 8
butter = 12
sugar = 1.25
eggs = 2
vanilla = 2
flour = .75
cocoa = .25
salt = 1

# processing
# Chocolate brownies
print('Welcome to Chocolate Brownies ingredients. ')

# logic to adjust for serving
def print_ingredients():
    print('Serving size for', servings)
    print(format(((chocolate / 9) * servings), ',.1f'), 'oz semi-sweet chocolate')
    print(format(((butter / 9) * servings), ',.1f'), 'tablespoons melted butter')
    print(format(((sugar / 9) * servings), ',.1f'), 'cups of sugar')
    print(format(((eggs / 9) * servings), ',.1f'), 'eggs')
    print(format(((vanilla / 9) * servings), ',.1f'), 'teaspoons of vanilla extract')
    print(format(((flour / 9) * servings), ',.1f'), 'cup all-purpose flour')
    print(format(((cocoa / 9) * servings), ',.1f'), 'cup of cocoa powder')
    print(format(((salt / 9) * servings), ',.1f'), 'teaspoon salt')

# print ingredients
print_ingredients()

# input how many servings
servings = float(input('Enter serving size: '))

# output adjusted ingredients
print_ingredients()

# link : https://tasty.co/recipe/the-best-fudgy-brownies
