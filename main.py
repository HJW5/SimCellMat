import numpy as np
from degradation_model import sim_degradation, simulate_material, plot_degradation
from materials import get_material  # For direct access if needed

def main():
    """Command-line interface for degradation simulation"""
    print("🌱 Biomaterial Degradation Simulator")
    print("Available materials: PLA, Mg, PCL")  # Update with your materials
    
    try:
        # Example 1: Simple preset simulation
        print("\nRunning preset simulation for PLA...")
        time, mass = sim_degradation(
            initial_mass=1.0,
            degradation_rate=0.02,  # PLA's rate
            days=100
        )
        plot_degradation(time, mass, "PLA (Preset)")
        
        # Example 2: Material database simulation
        print("\nRunning database simulation for Mg...")
        time, mass, material, warning = simulate_material("Mg", days=150)
        print(f"Material: {material.name} | {warning}")
        plot_degradation(time, mass, material.name)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
