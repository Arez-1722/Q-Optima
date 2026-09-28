Q-optima

Quantum-inspired metaheuristic framework for dynamic vehicle routing under changing traffic conditions.

SIH 2026 · Quantum Technology Vertical · PS 1 (SIH26137) — Quantum-Inspired Intelligent Traffic Route Optimization in Transportation Systems Using Metaheuristic Optimization (Org: Egreen Quanta)

Status: work in progress. Only QACO has been developed so far, and it is not yet complete. All other algorithms and the benchmarking suite are not started.

Overview

Large-scale Vehicle Routing Problems (VRP) are NP-hard, and classical solvers struggle as network size and traffic dynamics grow. Real quantum hardware can't yet handle these instances, so Q-optima embeds quantum-mechanical ideas (superposition, interference, tunneling) into classical metaheuristics to get stronger global search and better exploration/exploitation balance.

The road network is modelled as a weighted graph whose edge weights change over time (simulated real-time traffic). Q-optima generates near-optimal routes on it and benchmarks them against conventional metaheuristics and exact methods.

Objectives
Solve large-scale VRP and shortest-path problems with a quantum-inspired metaheuristic framework.
Minimize total travel time, distance, and congestion.
Improve convergence speed and solution quality vs. classical algorithms at lower computational cost.
Demonstrate scalability for smart-city logistics and intelligent transportation systems.
Algorithms
Algorithm	Role	Status
Dynamic Interference-Tunneling QACO	Quantum-inspired Ant Colony Optimization: interference-based route sampling + tunneling-inspired nonlocal search	In development — partially implemented (notebook V2)
QPSO (Quantum Particle Swarm Optimization)	Required by the problem statement	Not started
Classical ACO	Baseline	Not started
Other metaheuristics (e.g. GA, PSO, SA)	Baselines	Not started
Exact solver (e.g. OR-Tools / MILP)	Optimality reference on small instances	Not started
