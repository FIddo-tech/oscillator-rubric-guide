# Oscillator Rubric and Reviewer Guide

A 100-point rubric and reviewer guide for grading AI answers to a driven, damped harmonic oscillator problem. It includes a reference solution, a flawed model answer with a graded audit, and a step-by-step guide for reviewers.

## What is in here

- problem_statement.md: the problem the AI model must solve
- golden_solution.md: the reference solution (omega_0 = 10 rad/s, gamma = 0.4 1/s, A(omega_0) = 2.5 m, tau = 2.5 s)
- bronze_solution_trap.md: a flawed answer whose errors partly cancel, with a graded audit (42/100)
- grading_rubric.md: five weighted criteria and two critical-failure caps
- reviewer_onboarding_guide.md: the scoring procedure for new reviewers
- check_golden_solution.py: numerical check of every number quoted above

## Why the bronze answer matters

Its amplitude at resonance is numerically correct because a wrong damping definition cancels a missing factor of 2. A reviewer who only checks the final number would miss both errors. The guide teaches reviewers to check each formula, not just the result.

## Run the check

    pip install -r requirements.txt
    python check_golden_solution.py
