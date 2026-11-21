# Golden solution

## Equation

m x'' + b x' + k x = F0 cos(omega t), which in standard form is
x'' + 2 gamma x' + omega_0^2 x = (F0 / m) cos(omega t).

## Parameters

- omega_0 = sqrt(k / m) = sqrt(50 / 0.5) = 10 rad/s
- gamma = b / (2 m) = 0.4 / (2 x 0.5) = 0.4 1/s
- F0 / m = 20 m/s^2

## Steady state

Write x_p = Re( X e^(i omega t) ). Then X = (F0 / m) / [ (omega_0^2 - omega^2) + i (2 gamma omega) ].

    A(omega) = |X| = (F0 / m) / sqrt( (omega_0^2 - omega^2)^2 + (2 gamma omega)^2 )

    delta(omega) = atan2( 2 gamma omega, omega_0^2 - omega^2 ),  with delta in [0, pi]

Use atan2, not plain arctan. Plain arctan returns a negative angle for omega > omega_0 and gives the wrong high-frequency limit.

## At omega = omega_0

A = (F0 / m) / (2 gamma omega_0) = 20 / (2 x 0.4 x 10) = 2.5 m, and delta = pi / 2.

The exact amplitude peak is slightly lower in frequency, at omega = sqrt(omega_0^2 - 2 gamma^2), about 9.984 rad/s, where A is about 2.502 m.

## Transient decay

tau = 1 / gamma = 2.5 s.

## Limits

- omega -> 0: A -> F0 / k = 0.2 m and delta -> 0. The spring dominates and the motion follows the force.
- omega -> infinity: A -> 0 (as 1 / omega^2) and delta -> pi. The mass's inertia dominates, so the motion is opposite in direction to the force.
