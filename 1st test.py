cmd=''
while cmd.lower() != "quit":
    cmd = input().lower()
    if cmd == "help":
        print("""
        start-to start the car
        stop - to stop the car
        quit - to quit the game
        """)

    elif cmd == "start":
        print("Car has started...")

    elif cmd == "stop":
        print("the car has stopped")
    elif cmd=="quit":
        print("Bye")
        break
    else:
        print("I dont understand...")

