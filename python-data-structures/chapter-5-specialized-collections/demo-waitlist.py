from collections import deque

# Create a waitlist deque
waitlist = deque()

# Append new elements
def arrive(name, vip=False):
    if vip:
        waitlist.appendleft(name)
        print(f"VIP Costumer {name} added to the front of the waitlist.")
    else:
        waitlist.append(name)
        print(f"Costumer {name} added to the end of the waitlist.")

    print(waitlist)

# Remove elements
def seat_costumer():
    if waitlist:
        name = waitlist.popleft()
        print(f"Costumer {name} is now being seated.")
    else:
        print("The waitlist is currently empty.")

    print(waitlist)

arrive('martina')
arrive("júlia", True)
arrive('seulgi')
seat_costumer()
seat_costumer()