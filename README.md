# Tennessee Eastman Process — Cyber-Physical Attack & Fault Dataset

## Overview

This dataset is generated using the **Revised Tennessee Eastman Process (TEP)** simulator running in MATLAB/Simulink. It is designed for research in anomaly detection, fault diagnosis, and cyber-physical attack detection in industrial control systems.

The dataset contains **three distinct anomaly scenarios**:

| # | Type | Target | Description |
|---|------|--------|-------------|
| SC1 | Cyber Attack | XMEAS(14) — Separator Underflow | Sensor value frozen at a fixed manipulated value |
| SC2 | Cyber Attack | XMEAS(7) — Reactor Pressure | Damped sinusoidal signal injected into sensor–PLC line |
| IDV(1) | Process Fault | Stream 4 composition | Step change in A/C feed ratio with constant B composition |

> **Attack scenario:** Both attacks target the **sensor–PLC communication channel**. The measured value reported by the sensor is intercepted and manipulated before reaching the PLC controller. The controller, therefore, receives a falsified signal and responds accordingly — making the attack stealthy and physically consequential.

---

## Dataset Structure

Each dataset has the shape **`10001 × 85`**:

- **73 measured variables** (XMEAS 1–41 from original TEP + extended variables per the revised model)
- **12 manipulated variables** (XMV 1–12)

For a full description of all variables, refer to the Revised TEP paper:

> Bathelt, A., Ricker, N. L., & Jelali, M. (2015). Revision of the Tennessee Eastman Process Model. *IFAC-PapersOnLine*. DOI: 10.1016/j.ifacol.2015.08.199

> **Sampling interval:** `Δt = 0.01 h` (36 seconds per sample) over a 100-hour simulation window.

---

## Attack Scenarios

### SC1 — Integrity Attack: Sensor Freeze on XMEAS(14)

**Target sensor:** XMEAS(14) — Product Separator Underflow (`m³/hr`)  
**Baseline value:** 25 m³/hr  
**Attack value:** 23 m³/hr

The attacker freezes the separator underflow reading at a fixed value, causing the PLC to receive a static signal instead of the real process measurement. Both the onset and recovery of the attack are **step changes**.
```
a(t) = A  for t₀ < t < t_end
a(t) = 0   otherwise
```
The manipulated signal sent to the PLC is defined as:

```
y* = y_m + a(t)
```

where ```y_m``` is the true sensor measurement, ```y*``` is the falsified signal delivered to the PLC, ```t₀``` is the attack start time, and ```t_end``` is the recovery time, and ```A``` is the step change. The effective result is that the controller receives a constant value for the full duration.

**Process consequence:** The separator and stripper levels drift from their setpoints, as the controller adjust the underflow valve due the false reading. The resulting behavior is superficially and cause false alarm in Stipper unit which making it detection .

---

### SC2 — Integrity Attack: Damped Sinusoidal Injection on XMEAS(7)

**Target sensor:** XMEAS(7) — Reactor Pressure (`kPa gauge`)

The attacker injects a **damped sinusoidal wave** into the sensor–PLC communication line for reactor pressure. The attack signal is:

```
a(t) = exp(-αt) · A · sin(ωt)
```

where:
- `A` is the amplitude of the injected wave,
- `α` is the damping coefficient,
- `ω` is the wave frequency.

**Rationale for the damped sinusoidal form:**  
The exponential damping term `exp{(-αt}` is intentionally chosen to mimic the natural response envelope of a first- or second-order process transfer function following a step or impulse disturbance. Real industrial processes exhibit transient responses that decay over time due to feedback control action. By shaping the attack signal in this way, the injected attack appears consistent with normal closed-loop process dynamics — making it significantly harder to distinguish from legitimate transient behavior using model-based or statistical detectors.

The parameters `A` and `ω` are tuned such that:
1. The reactor pressure remains within operational safety limits throughout the attack (no emergency shutdown is triggered),
2. The peak pressure deviation is comparable in magnitude to that observed under the IDV(1) process fault, ensuring the attack is realistic and challenging.

---

### IDV(1) — Process Fault: A/C Feed Ratio Step Change

**Fault type:** Step disturbance in Stream 4 feed composition  

IDV(1) is the most widely studied fault in the TEP literature and introduces a **negative step change in the A/C molar ratio** of the combined A+C feed (Stream 4) while holding the B (inert) composition constant. This shifts the reactant balance entering the separator, propagating through reactor temperature, pressure, and product quality loops.

This fault serves as a **baseline process anomaly** for comparison against the cyber attack scenarios, given its well-characterized signature in the literature.

---

## Simulation Scenarios

### Training Dataset

Total duration: **100 hours** | Shape: `10001 × 85`

```
 0 h – 30 h   →  Normal operation
30 h – 32 h   →  Attack SC1
32 h – 45 h   →  Normal operation
45 h – 50 h   →  Process fault IDV(1)
50 h – 70 h   →  Normal operation
70 h – 90 h   →  Attack SC2  (damped sinusoidal injection on reactor pressure)
90 h – 100 h  →  Normal operation
```

---

### Testing Dataset

Total duration: **100 hours** | Shape: `10001 × 85`

```
 0 h – 10 h   →  Normal operation
10 h – 40 h   →  Attack SC2  (damped sinusoidal injection on reactor pressure)
40 h – 50 h   →  Normal operation
50 h – 52 h   →  Attack SC1  (XMEAS14 frozen, step onset & recovery)
52 h – 70 h   →  Normal operation
70 h – 80 h   →  Process fault IDV(1)
80 h – 100 h  →  Normal operation
```

> The test set deliberately **reverses the anomaly order** and uses a different fault/attack mix compared to training, to evaluate the generalization capability of detection models.

---

## Simulator Configuration

| Parameter | Value |
|---|---|
| Base simulator | Revised TEP (Bathelt et al., 2015) |
| Operating mode | Mode 1 (50/50 G/H product split) |
| Noise | Enabled (deterministic seed — fixed across runs) |
| Sampling interval | 0.01 h (36 s) |
| Simulation duration | 100 h per dataset |
| Control strategy | Decentralized multiloop (Ricker, 1996) |

### Nominal Setpoints (Mode 1)

| Setpoint | Value | Unit |
|---|---|---|
| Production Rate | 22.89 | m³/hr |
| Stripper Level | 50 | % |
| Separator Level | 50 | % |
| Reactor Level | 75 | % |
| Reactor Pressure | 2800 | kPa gauge |
| Mole % G (product) | 53.8 | mol% |
| Reactor Temperature | 122.9 | °C |
| Recycle Valve | 0 (closed) | % |
| Steam Valve | 0 (closed) | % |
| Agitator Speed | 100 (max) | % |

---

## Visualization

To plot any process variable over time against the anomaly timeline, open and run:

```
training_dataset.ipynb
```

The notebook provides an interactive interface to select and visualize any of the 85 variables across the full simulation horizon, with anomaly intervals highlighted.

---

## References

- Downs, J. J., & Vogel, E. F. (1993). A plant-wide industrial process control problem. *Computers & Chemical Engineering*, 17(3), 245–255.
- Bathelt, A., Ricker, N. L., & Jelali, M. (2015). Revision of the Tennessee Eastman Process Model. *IFAC-PapersOnLine*. DOI: 10.1016/j.ifacol.2015.08.199
- Ricker, N. L. (1996). Decentralized control of the Tennessee Eastman Challenge Process. *Journal of Process Control*, 6(4), 205–221.
