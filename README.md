# Fear-The-Cat-Lady-Python: Text-Based Adventure

## Overview
A Python-based adventure game developed to demonstrate foundational programming concepts including dictionary-based state management, nested data structures, and conditional logic. 

The player navigates a multi-room house to collect 6 specific items (Laser Pointer, Cat Carrier, etc.) to successfully "capture" the Cat Lady boss in the Master Bedroom.

## Technical Implementation & Features

* **Dictionary-Based State Engine:** Modeled the entire house layout and item locations using nested Python dictionaries. Movement options update dynamically based on the player’s current room coordinates.
* **Algorithmic Flow Control:** Structured the game loop inside a continuous `while True` block that evaluates user choices for navigation or actions.
* **Input Validation & Sanitization:** Protected the runtime engine from crashing by utilizing `.strip().lower()` on all user commands, ensuring the game safely handles accidental uppercase letters or trailing spaces.
* **Inventory Management:** Tracks gathered tools in a running player inventory array. Once an item is successfully collected, it is removed from the room directory using the `del` keyword to prevent duplication exploits.

---

## Game Map Layout

* **Garage** (Starting Point) -> Leads North to the Mudroom.
* **Mudroom** -> The central hub connecting to the Dining Room (North), Garage (South), Living Room (East), and Regular Bathroom (West).
* **Kitchen** -> Houses the Squeaky Toy; opens West directly into the Master Bedroom (Boss Room).

### Item Registry
* **Dining Room:** Cat Carrier
* **Living Room:** Laser Pointer
* **Regular Bedroom:** Scratching Post
* **Regular Bathroom:** Catnip
* **Kitchen:** Squeaky Toy
* **Master Bathroom:** Spray Bottle
## Project Files
* `cat_lady_game.py`: The main game engine.
* `design_document.pdf`: Original planning, pseudocode, and game map.

## How to Run
1. Ensure Python 3.x is installed.
2. Run `python cat_lady_game.py` in your terminal.
3. Follow the on-screen prompts to navigate and collect items.
