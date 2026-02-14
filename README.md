# sensors_equations
*this project was developed in 2022*

Estimate phone orientation (altitude and azimuth) from raw sensor vectors and evaluate the error range against known sky-object references.

## Project Overview

This repository contains iterative experiments for sensor-based orientation estimation.

- `sesors_eq.py` -> first azimuth experiments from cross/dot products.
- `sesors_eq2.py` to `sesors_eq5.2.py` -> later variants adding frame rotation, tilt handling, and test readings.
- `1.dart` / `darts.txt` -> Dart port of the core altitude/azimuth idea.
- `test acc/error_range.ipynb` -> analysis notebook for sensor error behavior.
- `test acc/output.csv` -> logged measurements (reference vs phone-estimated values).
- `test acc/results/` -> exported result plots.

## Sensor Model (high level)

Inputs:
- `H`: gravity/acceleration vector (used for altitude and tilt estimation).
- `G`: magnetic field vector (used for azimuth after frame correction).

Typical flow used by the scripts:
1. Estimate altitude from `atan2(Hz, Hy)`.
2. Build rotation matrices and rotate vectors into a horizontal frame.
3. Estimate azimuth from rotated magnetic components using `atan2`.
4. Compare against reference azimuth/altitude values.

## Data Columns (`test acc/output.csv`)

Each row contains:
- `Name`
- `alt`, `az` (reference values)
- `time`
- `phone alt`, `phone az` (estimated by phone/sensor model)
- `phone time`

Derived in notebook:
- `alt error = alt - phone alt`
- `az error = az - phone az`
- lag-time based and grouped error views

## Results Plots

### 1) Altitude error by sample index

![Altitude error by index](test%20acc/results/output.png)

### 2) Alt/Az error scatter by object category

![Object-wise error scatter](test%20acc/results/output2.png)

### 3) Azimuth error by sample index

![Azimuth error by index](test%20acc/results/output3.png)

### 4) Altitude error vs azimuth error

![Altitude vs azimuth error](test%20acc/results/output4.png)

### 5) Mean error comparison across selected objects

![Mean errors by object](test%20acc/results/output5.png)

## Run

### Python script experiments

```bash
python sesors_eq5.2.py
```

You can also run any of the other `sesors_eq*.py` files directly.

### Notebook analysis

```bash
jupyter notebook "test acc/error_range.ipynb"
```

## Requirements

- Python 3.x
- `numpy`
- `pandas`
- `matplotlib`
- `jupyter`

Install example:

```bash
pip install numpy pandas matplotlib jupyter
```

## Notes

- File names use the existing spelling `sesors_eq*` (kept as-is).
- For a static report, see `test acc/error_range.pdf`.
