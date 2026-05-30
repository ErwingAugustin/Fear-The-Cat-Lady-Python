#Erwing Augustin
#It 140
#CAT LADY game

# displays rules at start of game 

print("-------------------------FEAR THE CAT LADY------------------------------")
print("The ferociously lazy cat lady has taken over the master bedroom,\nyour job as a brave adventurer is to Capture and get rid of her,\nbut be warned she is agile and strong and dangerous with her sharp claws.\nYou will begin at the start point in the Garage, but before you take her on;\nyou will need to travel throughout the House gathering supplies")
print("INSTRUCTIONS\nCollect 6 items and capture the Cat Lady to win the game.\n""To Move Type: south, north, east, west.\n""TO Add Items to Inventory Type : collect.")

# Define the rooms and their connections
rooms = {
    'Garage': {'north': 'Mudroom'},
    'Mudroom': {'south': 'Garage', 'north': 'Diningroom', 'east': 'Livingroom', 'west': 'Regularbathroom'},
    'Diningroom': {'north': 'Kitchen', 'south': 'Mudroom'},
    'Regularbathroom': {'east': 'Mudroom'},
    'Livingroom': {'north': 'Regularbedroom', 'west': 'Mudroom'},
    'Regularbedroom': {'south': 'Livingroom'},
    'Masterbathroom': {'south': 'Kitchen'},
    'Kitchen': {'south': 'Mudroom', 'north': 'Masterbathroom', 'west': 'Masterbedroom'},
    'Masterbedroom': {'east': 'Kitchen'},
}
# Define the items in each room
items = {
    'Diningroom': 'Cat Carrier',
    'Livingroom': 'Laser Pointer',
    'Regularbathroom': 'Catnip',
    'Regularbedroom': 'Scratching Post',
    'Kitchen': 'Squeaky Toy',
    'Masterbathroom': 'Spray Bottle',
    'Masterbedroom': 'Cat Lady'
}
# Function to move between rooms
def move(current_room, direction):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("You can't go that way!")
        return current_room

# Function to collect items
def collect_item(current_room, inventory):
    if current_room in items:
        item = items[current_room]
        if item != 'Cat Lady':
            inventory.append(item)
            print(f"You have collected a {item}.")
            del items[current_room]  # Remove the item from the room
        else:
            print("the CAT Lady is here! You can't collect anything.")
    else:
        print("There is nothing to collect here.")
#starting Room
def main():
    current_room = 'Garage'
    inventory = []

    while True:
        print(f"\nYou are in the {current_room}.")
        print("Inventory:", inventory)
        command = input("Enter a direction (north, south, east, west) or 'collect': ").strip().lower()

        if command in ['north', 'south', 'east', 'west']:
            current_room = move(current_room, command)
        elif command == 'collect':
            collect_item(current_room, inventory)
        else:
            print("Invalid command!")

        # End the game if the player finds 6 items and makes it to the Masterbedroom
        if  len(inventory) == 6 and current_room=='Masterbedroom':
            print("Congratulations!!!! You have collected all 6 Items,\nYou have found and captured th CAT LADY!")
            break
        
if __name__ == "__main__":
    main()
    
