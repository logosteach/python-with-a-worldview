# ============================================================
#  The Adventurer's Pack
#  A game that practices lists, indexing, negative indexing,
#  append, insert, del, pop, and len
# ============================================================

print("=" * 55)
print("       THE ADVENTURER'S PACK")
print("=" * 55)
print("You are packing for an important journey.")
print("Manage your backpack wisely!\n")

# Start with an empty backpack (a list)
backpack = []

# Maximum number of items the backpack can hold
MAX_CAPACITY = 8

while True:
    print("\n" + "-" * 40)
    print("What would you like to do?")
    print("1. View everything in the backpack")
    print("2. Add an item to the end (append)")
    print("3. Insert an item at a specific position")
    print("4. Remove the last item (pop)")
    print("5. Remove an item by its number (del)")
    print("6. Look at a specific item by index")
    print("7. Check how many items you are carrying (len)")
    print("8. Quit the game")
    print("-" * 40)

    choice = input("Enter your choice (1-8): ").strip()

    # ----- 1. VIEW INVENTORY (looping + indexing) -----
    if choice == "1":
        if len(backpack) == 0:
            print("\nYour backpack is empty.")
        else:
            print("\nItems in your backpack:")
            # Loop through the list using indexing
            for i in range(len(backpack)):
                print(f"  Slot {i}: {backpack[i]}")

    # ----- 2. APPEND -----
    elif choice == "2":
        if len(backpack) >= MAX_CAPACITY:
            print(f"\nYour backpack is full! (Maximum {MAX_CAPACITY} items)")
        else:
            item = input("What item would you like to add? ").strip()
            if item == "":
                print("You can't add an empty item.")
            else:
                backpack.append(item)
                print(f"'{item}' has been added to the end of your backpack.")

    # ----- 3. INSERT -----
    elif choice == "3":
        if len(backpack) >= MAX_CAPACITY:
            print(f"\nYour backpack is full! (Maximum {MAX_CAPACITY} items)")
        else:
            item = input("What item would you like to insert? ").strip()
            if item == "":
                print("You can't insert an empty item.")
            else:
                try:
                    position = int(input(f"At which position? (0 to {len(backpack)}): "))
                    if 0 <= position <= len(backpack):
                        backpack.insert(position, item)
                        print(f"'{item}' has been inserted at position {position}.")
                    else:
                        print("That position is outside the backpack.")
                except ValueError:
                    print("Please enter a valid number for the position.")

    # ----- 4. POP (remove last item) -----
    elif choice == "4":
        if len(backpack) == 0:
            print("\nYour backpack is already empty. Nothing to remove.")
        else:
            removed_item = backpack.pop()          # removes and returns the last item
            print(f"You removed '{removed_item}' from the end of the backpack.")

    # ----- 5. DEL (remove by index) -----
    elif choice == "5":
        if len(backpack) == 0:
            print("\nYour backpack is empty. Nothing to delete.")
        else:
            print("\nCurrent items:")
            for i in range(len(backpack)):
                print(f"  {i}: {backpack[i]}")
            try:
                index = int(input("Enter the number of the item to delete: "))
                if 0 <= index < len(backpack):
                    removed = backpack[index]
                    del backpack[index]            # deletes the item at that index
                    print(f"'{removed}' has been removed from the backpack.")
                else:
                    print("That number is not a valid slot.")
            except ValueError:
                print("Please enter a valid number.")

    # ----- 6. INDEXING (positive and negative) -----
    elif choice == "6":
        if len(backpack) == 0:
            print("\nYour backpack is empty.")
        else:
            print("\nYou can use positive or negative indexes.")
            print("  0 = first item")
            print(f"  {len(backpack)-1} = last item")
            print("  -1 = last item (negative indexing)")
            print("  -2 = second-to-last item, etc.")
            try:
                index = int(input("Enter an index: "))
                # This works for both positive and negative indexes
                item = backpack[index]
                print(f"The item at index {index} is: '{item}'")
            except IndexError:
                print("That index is outside the backpack.")
            except ValueError:
                print("Please enter a valid number.")

    # ----- 7. LEN -----
    elif choice == "7":
        current = len(backpack)
        print(f"\nYou are currently carrying {current} item(s).")
        print(f"Backpack capacity: {current} / {MAX_CAPACITY}")
        if current == 0:
            print("Your pack is empty — time to find some supplies!")
        elif current >= MAX_CAPACITY:
            print("Your pack is completely full!")
        else:
            print(f"You still have room for {MAX_CAPACITY - current} more item(s).")

    # ----- 8. QUIT -----
    elif choice == "8":
        print("\nYou close the backpack and set off on your journey.")
        print("Thanks for playing The Adventurer's Pack!")
        break

    # ----- Invalid menu choice -----
    else:
        print("\nPlease enter a number from 1 to 8.")
        
# Copyright 2026 LogosTeach - All Rights Reserved
