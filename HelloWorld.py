def who2greet(args=None):
    name = input("input the name you want to 'Hello':")
    return name

def main():
    name = who2greet()
    print("Hello " + name +"!")

if __name__ == "__main__":
    main()