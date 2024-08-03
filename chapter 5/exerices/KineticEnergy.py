"""
In physics, an object that is in motion is said to have kinetic energy. The following formula
can be used to determine a moving object’s kinetic energy:
KE 5 ½ mv2
The variables in the formula are as follows: KE is the kinetic energy, m is the object’s mass
in kilograms, and v is the object’s velocity in meters per second.
Write a function named kinetic_energy that accepts an object’s mass (in kilograms)
and velocity (in meters per second) as arguments. The function should return the amount
of kinetic energy that the object has. Write a program that asks the user to enter values
for mass and velocity, then calls the kinetic_energy function to get the object’s kinetic
energy.
"""


def kinetic_energy(mass, velocity):
    mass = float(mass)
    velocity = float(velocity)

    # calculate the KE
    kinetic_energy_value = 1 / 2 * mass * velocity * velocity
    print("the object KE (mass =", mass, "velocity = ", velocity, ") is = ", round(kinetic_energy_value, 2))


from app_frame import app_frame

app_frame(kinetic_energy, mass=0, velocity=0)
