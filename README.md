# StatisticsOfDisorderSystem
We have collected some commonly used functions when studying Anderson localization and quasi-periodic localization. \
These functions can be divided into five parts: \
(a) plot. (b) statistics of the eigenstates. (c) statistics of the eigenvalues. (d) statistics of the dynamics. (e) typical Hamiltonians.
 
## Plot
1. (EVIprPlot) :we use the code (EVIprPlot) to plot this figure. 
![image](EVIprPlotExample1.jpg)

## Statistics of the eigenstates.
1.（Ipr）： calculate the Ipr for a single eigenstate.\
2.（Localizationlength）： given an eigenstate and calculate the localization length.\
3. (scalingexponent) : get the scaling exponent by the system size and IPR data.  

## Statistics of the eigenvalues
1. (Energyratio) :calculate the energy level sacing ratio.\
2. (Boxcounting) : calculate the spectral fractal dimendion.

## Statistics of the dynamics
1. (x2) : claculate $<x^2>$

## Typical Hamiltonians
1. (getGAA) :get the single particle Hamiltonian of the Generalized AA model(a quasiperiodic system with multifractal states.)

## Running the utilities

The `.m` files are independent MATLAB functions. Add this repository's root
to the MATLAB path; there is no single batch experiment entry point. For example:

```matlab
addpath(pwd)
H = getGAA(34, 0.5, 1, 0);
[states, energies] = eig(H, 'vector');
ipr = Ipr(states(:, 1));
```

`BoxCounting.py` is the Python utility (the filename is case-sensitive).
Install its dependencies and run the regression tests from the repository root:

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests
python BoxCounting.py
```

`BoxCountingE(E, N)` returns exactly N counts and N left edges. It uses uniform
bins over the spectrum's range, including the maximum in the last bin, and
accepts unsorted spectra. `GetNb(counts, q)` sums powers over occupied boxes;
q=0 gives the number of occupied boxes. Its historical default q=0.001 remains
unchanged. These counts are not a fitted fractal dimension by themselves:
the scale sequence and fitting procedure must be chosen for the experiment.

## Reuse and limits

The original `EVIprPlot.m` and `Ipr.m` also occur in the public
[Group-meeting Unbounded example](https://github.com/hustZhangYu/Group-meeting/tree/main/20230316/Unbounded).
The copies remain independent so this utility repository needs no external
checkout to run. `Localizationlength.m` is a historical estimator: its
coordinate handling and choice of fitting tail require review before new
quantitative use. The Python tests cover box occupancy bookkeeping, not the
scientific validity of the other estimators.

