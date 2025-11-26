# PhD Defense Presentation

## Title
**Embedded Convex Optimization for Control of Synchronous Machines**

## Author
**Hiba HOUMSI**

## Supervisors
- Paolo Massioni
- Federico Bribiesca-Argomedo
- Romain Delpoux

## Institution
Ampère Laboratory, INSA Lyon, France

## Abstract

This PhD defense presents advanced control strategies for Permanent Magnet Synchronous Machines (PMSM) with a focus on embedded implementation on low-cost microcontrollers. The work addresses three main research areas:

## Problem Statement

Traditional control approaches rely on offline computation on powerful computers. This work proposes a novel **hybrid online-offline approach** where optimization solvers run directly on the embedded microcontroller.

![Embedded Approach](pictures/online_offline2.eps)
*Proposed embedded approach: optimization directly on microcontroller*

## Research Contributions

### Part 1: Optimal Torque Control
- Novel convex formulation of the optimal torque control (OTC) problem
- Change of variable approach to eliminate bilinear constraints
- Convexity proof via Sum-of-Squares (SoS) programming
- Real-time interior-point solver for embedded implementation
- Experimental validation on IPMSM test bench

**Visual illustration:** The presentation includes an animated sequence showing how the optimal current trajectory evolves across different torque and speed operating points.
- Animation frames: `eps_frames_torque_cost_speed_optimal/frame_000` to `frame_014`
- Illustrates voltage ellipse, current circle, and torque hyperbola constraints

![Solver Performance](pictures/expe_idq_solver.eps)
*Real-time solver performance: optimal current references tracking*

### Part 2: Embedded Control Synthesis
- Pole-constrained H₂ controller synthesis for current regulation
- Embedded LMI solver running as idle task on microcontroller
- Fast computation time (~0.3s) enabling online controller tuning
- Guaranteed transient specifications (decay rate, damping)
- Experimental validation on dsPIC33AK512MC510

**Visual illustration:** The control architecture shows the complete embedded system with high-priority control loops and idle-task LMI solver.

![Embedded Control Architecture](pictures/combined.eps)
*Complete embedded control system showing: control loops, trajectory generation, and embedded synthesis*

![Test Bench](pictures/PMSM_test_bench.eps)
*CTRL-ELEC experimental platform: IPMSM motor, inverter, and dsPIC33AK512 microcontroller*

### Part 3: Linear Parameter-Varying (LPV) Control
- Linearization-free control approach
- Speed-dependent gain scheduling with Lyapunov stability certificates
- Improved noise rejection compared to PI control
- LMI-based synthesis for robust performance
- Experimental validation showing superior tracking and disturbance rejection

**Visual illustration:** Speed-dependent gain scheduling with superior noise rejection compared to PI control.

![LPV Control Architecture](pictures/ControlFOCLPV.eps)
*LPV control structure with speed-dependent gain scheduling K(ω)*

## Key Contributions

1. **Convex formulation** of the non-convex optimal torque control problem
2. **Embedded optimization solvers** running on industrial microcontrollers
3. **Online control synthesis** enabling adaptive performance tuning
4. **Experimental validation** on industrial motor drive platforms

## Overall System Architecture

The complete embedded control system integrates all three contributions:

![Complete System Diagram](pictures/AdvancedControl.eps)
*Overall control architecture showing the interaction between trajectory generation (Part 1), feedback control (Part 2), and embedded synthesis (Part 2)*

The system operates at multiple priority levels:
- **High priority (~20 kHz):** Current control loop with optimized gains
- **Lower priority (~1 kHz):** Optimal trajectory generation solving OTC problem
- **Idle task:** Embedded LMI solver for online controller adaptation

## Applications

The proposed methods are applicable to:
- Automotive propulsion systems (electric vehicles)
- Robotic actuators
- Wind turbines and power generation
- Industrial motor drives requiring high performance and low cost

## Experimental Platform

All experimental validations were performed on the **CTRL-ELEC platform** at Ampère Laboratory.

**Platform website:** [https://www.ctrl-elec.fr](https://www.ctrl-elec.fr)

The platform provides:
- High-performance PMSM test benches (SPMSM and IPMSM)
- Industrial-grade microcontrollers (Microchip dsPIC33 series)
- Rapid Control Prototyping tools
- Open-source experimental approach

## Files Structure

### Main Files
- `defense_presentation.tex` - Main LaTeX file
- `defense_presentation.pdf` - Compiled presentation

### Section Files
- `introduction.tex` - Problem statement and motivation
- `section1_optimal_torque_control.tex` - Part 1: OTC formulation and solver
- `section2_embedded_control_synthesis.tex` - Part 2: Embedded LMI solver
- `section3_lpv_control.tex` - Part 3: LPV control design
- `section4_conclusion.tex` - Summary of contributions
- `section5_perspectives.tex` - Future research directions and publications

### Resources
- `pictures/` - Figures, diagrams, and experimental results
- `eps_frames_*/` - Animation frames for voltage/torque constraints

## Compilation

To compile the presentation, use the following LaTeX → DVI → PS → PDF workflow:

```bash
latex defense_presentation.tex
dvips defense_presentation.dvi -o defense_presentation.ps
ps2pdf defense_presentation.ps defense_presentation.pdf
```

Or use a single command chain:

```bash
latex defense_presentation.tex && dvips defense_presentation.dvi -o defense_presentation.ps && ps2pdf defense_presentation.ps defense_presentation.pdf
```

**Note:** This compilation recipe is required for:
- Proper handling of EPS figures with PSfrag replacements
- Animation frames in the presentation
- Compatibility with the psfrag package for mathematical notation overlays

**Required LaTeX packages:** beamer, tikz, psfrag, animate, graphicx, epstopdf, and standard math packages.

## Publications

The work resulted in multiple conference and journal publications:
- IEEE ICCAD 2023: KKT approach to field-weakening
- IEEE VPPC 2023: Embedded controller optimization
- ECC 2025: Robust pole-constrained H₂ controller
- IAS 2025: Real-time interior-point solver for OTC

## Contact

**Email:** hiba.houmsi@insa-lyon.fr

**CTRL-ELEC Platform:** [https://www.ctrl-elec.fr](https://www.ctrl-elec.fr)

## Affiliations

- Ampère Laboratory (UMR CNRS 5005)
- INSA Lyon
- Université de Lyon
- CNRS

---

*PhD Defense Date: November 14, 2025*
