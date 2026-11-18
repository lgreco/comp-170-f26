class Person:
    """The structure of a simple object in pictorial
    form (using Unified Modeling Language - UML).

    ------------------------------|
    | Person                      |
    | ----------------------------|
    | - first_name: str           |
    | - last_name: str            |
    | - fav_snack: str            |
    | - birth_month: int          |
    | - birth_day: int            |
    | - ssn: int                  |
    | ----------------------------|
    | + get_first_name() -> str   |
    | + get_ssn() -> int          |
    | -----------------------------
    """

    # The first thing we write in a class,
    # is how to instantiate itself.
    # THE CONSTRUCTOR
    def __init__(self, first_name: str):
        self.__first_name = first_name
        self.__last_name = None
        self.__fav_snack = None
        self.__birth_month = -1
        self.__birth_day = -1
        self.__ssn = -1

    def __str__(self):
        return f"{self.__first_name} -- birthday on {self.__birth_month}/{self.__birth_day}"

    def set_birthday(self, month: int, day: int):
        if month >= 1 and month <= 12 and day >= 1 and day <= 31:
            self.__birth_month = month
            self.__birth_day = day


blue_hoodie = Person("Anthony")
print(blue_hoodie)
blue_hoodie.set_birthday(2,31)
print(blue_hoodie)
