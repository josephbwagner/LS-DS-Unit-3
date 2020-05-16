from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome',
              'Shiny',
              'Impressive',
              'Portable',
              'Improved',
              'Charred',
              'Holographic',
              'Giant']
NOUNS = ['Anvil',
         'Catapult',
         'Disguise',
         'Mousetrap',
         'Guitar',
         'Toothbrush',
         'Can of Peas',
         'Straw Hat',
         'Wooden Sword']


def generate_products(num_products=30):
    '''
    Generates a list of Products with some random attributes

    Parameters:
    num_products (int): number of Products to generate

    Returns:
    products (list): list of Product objects
    '''
    products = []
    for item in range(num_products):
        # Generate product name
        prod_name = (str(sample(ADJECTIVES, 1)[0]) +
                     str(' ') +
                     str(sample(NOUNS, 1)[0]))

        # Generate Product instance attributes
        prod_price = randint(5, 100)
        prod_weight = randint(5, 100)
        prod_flammability = uniform(0.0, 2.5)

        # Initialize Product
        prod = Product(name=prod_name,
                       price=prod_price,
                       weight=prod_weight,
                       flammability=prod_flammability)

        # Assign to products
        products.append(prod)
    return products


def inventory_report(products):
    '''
    Display formatted report (as a side-effect) of generated products

    Parameters:
    products (list): output of `generate_products`

    Returns:
    0
    '''
    unique_names = set()
    prices_list = []
    weights_list = []
    flammability_list = []

    for item in products:
        # Get all unique elements by inserting into a set
        unique_names.add(item.name)
        # Build list of `products` item prices, weights, and flammability
        prices_list.append(item.price)
        weights_list.append(item.weight)
        flammability_list.append(item.flammability)

    # Calculate averages
    average_price = sum(prices_list) / len(prices_list)
    average_weight = sum(weights_list) / len(weights_list)
    average_flammability = sum(flammability_list) / len(flammability_list)

    # Display report
    print('\nACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:\t', len(unique_names))
    print('Average price:\t\t', average_price)
    print('Average weight:\t\t', average_weight)
    print('Average flammability:\t', average_flammability, '\n')

    return 0


if __name__ == '__main__':
    inventory_report(generate_products())
