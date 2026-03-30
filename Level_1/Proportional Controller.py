import numpy as np
import matplotlib.pyplot as plt

def proportional_controller(Kp, dt, total_time, setpoint, tank_volume):

    volumes = []
    times = np.arange(0, total_time, dt)

    for _ in times:
        error = setpoint - tank_volume

        inflow = Kp * error

        outflow = 0

        tank_volume += (inflow - outflow) * dt

        tank_volume = max(0, tank_volume)

        volumes.append(tank_volume)
    return volumes, times, setpoint

def plot_results(volumes, times, setpoint):
    plt.figure(figsize=(10, 5))
    plt.plot(times, volumes, label='Tank 1 (Actual)', color='blue', linewidth=3)
    plt.axhline(y=setpoint, color='red', linestyle='-', label='Setpoint')
    plt.xlabel('Time [s]')
    plt.ylabel('Tank volume [m^3]')
    plt.title('P-Controller Simulation')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():

    dt = 0.1
    total_time = 5000
    setpoint = 70
    Kp = 0.5
    tank_volume = 30

    volumes, times, setpoint = proportional_controller(Kp, dt, total_time, setpoint, tank_volume)

    plot_results(volumes, times, setpoint)


if __name__ == "__main__":
    main()
