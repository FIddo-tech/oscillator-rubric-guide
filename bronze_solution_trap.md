# Flawed model answer ("bronze") and reviewer audit

## Model answer (contains subtle errors)

"The natural frequency is omega_0 = sqrt(k / m) = 10 rad/s. The damping factor is gamma = b / m = 0.8 1/s. The amplitude is A(omega) = (F0 / m) / sqrt( (omega_0^2 - omega^2)^2 + (gamma omega)^2 ). At resonance A(10) = 20 / (0.8 x 10) = 2.5 m. The phase is delta = arctan[ gamma omega / (omega_0^2 - omega^2) ]. As omega -> infinity the argument tends to 0, so delta -> 0: the force drives the system in phase. The transient decays with tau = 1 / gamma = 1.25 s."

## Reviewer audit

- C1 (10/20): uses gamma = b / m, not b / (2 m) as the standard form requires.
- C2 (10/20): balances forces but never separates the transient from the steady state.
- C3 (12/25): the amplitude is numerically right only because the wrong gamma cancels the missing factor of 2, so the two errors hide each other. The phase uses principal-value arctan with no quadrant handling.
- C4 (10/20): the omega -> 0 limit is correct. The claim delta -> 0 as omega -> infinity is wrong (it should be pi).
- C5 (0/15): tau = 1.25 s is wrong (it should be 2.5 s), and Trigger B fired.

Final score: 42/100 (fail). Trigger B caps the score at 50, so the cap does not change it.
