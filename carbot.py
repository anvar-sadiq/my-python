def start(carname):
    print(f"car starting {carname}")

def gearNutre():
    print("on nutre")

def steerdirection():
    print("steering")

def turnIndicatorsOnce():
    print("click click")

def turnFirstGear():
    print("on first gear")

def indicatorOn(direction):
    print(f"now turning Indicator {direction}")

def changrgearto(gearNumber):
    print(f"now running on gear {gearNumber}")


def main():
    start("ROLLS ROYCE")
    # turnIndicatorsOnce()
    gearNutre()
    steerdirection()
    changrgearto(1)
    turnFirstGear()
    indicatorOn("RIGHT")
    print("car is now moving")





main()
