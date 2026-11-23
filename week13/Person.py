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
        self.__trusted_party = False
        self.__job_title = None
        self.__birth_month = -1
        self.__birth_day = -1
        self.__ssn = -1

    def __str__(self):
        return f"{self.__first_name} {self.__last_name}-- birthday on {self.__birth_month}/{self.__birth_day}"

    def get_first_name(self):
        return self.__first_name

    def set_trusted_party(self, status:bool):
        self.__trusted_party = status

    def is_trusted_party(self):
        return self.__trusted_party

    def set_job_title(self, title:str):
        self.__job_title = title

    def get_job_title(self):
        return self.__job_title

    def has_ssn(self):
        return self.__ssn != -1
    
    def set_ssn(self, ssn:int):
        self.__ssn = ssn

    def get_ssn(self, who_asks):
        if who_asks.is_trusted_party():
            return self.__ssn
        else:
            return "None of your business"
        
    def set_birthday(self, month: int, day: int):
        if month >= 1 and month <= 12 and day >= 1 and day <= 31:
            self.__birth_month = month
            self.__birth_day = day

if __name__ == "__main__":
    d = Person("Drew")
    d.set_ssn(123456789)

    l = Person("Leo")
    l.set_job_title("Prof")

    result = d.get_ssn(l)
    print(result)

    l.set_job_title("Loan Officer")
    l.set_trusted_party(True)
    result = d.get_ssn(l)
    print(result)

    
