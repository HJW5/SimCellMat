import numpy as np
import matplotlib.pyplot as plt

initial_mass = 1.0
degradation_rate = 0.02
days = 100

def sim_degradation(initial_mass, degradation_rate, days):
    time = np.arange(0, days + 1)
    mass = initial_mass * np.exp(-degradation_rate * time)
    return time, mass

def plot_degradation(time, mass, material_name="Unknown"):
    plt.figure(figsize=(8, 5))
    plt.plot(time, mass, label=material_name)
    plt.title(f"Degradation of {material_name}")
    plt.xlabel("Time (days)")
    plt.ylabel("Mass Remaining (g)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"plots/{material_name}_degradation.png")
    plt.show()
