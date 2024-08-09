import numpy as np

def read_frequencies_from_file(file_path):
    """
    Read vibrational frequencies from a file.
    
    :param file_path: Path to the file containing vibrational frequencies
    :return: List of vibrational frequencies in cm^-1
    """
    frequencies = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 1 and parts[1].replace('.','',1).isdigit():
                frequency = float(parts[1])
                frequencies.append(frequency)
    return frequencies

def vibrational_correction(frequencies, temperature, R):
    """
    Calculate vibrational correction to energy.
    
    :param frequencies: List of vibrational frequencies in cm^-1
    :param temperature: Temperature in Kelvin
    :param R: Gas constant in eV/K
    :return: Vibrational correction in eV
    """
    h = 4.135667696e-15  # Planck constant in eV·s
    c = 2.99792458e10    # Speed of light in cm/s
    k = 8.617333262145e-5  # Boltzmann constant in eV/K
    
    vibrational_energy = 0.0
    for freq in frequencies:
        freq_in_hz = freq * c
        vibrational_energy += R * (h * freq_in_hz / (2 * k)) + (R / k) * (h * freq_in_hz) / (np.exp(h * freq_in_hz / (k * temperature)) - 1)
    
    return vibrational_energy

def rotational_correction(temperature, is_linear, R):
    """
    Calculate rotational correction to energy.
    
    :param temperature: Temperature in Kelvin
    :param is_linear: Boolean indicating if the molecule is linear
    :param R: Gas constant in eV/K
    :return: Rotational correction in eV
    """
    if is_linear:
        return R * temperature
    else:
        return 1.5 * R * temperature

def translational_correction(temperature, R):
    """
    Calculate translational correction to energy.
    
    :param temperature: Temperature in Kelvin
    :param R: Gas constant in eV/K
    :return: Translational correction in eV
    """
    return 1.5 * R * temperature

def correct_adsorption_energy(E0K, temperature, final_frequencies, isolated_frequencies, surface_frequencies, is_linear):
    """
    Correct the adsorption energy from 0 K to a finite temperature.
    
    :param E0K: Adsorption energy at 0 K in eV
    :param temperature: Temperature in Kelvin
    :param final_frequencies: List of vibrational frequencies of the final state (surface + adsorbat) in cm^-1
    :param isolated_frequencies: List of vibrational frequencies of the isolated molecule in cm^-1
    :param surface_frequencies: List of vibrational frequencies of the surface in cm^-1
    :param is_linear: Boolean indicating if the molecule is linear
    :return: Corrected adsorption energy in eV
    """
    R = 8.31446261815324e-5  # Gas constant in eV/K
    
    # Calculate vibrational correction for the final state (surface + adsorbat)
    vibrational_corr_final = vibrational_correction(final_frequencies, temperature, R)
    print(f"Calculated Vibrational Correction for Final State: {vibrational_corr_final:.3f} eV")
    
    # Calculate vibrational correction for the isolated molecule
    vibrational_corr_isolated = vibrational_correction(isolated_frequencies, temperature, R)
    print(f"Calculated Vibrational Correction for Isolated Molecule: {vibrational_corr_isolated:.3f} eV")
    
    # Calculate vibrational correction for the surface
    vibrational_corr_surface = vibrational_correction(surface_frequencies, temperature, R)
    print(f"Calculated Vibrational Correction for Surface: {vibrational_corr_surface:.3f} eV")
    
    # Calculate rotational correction
    rot_corr = rotational_correction(temperature, is_linear, R)
    print(f"Calculated Rotational Correction at {temperature} K: {rot_corr:.3f} eV")
    
    # Calculate translational correction
    trans_corr = translational_correction(temperature, R)
    print(f"Calculated Translational Correction at {temperature} K: {trans_corr:.3f} eV")
    
    # Correct adsorption energy
    corrected_energy = (E0K + vibrational_corr_final - 
                        (vibrational_corr_isolated + vibrational_corr_surface + trans_corr + rot_corr))
    return corrected_energy

def main():
    file_path_final = input("Enter the path to the file containing vibrational frequencies of the final state (surface + adsorbat): ")
    final_frequencies = read_frequencies_from_file(file_path_final)
    
    file_path_isolated = input("Enter the path to the file containing vibrational frequencies of the isolated molecule: ")
    isolated_frequencies = read_frequencies_from_file(file_path_isolated)
    
    file_path_surface = input("Enter the path to the file containing vibrational frequencies of the surface: ")
    surface_frequencies = read_frequencies_from_file(file_path_surface)
    
    E0K = float(input("Enter the adsorption energy at 0 K in eV: "))
    temperature = float(input("Enter the temperature in Kelvin: "))
    is_linear = input("Is the molecule linear (yes/no)? ").strip().lower() == 'yes'
    
    # Correct adsorption energy
    corrected_energy = correct_adsorption_energy(E0K, temperature, final_frequencies, isolated_frequencies, surface_frequencies, is_linear)
    print(f"Corrected adsorption energy at {temperature} K: {corrected_energy:.3f} eV")

if __name__ == "__main__":
    main()

