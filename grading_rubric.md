# Grading rubric (100 points)

| ID | Dimension | Max | Scoring |
|---|---|---|---|
| C1 | Equation, parameters and units | 20 | 20: correct ODE with units and gamma = b / (2 m). 10: minor parameter or unit error (for example gamma = b / m). 0: wrong order or signs. |
| C2 | Solution decomposition | 20 | 20: clearly separates the transient x_h and the steady state x_p. 10: mentions both but confuses them or never separates them. 0: drops the homogeneous part without justification. |
| C3 | Amplitude and phase | 25 | 25: correct A(omega) and delta(omega) with the correct quadrant (atan2 or equivalent). 12: correct amplitude but a phase quadrant error, or a missing factor 2 in the damping term. 0: wrong form. |
| C4 | Limiting cases | 20 | 20: both limits correct with physical interpretation (0.2 m and delta -> 0; A -> 0 and delta -> pi). 10: one limit correct, or no interpretation. 0: both wrong. |
| C5 | Transient time and consistency | 15 | 15: tau = 1 / gamma = 2.5 s and no contradictions. 0: wrong tau or a trigger fired. |

## Critical failure triggers (score caps)

- Trigger A: claims the amplitude grows without bound at omega = omega_0 although b > 0. Cap at 40/100.
- Trigger B: claims delta -> 0 at high driving frequency (quadrant or branch error). Cap at 50/100.
