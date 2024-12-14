cmd=''
started=False
stopped=False
while cmd.lower() != "quit":
    cmd = input().lower()
    if cmd == "help":
        print("""
start-to start the car
stop - to stop the car
quit - to quit the game
        """)

    elif cmd == "start":
        if started==True:
            print("the car is already started")
        else:
            print("Car has started...")
            started=True

    elif cmd == "stop":
        if stopped==True:
            print("The car has already stopped")
            stopped=True
        else:
            print("the car has stopped")
    elif cmd=="quit":
        print("Bye")
        break
    else:
        print("I dont understand...")

