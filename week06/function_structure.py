
def display_greeting():
  print("Hello world!")

def greet_personally(name):
    print("Hello", name)

def create_greeting(name):
    greeting = "Hello " + name
    return greeting



if __name__ == "__main__":  # ignore this line for now
    message = create_greeting("Drew")
    print(message)

    print(create_greeting('Adem'))
