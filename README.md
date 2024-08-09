# Thermodynamic-corrections-for-adsorption-energy-calculated-from-static-DFT-calculations
Python code accompanies the publication titled Density Functional Theory Calculations of Surface Thermochemistry in Al/CuO Thermite Reaction published in Phys. Rev. Mater. in 2024. The purpose of this code is to calculate the adsorption energy at finite temperature from the static adsorption energy of a chemical species and their frequency values


# README: Thermodynamic Correction for Adsorption Energy

# Overview

This Python script is designed to calculate the adsorption energy at finite temperatures, starting from the static adsorption energy obtained from Density Functional Theory (DFT) calculations. The script performs thermodynamic corrections, including vibrational, rotational, and translational corrections, to account for the effect of temperature on the adsorption energy of a chemical species on surfaces or porous materials.

# Features

- Vibrational Correction : Adjusts the energy for vibrational contributions using vibrational frequencies.
- Rotational Correction : Computes the rotational energy correction depending on whether the molecule is linear or non-linear.
- Translational Correction : Adds translational energy correction based on temperature.
- Energy Correction : Provides the corrected adsorption energy at a specified temperature.

# Prerequisites

- Python 3.x: Ensure Python 3.x is installed on your system.
- Numpy: The script uses the `numpy` library for numerical calculations. Install it using:

  pip install numpy


# Usage

1. Prepare Input Files: Create text files containing the vibrational frequencies (in cm-1) for the final state (surface + adsorbate), isolated molecule, and the surface.
   
2. Run the Script: Execute the script by running:

   python script_name.py


3. Provide Input Values: The script will prompt you for the following inputs:
   - File path containing the vibrational frequencies for the final state (surface + adsorbate).
   - File path containing the vibrational frequencies for the isolated molecule.
   - File path containing the vibrational frequencies for the surface.
   - Adsorption energy at 0 K (in eV).
   - Temperature (in Kelvin).
   - Whether the molecule is linear (yes/no).

4.  Output : The script will calculate and display the corrected adsorption energy at the specified temperature.

# Example

To use the script, you need to enter:
- `file_path_final.txt` for the final state frequencies.
- `file_path_isolated.txt` for the isolated molecule frequencies.
- `file_path_surface.txt` for the surface frequencies.
-  The adsorption energy in eV at 0 K.
-  The temperature in K.
- `yes` if the molecule is linear and no for nolinear.

# Contact

For questions or suggestions, please contact the author.


