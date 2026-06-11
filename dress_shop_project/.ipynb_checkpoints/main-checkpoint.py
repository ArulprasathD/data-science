import inventory as inv

def greeting():
    return "welcome"


def main():

    print(greeting())

    while True:
        print("\n""Available dress")
        for i in inv.collections():
            print(i)

        dress = input("which dress would you like : ").lower()

        if dress in inv.collections():
            print("\n""dress available")
            break

        else:
            print("\n""not available")
            
    print("\n""Available Brand")
    for j in inv.brand():
        print(j)

    selected_brand = input("which brand would you like:").lower()

    print("\n""Available colours")
    for k in inv.colours():
        print(k)

    selected_colour = input("which colour would you like :").lower()

    print("\n"f"SELECTED DRESS : {dress}")
    print("\n"f"SELECTED BRAND :{selected_brand}")
    print("\n"f"SELECTED COLOUR : {selected_colour}")

    if dress == "shirt":
        print("Total bill :",inv.PRICE["shirt"])
    elif dress == "pant":
        print("Total bill :",inv.PRICE["pant"])
    elif dress == "t-shirt":
        print("Total bill :",inv.PRICE["t-shirt"])
    elif dress == "track":
        print("Total bill :",inv.PRICE["track"])


 
if __name__ == "__main__":
     main()