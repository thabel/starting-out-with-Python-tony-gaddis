import tkinter
import random

class SolarSystemGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Solar System")

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=800, height=800, bg="black")
        
        # Draw the Sun and planets
        self.draw_solar_system()

        # Pack the canvas.
        self.canvas.pack()

        # Start the mainloop.
        tkinter.mainloop()

    def draw_solar_system(self):
        # Sun
        self.canvas.create_oval(370, 370, 430, 430, fill="yellow", outline="yellow")
        self.canvas.create_text(400, 450, text="Sun", fill="white")

        # Planet details: (name, color, distance from Sun, diameter)
        planets = [
            ("Mercury", "gray", 60, 10),
            ("Venus", "orange", 100, 20),
            ("Earth", "blue", 140, 20),
            ("Mars", "red", 180, 15),
            ("Jupiter", "brown", 220, 40),
            ("Saturn", "goldenrod", 260, 35),
            ("Uranus", "light blue", 300, 30),
            ("Neptune", "blue", 340, 30),
            ("Pluto", "white", 380, 8)
        ]

        # Draw planets
        for planet in planets:
            name, color, distance, diameter = planet
            x0 = 400 - diameter // 2
            y0 = 400 - distance - diameter // 2
            x1 = 400 + diameter // 2
            y1 = 400 - distance + diameter // 2
            
            self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline=color)
            self.canvas.create_text(400, y0 - 10, text=name, fill="white")

# Create an instance of the SolarSystemGUI class.
solar_system_gui = SolarSystemGUI()
