import time

def countdown(t):
    while t:
        min, sec =divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(min, sec)
        print(timer, end = '\r')
        time.sleep(1)
        t -= 1
    print("Time's up!")

def help():
    print("Will be made later")

#main program
while True:
    print("Enter 'Help' to display instructions")
    print("Enter 'Timer' to use the timer")
    print("Enter 'Exit' to exit the app")
    a = input("T->")
    if a == "Help" or a == "help":
        help()
    elif a == "Timer" or a == "timer":
        tm = int(input("Enter the minutes : "))
        ts = int(input("Enter seconds : "))
        t = (tm * 60) + ts
        countdown(t)
    elif a == "Exit" or a == "exit":
        break
    else:
        print("Invalid Input")

#just trying things out