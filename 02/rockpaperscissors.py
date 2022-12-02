map = {
    "A": "Rock", "B": "Paper", "C": "Scissors",
    "X":
        {
            "A": "Scissors",
            "B": "Rock",
            "C": "Paper"},
    "Y":
        {
            "A": "Rock",
            "B": "Paper",
            "C": "Scissors"
        },
    "Z":
        {
            "A": "Paper",
            "B": "Scissors",
            "C": "Rock"
        }
}

pointmap = {"Rock": 1, "Paper": 2, "Scissors": 3, "Draw": 3, "Win": 6}

def playRound(a, b):
    points = pointmap[b]
    if a == b: return points + pointmap["Draw"]
    if (b == "Rock" and a == "Scissors") or (b == "Paper" and a == "Rock") or (b == "Scissors" and a == "Paper"):
        return points + pointmap["Win"]
    else:
        return points

if __name__ == '__main__':
    input = open('input').readlines()
    total = 0
    for i in input:
        i = i.strip()
        a = i[0]
        b = i[2]
        total = total + playRound(map[a], map[b][a])
    print(total)