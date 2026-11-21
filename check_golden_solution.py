"""
Numerical check of the golden solution and of the bronze-answer audit.
Run it to confirm every number quoted in the Markdown files.
"""

import numpy as np

m, k, b, F0 = 0.5, 50.0, 0.4, 10.0
w0 = np.sqrt(k / m)
gamma = b / (2 * m)


def amplitude(w, g=gamma, damping_factor=2.0):
    return (F0 / m) / np.sqrt((w0 ** 2 - w ** 2) ** 2 + (damping_factor * g * w) ** 2)


def phase(w):
    return np.arctan2(2 * gamma * w, w0 ** 2 - w ** 2)


# Golden solution
assert np.isclose(w0, 10.0)
assert np.isclose(gamma, 0.4)
assert np.isclose(amplitude(w0), 2.5)
assert np.isclose(phase(w0), np.pi / 2)
assert np.isclose(1 / gamma, 2.5)
assert np.isclose(amplitude(0.0), F0 / k)             # 0.2 m
assert np.isclose(phase(1e-9), 0.0, atol=1e-6)         # low-frequency phase
assert np.isclose(phase(1e6), np.pi, atol=1e-5)        # high-frequency phase
assert amplitude(1e6) < 1e-9                           # high-frequency amplitude
w_peak = np.sqrt(w0 ** 2 - 2 * gamma ** 2)
assert np.isclose(w_peak, 9.984, atol=1e-3) and amplitude(w_peak) > amplitude(w0)

# Why plain arctan is a trap: it gives ~0 (not pi) at high frequency
naive_high = np.arctan(2 * gamma * 1e6 / (w0 ** 2 - 1e6 ** 2))
assert abs(naive_high) < 1e-5

# Bronze answer: wrong gamma, but its amplitude at resonance is right by cancellation
gamma_b = b / m
assert np.isclose((F0 / m) / (gamma_b * w0), 2.5)
assert np.isclose(1 / gamma_b, 1.25) and not np.isclose(1 / gamma_b, 1 / gamma)

# Rubric arithmetic
assert 20 + 20 + 25 + 20 + 15 == 100
assert 10 + 10 + 12 + 10 + 0 == 42

print("All checks passed.")
