def main():
    Mean_Radius = {
        "Io": 1821.6,
        "Europa": 1560.8,
        "Ganymede": 2634.1,
        "Callisto": 2410.3,
    }
    Surface_Gravity = {
        "Io": 1.796,
        "Europa": 1.314,
        "Ganymede": 1.428,
        "Callisto": 1.235,
    }
    Orbital_Period = {
        "Io": 1.769,
        "Europa": 3.551,
        "Ganymede": 7.154,
        "Callisto": 16.689,
    }

    name = input("Enter Moon name: ")
    if name not in Mean_Radius:
        print(f'No moon named {name} foud')
    else:
        print(f"Here is {name} radius {Mean_Radius[name]}")
        print(f"Here is {name} surface gravity {Surface_Gravity[name]}")
        print(f"Here is {name} orbital period {Orbital_Period[name]}")


if __name__ == '__main__':
    main()
