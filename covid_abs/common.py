
import numpy as np

"""
Probability of each infection serverity by age

Source: Imperial College Covid-19 research team
"""

age_hospitalization_probs = [0.001, 0.003, 0.012, 0.032, 0.049, 0.102, 0.166, 0.243, 0.273 ]
age_severe_probs = [0.05, 0.05, 0.05, 0.05, 0.063, 0.122, 0.274, 0.432, 0.709 ]
age_death_probs = [0.002, 0.00006, 0.0003, 0.0008, 0.0015, 0.006, 0.022, 0.051, 0.093 ]

## Citar fontes

"""
Wealth distribution

By stratum, source: http://www.sdp.gov.co/sites/default/files/evolucion-balance-financiero_0.pdf
"""

lorenz_curve = [.041, .232, .359, .187, .091, .091]
share = np.min(lorenz_curve)
basic_income = np.array(lorenz_curve)/share
