class Material: 
  def __init__(self, name, degradation_rate, youngs_modulus, density, toxicity_threshold):
    self.name = name
    self.degradation_rate = degradation_rate # /day
    self.youngs_modulus = youngs_modulus # MPa
    self.density = density # g/cm
    self.toxicity_threshold = toxicity_threshold # %mass remaining
   
    def simulate(self, initial_mass=1.0, days=100):
        time, mass = sim_degradation(initial_mass, self.degradation_rate, days)
        return time, mass

    # Example materials
pla = Material("PLA", degradation_rate=0.02, youngs_modulus=2500, density=1.25, toxicity_threshold=0.3)
magnesium = Material("Magnesium", degradation_rate=0.05, youngs_modulus=45000, density=1.74, toxicity_threshold=0.4)

# Run and plot
for mat in [pla, magnesium]:
    t, m = mat.simulate()
    plot_degradation(t, m, material_name=mat.name)
