import numpy as np
import matplotlib.pyplot as plt
import turtle
import time
from scipy.interpolate import make_interp_spline

#GLOBAL PARAMETERS
INITIAL_X = 0
INITIAL_Y = 200
SETPOINT = 0
TIME_STEP = 0.001
FRAME_COUNT = 500
MASS = 1
SPRING_K = 8000
STARTING_PHASE = 0
B = 8
#-----------------

class Simulation(object):
    def __init__(self):
        self.mass = Mass()
        self.screen = turtle.Screen()
        self.screen.setup(400, 700)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(180)
        self.marker.goto(15, SETPOINT)
        self.marker.color('red')
        self.sim = True
        self.timer = 0
        self.positions = np.array([])
        self.times =np.array([])
        self.stationary = np.array([INITIAL_Y])
        self.stationary_times = np.array([0])
    def cycle(self):
        while(self.sim):
            self.mass.set_y(self.timer * TIME_STEP)
            time.sleep(TIME_STEP)
            self.timer += 1
            self.positions = np.append(self.positions, self.mass.get_y())
            self.times = np.append(self.times, self.timer)
            if self.mass.get_dy(self.timer * TIME_STEP) < 800 and self.mass.get_dy(self.timer * TIME_STEP) > 0 and self.mass.get_y() > 0:
                self.stationary = np.append(self.stationary, self.mass.get_y())
                self.stationary_times = np.append(self.stationary_times, self.timer)
                print(self.timer, self.mass.get_dy(self.timer * TIME_STEP))
            if self.timer > FRAME_COUNT:
                print("SIMULATION ENDED")
                self.sim = False
        graph(self.times, self.positions, self.stationary_times, self.stationary)

def graph(x, y, sx, sy):  # Function for plotting the results of the simulation on a matplotlib graph
    #Things for smoothing out the line marking the decay of amplitude over time
    x_new = np.linspace(sx.min(), sx.max(), 300)
    smoothed_sx = make_interp_spline(sx, sy)
    y_new = smoothed_sx(x_new)
    #End of smoothing code
    #Need to write a piece of code which just plots the stationary points (calculated) in the given number of frames for better accuracy

    plt.plot(x, y)
    plt.plot(x_new, y_new)
    plt.plot(x, 0.4*np.ones(len(x)), color='black', linewidth=0.8)
    plt.title("Dampened oscillations")
    plt.ylabel("Position")
    plt.xlabel("Time")
    plt.margins(x=0)
    plt.show()

class Mass(object):
    def __init__(self):
        global Mass
        self.Mass = turtle.Turtle()
        self.Mass.shape('square')
        self.Mass.color('black')
        self.Mass.penup()
        self.Mass.goto(INITIAL_X, INITIAL_Y)
        self.Mass.speed(0)
        self.y = INITIAL_Y
        self.omega = ((SPRING_K / MASS) - (B / (2*MASS))**2)**0.5
    def set_y(self, time):
        self.y_last = self.y
        self.Mass.sety(INITIAL_Y * np.exp((- B * time) / (2 * MASS)) * np.cos(self.omega * time + STARTING_PHASE))
    def get_y(self):
        self.y = self.Mass.ycor()
        return self.y
    def get_dy(self, time):
        self.dy = (self.y - self.y_last) / TIME_STEP
        #Think below is the correct diffrentiation to get the velocity of the dampened oscillations
        self.dy_2 = (-B/(2*MASS)) * INITIAL_Y * np.exp((- B * time) / (2 * MASS)) * np.cos(self.omega * time + STARTING_PHASE) - INITIAL_Y * np.exp((- B * time) / (2 * MASS)) * self.omega * np.sin(self.omega * time + STARTING_PHASE)
        return self.dy_2

def main():
    simulation = Simulation()
    simulation.cycle()

main()
