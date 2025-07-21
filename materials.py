class Material:
    def __init__(self, name, degradation_rate, youngs_modulus, density, toxicity_threshold):
        self.name = name
        self.degradation_rate = degradation_rate  # /day
        self.youngs_modulus = youngs_modulus     # MPa
        self.density = density                   # g/cm³
        self.toxicity_threshold = toxicity_threshold  # mg/L

# Predefined materials library
MATERIAL_LIBRARY = {
    "PLA": Material(
        name="PLA",
        degradation_rate=0.02,
        youngs_modulus=3500,
        density=1.25,
        toxicity_threshold=50
    ),
    "Mg": Material(
        name="Magnesium",
        degradation_rate=0.08,
        youngs_modulus=45000,
        density=1.74,
        toxicity_threshold=5
    ),
    "PCL": Material(
        name="Polycaprolactone",
        degradation_rate=0.015,
        youngs_modulus=400,
        density=1.145,
        toxicity_threshold=100
    )
}

def get_material(name):
    """Safely retrieve material with error handling"""
    try:
        return MATERIAL_LIBRARY[name.upper()]
    except KeyError:
        raise ValueError(f"Material '{name}' not found. Available: {list(MATERIAL_LIBRARY.keys())}")
