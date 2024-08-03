"""
If you have downloaded the source code you will find a file named WorldSeriesWinners.
txt in the Chapter 07 folder. This file contains a chronological list of the World Series win
ning teams from 1903 through 2009. (The first line in the file is the name of the team that
won in 1903, and the last line is the name of the team that won in 2009. Note the World
Series was not played in 1904 or 1994.)
Write a program that lets the user enter the name of a team, then displays the number of
times that team has won the World Series in the time period from 1903 through 2009.
"""


def main():
    try:
        SHIFT = 1903
        worldSeriesWinners = []
        with open("WorldSeriesWinners.txt", "r") as file:
            for line in enumerate(file):
                line = list(line)
                if line[0] in range(1, 91):
                    line[0] += 91
                worldSeriesWinners.append((line[0] + SHIFT, line[1].rstrip()))

        team_name = take_team_name()
        victory = count_team_victory(team_name, worldSeriesWinners)

        if len(victory):
            print("Team have won", len(victory), 'times')
            print("here's the years of victory", victory)
        else:
            print("Team not found in winners list")

    except FileNotFoundError:
        print("File not found")


def take_team_name():
    team_name = input("Enter a name of a team: ")
    return team_name


def count_team_victory(team, list_of_teams):
    res = []
    for el in list_of_teams:
        if el[1] == team:
            res.append(el[0])

    return res


if __name__ == '__main__':
    main()
