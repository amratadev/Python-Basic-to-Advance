# Function to create a person's info
def person(name, bid):
    person_info = {}                # dictionary banayi
    person_info["Name"] = name       # name assign kiya
    person_info["Bid"] = bid         # bid assign kiya
    return person_info               # dictionary return kiya

# Auction dictionary to store all participants
auction = {}

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid amount? "))
    choice = input("Do you want to continue? (Y/N): ")

    # ek person ka info dictionary me store karna
    auction[name] = person(name, bid)

    if choice.upper() != "Y":        # agar choice Y nahi hai to loop break
        break

# Final auction dictionary print karna
print("Auction Results:")
print(auction)