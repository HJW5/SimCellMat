from material import Material
from degradation_model import plot_degradation

# Define materials
pla = Material("PLA", degradation_rate=0.02, youngs_modulus=2500, density=1.25, toxicity_threshold=0.3)
mg = Material("Magnesium", degradation_rate=0.05, youngs_modulus=45000, density=1.74, toxicity_threshold=0.4)

# Run simulations
time, mass = pla.simulate()
plot_degradation(time, mass, material_name=pla.name)
