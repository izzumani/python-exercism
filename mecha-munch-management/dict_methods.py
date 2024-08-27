"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item_name in items_to_add:
        current_cart[item_name] = current_cart.get(item_name,0) + 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return add_item({}, notes)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    # for idea_key in ideas.keys():
    #     if dict(recipe_updates).get(idea_key,None):
    #         ideas[idea_key] =  dict(recipe_updates)[idea_key]
    ideas |=dict(recipe_updates)
    return ideas

def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    for aisle_key in aisle_mapping.keys():
        
        if cart.get(aisle_key,None)!=None:
            cart_value = cart[aisle_key]
            cart[aisle_key] = aisle_mapping[aisle_key]
            if len(cart[aisle_key]) ==2:
                cart[aisle_key].insert(0,cart_value)
     
    return dict(sorted(cart.items(),reverse=True))
    

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key_fulfil in fulfillment_cart:
        store_inv_list = store_inventory.get(key_fulfil,[0,'',False])
        if store_inv_list[0] > fulfillment_cart[key_fulfil][0]:
            store_inventory[key_fulfil][0] -=fulfillment_cart[key_fulfil][0]
        else:
            store_inv_list[0] = 'Out of Stock'
            store_inventory[key_fulfil] = store_inv_list
    return store_inventory