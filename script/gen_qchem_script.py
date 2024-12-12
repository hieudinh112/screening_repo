def generate_script(lattice_params, unitcell_data, rem_params):
    lattice_section = f"""
$lattice
{len(lattice_params)}
""" + "\n".join([" ".join(map(str, line)) for line in lattice_params]) + "\n$end"

    unitcell_section = f"""
$unitcell
RELATIVE
{unitcell_data['lattice_vectors']}
""" + "\n".join([" ".join(map(str, atom)) for atom in unitcell_data['atoms']]) + "\n$end"

    rem_section = "$rem\n" + "\n".join([f"{key} = {value}" for key, value in rem_params.items()]) + "\n$end"

    return f"{lattice_section}\n\n{unitcell_section}\n\n{rem_section}"

# Save to a file or print to the console
def save_script_to_file(filename, lattice_params, unitcell_data, rem_params):
    script = generate_script(lattice_params, unitcell_data, rem_params)
    with open(filename, "w") as f:
        f.write(script)

# # Example usage
lattice_params = [
    [0.000000000000E+00,   0.177775000000E+01,   0.177775000000E+01],
    [0.177775000000E+01,   0.000000000000E+00,   0.177775000000E+01],
    [0.177775000000E+01,   0.177775000000E+01,   0.000000000000E+00]
]

# Example usage
# lattice_params = [
#     [5.798338236, 0.0, 0.0],
#     [2.8991691180000005, 1.67383607070355, 4.734323344756501],
#     [2.8991691180000005, 5.02150821211065, 0.0]
# ]

unitcell_data = {
    "lattice_vectors": "0 1",
    "atoms": [
        ["C", 0.0, 0.0, 0.0],
        ["C", 0.888875, 0.888875, 0.888875]
    ]
}

# unitcell_data = {
#     "lattice_vectors": "0 1",
#     "atoms": [
#         ["Mg", 0.0, 0.0, 0.0],
#         ["O", 0.5, 0.5, 0.5]
#     ]
# }

rem_params = {
    "jobtype": "sp",
    "method": "pbe",
    "basis": "cc-pvqz",
    "aux_basis": "rimp2-cc-pvqz",
    "integral_direct": "true",
    "do_rij_bigmem": "false",
    "compact_diffuse_thresh": 2.0,
    "mp_mesh": "[1,1,1]",
    "omega_rs": 0.5,
    "fft_ng": 10,
    "aft_ng": 10,
    "scf_convergence": 7,
    "input_bohr": "false",
    "scf_algorithm": "gdm",
    "MAX_SCF_CYCLES": 500,
    "madelung": "false",
    "mem_total": 32000,
    "print_level": 10,
    "grid_type_xc": 2
}

input_path = "/n/home02/hieudinh/scr_work/basis_series/diamond/"

for i in range(1, 11):
    filename = input_path + f"diamond_ccpvqz_{i:02d}.in"

    rem_params["omega_rs"] = i / 10
    save_script_to_file(filename, lattice_params, unitcell_data, rem_params)
    print(f"Script saved to {filename}")

