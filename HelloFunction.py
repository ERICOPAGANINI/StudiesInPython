def main():

    hello()
    name= input("Whats your name? ")
    hello(name)
    
def hello(to="World"):
    print("Hello,", to)

main()