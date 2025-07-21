class Material: 
  def __init__(self, name, degradation_rate, youngs_modulus, density, toxicity_threshold):
    self.name = name
    self.degradation_rate = degradation_rate # /day
    self.youngs_modulus = youngs_modulus # MPa
    self.density = density # g/cm
