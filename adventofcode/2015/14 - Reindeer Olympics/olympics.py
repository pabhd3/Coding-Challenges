from json import dumps

class Reindeer:
    def __init__(self, name, speed, flyDuration, restDuration, state):
        self.name = name
        self.speed = speed
        self.flyDuration = flyDuration
        self.restDuration = restDuration
        self.state = state
        self.traveled = 0

    def __str__(self):
        return dumps({"name": self.name, "speed (km/s)": self.speed, 
            "fly (sec)": self.flyDuration, "rest (sec)": self.restDuration,
            "state": self.state, "traveled": self.traveled}, indent=4)

if __name__ == "__main__":
    # Read input data
    with open("input.txt", "r") as r:
        data = r.read()
        r.close()
    # Create the Reindeer
    allReindeer = []
    for reindeer in data.split("\n"):
        name, _, _, speed, _, _, flyDuration, _, _, _, _, _, _, restDuration, _ = reindeer.split()
        allReindeer.append(Reindeer(name=name, speed=int(speed), 
            flyDuration=int(flyDuration), restDuration=int(restDuration),
            state={"state": "Fly", "timeRemaining": int(flyDuration)}))
    # Loop through the seconds
    for _ in range(0, 2504):
        print("-------------------------")
        # Loop through each reindeer
        for r in allReindeer:
            if(r.state["state"] == "Fly"):
                if(r.state["timeRemaining"] > 0):
                    r.traveled += r.speed
                    r.state["timeRemaining"] -= 1
                elif(r.state["timeRemaining"] == 0):
                    r.state["state"] = "Rest"
                    r.state["timeRemaining"] = r.restDuration
                    print(r.name, "is now in state", r.state["state"])
            elif(r.state["state"] == "Rest"):
                if(r.state["timeRemaining"] > 0):
                    r.state["timeRemaining"] -= 1
                elif(r.state["timeRemaining"] == 0):
                    r.state["state"] = "Fly"
                    r.state["timeRemaining"] = r.flyDuration
                    print(r.name, "is now in state", r.state["state"])
    # Print States
    for reindeer in allReindeer:
        print(reindeer)
    print("\nResults")
    print(max(allReindeer, key=lambda r: r.traveled))