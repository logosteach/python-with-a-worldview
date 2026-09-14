"""
Devin's Pet Store  --  Unit 5 OOP practice file
================================================

READ THIS FIRST.

You are not expected to write a program this size on your own yet.
This file exists so you can *see objects in action*: classes, instances,
inheritance, encapsulation, getters and setters, and a running loop that
uses those objects all day long.

Read it from the top down. Run it. Change a price. Add a sixth dog breed.
Break a setter on purpose and watch the pre-condition catch you.

Vocabulary you will meet in the comments:
    OOP, class, instance, instantiation, attribute, method, self,
    __init__ / constructor, instance attribute, class attribute,
    encapsulation, abstraction, inheritance, polymorphism,
    parent / child, override, super(), composition, is-a / has-a,
    decorator, @property, getter, setter, pre-condition, post-condition,
    state, behavior, public interface, leading underscore.

Owner of the store in this story: Devin.
"""

# ---------------------------------------------------------------------------
# A CLASS ATTRIBUTE lives on the class itself, not on one animal.
# Every animal in the store pays the same sales tax, so the rate belongs
# here once, not copied onto every puppy.
# ---------------------------------------------------------------------------
SALES_TAX_RATE = 0.08  # 8 percent. Used as a module-level constant too.


class Animal:
    """Parent class. Every creature Devin sells *is-an* Animal.

    Think of a class as a blueprint. An *instance* is one real animal
    built from that blueprint. The line later that says
        scout = Labrador("Scout", 250.00)
    is called *instantiation*.
    """

    # Class attribute: shared idea, not one animal's private fact.
    kingdom = "Animalia"

    def __init__(self, name, price):
        # self is "this particular animal." Python passes it for you
        # when you write scout.speak() -- you never type self in the call.
        self.name = name
        self._sold = False
        # _price has a leading underscore: a hint that callers should
        # use the public interface (the price property) instead of
        # poking at the raw number. That is *encapsulation*.
        self.price = price  # goes through the setter below

    # ----- getter / setter with @property (a decorator) --------------------
    # A decorator is the @ line sitting above a method. It wraps the
    # method in extra behavior. @property lets us write animal.price
    # as if it were a plain attribute, while still running our checks.

    @property
    def price(self):
        """Getter. Returns the stored price tag."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter.
        Pre-condition: the new price must be a number greater than 0.
        Post-condition: self._price holds that number.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("A price tag has to be a number.")
        if value <= 0:
            raise ValueError("Devin does not give animals away. Price must be > 0.")
        self._price = float(value)

    @property
    def sold(self):
        return self._sold

    def mark_sold(self):
        """Behavior that changes state. After this, the animal is no longer for sale."""
        self._sold = True

    def speak(self):
        """Default sound. Child classes *override* this. That override is
        one example of *polymorphism*: one name (speak), many forms."""
        return f"{self.name} makes a quiet animal sound."

    def behave(self):
        """A second behavior every animal has. Children override this too."""
        return f"{self.name} looks around the shop."

    def price_tag(self):
        """Abstraction: the caller does not need to know how we format money."""
        return f"${self.price:.2f}"

    def describe(self):
        status = "SOLD" if self._sold else "for sale"
        return f"{self.name} ({self.__class__.__name__}) -- {self.price_tag()} -- {status}"

    def do_taxes(self):
        # A wink from the Unit 5 assignment. Animals do not file taxes.
        return f"{self.name} cannot do taxes. That is Devin's job."


# ---------------------------------------------------------------------------
# Mid-level parents. A Labrador *is-a* Dog *is-an* Animal.
# super() calls the parent constructor so we do not repeat name/price setup.
# ---------------------------------------------------------------------------
class Dog(Animal):
    species = "dog"

    def speak(self):
        return f"{self.name} barks: Woof!"

    def behave(self):
        return f"{self.name} wags a tail and sniffs a customer."


class Cat(Animal):
    species = "cat"

    def speak(self):
        return f"{self.name} meows: Mrrp?"

    def behave(self):
        return f"{self.name} hops onto a shelf and knocks a toy down."


class Bird(Animal):
    species = "bird"

    def speak(self):
        return f"{self.name} chirps: tweet-tweet!"

    def behave(self):
        return f"{self.name} flutters to a higher perch."


class Gerbil(Animal):
    """Gerbils inherit straight from Animal. There is no GerbilBreed layer
    because Devin just sells 'gerbils,' not five named gerbil breeds."""

    species = "gerbil"

    def speak(self):
        return f"{self.name} squeaks softly."

    def behave(self):
        return f"{self.name} stuffs both cheeks and darts into a tube."


# ----- five dog breeds -----------------------------------------------------
class Labrador(Dog):
    def speak(self):
        return f"{self.name} the Labrador woofs happily."

    def behave(self):
        return f"{self.name} drops a tennis ball at your feet."


class Beagle(Dog):
    def speak(self):
        return f"{self.name} the Beagle howls a little howl."

    def behave(self):
        return f"{self.name} follows a scent trail around the aisle."


class Poodle(Dog):
    def speak(self):
        return f"{self.name} the Poodle yips."

    def behave(self):
        return f"{self.name} poses as if a camera just appeared."


class GermanShepherd(Dog):
    def speak(self):
        return f"{self.name} the German Shepherd gives a deep bark."

    def behave(self):
        return f"{self.name} stands between Devin and the door, on watch."


class Dachshund(Dog):
    def speak(self):
        return f"{self.name} the Dachshund barks from somewhere near the floor."

    def behave(self):
        return f"{self.name} wriggles under a display table."


# ----- five cat breeds -----------------------------------------------------
class Persian(Cat):
    def speak(self):
        return f"{self.name} the Persian purrs like a small engine."

    def behave(self):
        return f"{self.name} demands to be brushed. Now."


class Siamese(Cat):
    def speak(self):
        return f"{self.name} the Siamese talks back: raow!"

    def behave(self):
        return f"{self.name} inspects every bag a customer carries."


class MaineCoon(Cat):
    def speak(self):
        return f"{self.name} the Maine Coon chirps more than meows."

    def behave(self):
        return f"{self.name} stretches out to full, ridiculous length."


class Tabby(Cat):
    def speak(self):
        return f"{self.name} the Tabby trills."

    def behave(self):
        return f"{self.name} finds the one sunbeam in the shop."


class Calico(Cat):
    def speak(self):
        return f"{self.name} the Calico meows twice, just to be sure."

    def behave(self):
        return f"{self.name} sits in the exact center of the counter."


# ----- five bird breeds ----------------------------------------------------
class Parakeet(Bird):
    def speak(self):
        return f"{self.name} the Parakeet chatters."

    def behave(self):
        return f"{self.name} rings the tiny bell in the cage."


class Cockatiel(Bird):
    def speak(self):
        return f"{self.name} the Cockatiel whistles a scale."

    def behave(self):
        return f"{self.name} raises a crest and tilts its head."


class Canary(Bird):
    def speak(self):
        return f"{self.name} the Canary sings."

    def behave(self):
        return f"{self.name} hops from perch to perch."


class Finch(Bird):
    def speak(self):
        return f"{self.name} the Finch peeps."

    def behave(self):
        return f"{self.name} takes a quick bath in the water dish."


class Parrot(Bird):
    def speak(self):
        return f"{self.name} the Parrot says, 'Hello, Devin!'"

    def behave(self):
        return f"{self.name} imitates the cash drawer slamming shut."


# ---------------------------------------------------------------------------
# Composition (has-a), not inheritance (is-a).
# A CashRegister is not an Animal. The store *has-a* register.
# This is the same idea as the BankAccount assignment: owner, balance,
# deposit, and a guarded setter.
# ---------------------------------------------------------------------------
class CashRegister:
    """Day register. Tracks how much Devin has taken in, tax included."""

    def __init__(self, owner):
        self.owner = owner
        self._balance = 0.0
        self._sales_count = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        # Pre-condition: the register balance is never allowed to go negative.
        if value < 0:
            raise ValueError("The register cannot hold a negative amount.")
        self._balance = float(value)

    @property
    def sales_count(self):
        return self._sales_count

    def deposit(self, amount):
        """Post-condition: balance is larger by amount; sales_count is +1."""
        if amount <= 0:
            raise ValueError("A sale must add a positive amount.")
        self.balance = self._balance + amount
        self._sales_count += 1

    def report(self):
        return (
            f"{self.owner}'s register: "
            f"{self._sales_count} sale(s), ${self._balance:.2f} total (tax included)."
        )


class PetStore:
    """The shop itself. It *has-a* list of animals and *has-a* register.

    That pairing is composition. The store is not a child of Animal
    or CashRegister. It holds them.
    """

    # Class attribute: one name for the whole shop.
    store_name = "Devin's Pet Store"

    def __init__(self, owner):
        self.owner = owner
        self.animals = []
        self.register = CashRegister(owner)
        self.is_open = False

    def stock(self, animal):
        self.animals.append(animal)

    def open_shop(self):
        self.is_open = True
        return f"{self.store_name} is open. {self.owner} turns on the lights."

    def close_shop(self):
        self.is_open = False
        return f"{self.store_name} is closed. {self.register.report()}"

    def for_sale(self):
        """Animals still on the floor."""
        return [a for a in self.animals if not a.sold]

    def find(self, name):
        needle = name.strip().lower()
        for animal in self.animals:
            if animal.name.lower() == needle:
                return animal
        return None

    def morning_chorus(self):
        """Polymorphism in a loop: every object answers .speak() and
        .behave() in its own way. The loop does not care which child
        class it is holding."""
        lines = []
        for animal in self.for_sale():
            lines.append(animal.speak())
            lines.append(animal.behave())
        return lines

    def sell(self, animal):
        """Complete one purchase.
        Pre-condition: the animal exists, is not already sold.
        Post-condition: animal.sold is True; register holds price + tax.
        """
        if animal is None:
            raise ValueError("There is no animal by that name.")
        if animal.sold:
            raise ValueError(f"{animal.name} already went home with someone else.")
        tax = animal.price * SALES_TAX_RATE
        total = animal.price + tax
        animal.mark_sold()
        self.register.deposit(total)
        return animal.price, tax, total


def build_devins_shop():
    """Factory-style helper. Builds one stocked store so main() stays short."""
    shop = PetStore("Devin")

    # Instantiation: each line builds one object from a child class.
    shop.stock(Labrador("Scout", 250.00))
    shop.stock(Beagle("Penny", 180.00))
    shop.stock(Poodle("Gigi", 320.00))
    shop.stock(GermanShepherd("Rex", 400.00))
    shop.stock(Dachshund("Otto", 210.00))

    shop.stock(Persian("Luna", 190.00))
    shop.stock(Siamese("Miso", 175.00))
    shop.stock(MaineCoon("Maple", 230.00))
    shop.stock(Tabby("Pip", 90.00))
    shop.stock(Calico("Clementine", 120.00))

    shop.stock(Parakeet("Kiwi", 35.00))
    shop.stock(Cockatiel("Sunny", 80.00))
    shop.stock(Canary("Goldie", 45.00))
    shop.stock(Finch("Pippin", 25.00))
    shop.stock(Parrot("Captain", 350.00))

    shop.stock(Gerbil("Nibble", 18.00))
    shop.stock(Gerbil("Dash", 18.00))

    return shop


def print_menu():
    print()
    print("  [1] List animals for sale")
    print("  [2] Let the animals make noise and behave")
    print("  [3] A customer buys an animal")
    print("  [4] Look at the register")
    print("  [5] Close the shop for the day")
    print()


def main():
    shop = build_devins_shop()
    print(shop.open_shop())
    print("Tax rate today:", f"{SALES_TAX_RATE:.0%}")
    print("Type a menu number. The shop stays open until you choose 5.")

    # A looped program: the *state* of the objects lives on between turns.
    # The register balance and each animal's sold flag persist.
    while shop.is_open:
        print_menu()
        choice = input("What happens next? ").strip()

        if choice == "1":
            available = shop.for_sale()
            if not available:
                print("Every animal has a home. The floor is empty.")
            else:
                print("On the floor:")
                for animal in available:
                    print("  ", animal.describe())

        elif choice == "2":
            lines = shop.morning_chorus()
            if not lines:
                print("No one left to make a sound.")
            else:
                print("A busy shopping day:")
                for line in lines:
                    print("  ", line)

        elif choice == "3":
            name = input("Which animal is the customer asking for? (name) ").strip()
            animal = shop.find(name)
            try:
                price, tax, total = shop.sell(animal)
            except ValueError as error:
                # A named exception. The pre-condition failed; nothing was sold.
                print("Sale did not go through:", error)
            else:
                print(f"{animal.name} has a new home.")
                print(f"  tag      {animal.price_tag()}")
                print(f"  tax 8%   ${tax:.2f}")
                print(f"  total    ${total:.2f}")
                print("  ", animal.do_taxes())

        elif choice == "4":
            print(shop.register.report())

        elif choice == "5":
            print(shop.close_shop())

        else:
            print("Please pick 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    # This standard line means: run main() when the file is launched
    # directly, but not if some later lesson imports a class from here.
    main()
