SHIFT = 1903

numberOfTeamWins = {

}
teamOftheYear = {

}


def processfile():
    with open("WorldSeries.txt", "r") as f:
        for index, line in enumerate(f):
            line = line.rstrip()
            if line.startswith("World Series Not Played"):
                continue
            if line in numberOfTeamWins:
                numberOfTeamWins[line] += 1
            else:
                numberOfTeamWins[line] = 1
            teamOftheYear[index + SHIFT] = line

    # print(teamOftheYear)


def main():
    processfile()
    user_input = int(input("Enter year in a range 1903 - 2009: "))
    if user_input not in range(1903,2010):
        print("Wrong range of year")
        exit(1)
    team_name = teamOftheYear.get(user_input,"Not found")
    if team_name == "Not found":
        print(f"World Series Not Played in {user_input}")
        exit(0)
    print(f"{team_name} won in {user_input} but through the range 1903 - 2009 he won"
          f" {numberOfTeamWins[team_name]} times")



if __name__ == '__main__':
    main()
