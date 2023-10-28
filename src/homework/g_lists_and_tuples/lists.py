#

def add_inventory(inventory,video_games,quantity):
    if video_games in inventory:

        inventory[video_games] += quantity

    else:

        inventory[video_games] = quantity 


def remove_inventory_widget(inventory,video_games):

    if video_games in inventory:
        del inventory[video_games]
        return "record deleted "
    else: 
        return "item not found "

