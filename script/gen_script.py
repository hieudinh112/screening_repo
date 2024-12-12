

def generate_slurm_script(job_name, output_file, nodes, ntasks, time, partition, command):
    slurm_script = f"""
#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --output={output_file}
#SBATCH --nodes={nodes}
#SBATCH --cpus-per-task={ntasks}
#SBATCH --time={time}
#SBATCH -o {job_name}_%j.out
#SBATCH -e {job_name}_%j.err
#SBATCH --mail-type=END
#SBATCH --mail-user=hieudinh@g.harvard.edu
#SBATCH --partition={partition}

module purge
module load gmp/6.3.0-fasrc01
module load mpc/1.3.1-fasrc01
module load mpfr/4.2.1-fasrc01
module load intel/24.0.1-fasrc01 intel-mkl/24.0.1-fasrc01 intelmpi/2021.11-fasrc01
module load cmake/3.28.3-fasrc01
module load Mambaforge/23.11.0-fasrc01
module load python/3.10.13-fasrc01

{command}

printf "... Done with the calculation..."
        """
    return slurm_script

def save_slurm_to_file(slurm_filename, job_name, output_file, nodes, ntasks, time, partition, command):
    slurm_script = generate_slurm_script(job_name, output_file, nodes, ntasks, time, partition, command)
    with open(slurm_filename, "w") as f:
        f.write(slurm_script)

# Example usage for SLURM script, we generate the job for different input files
for i in range(1, 11):

    # Configure of the cluster
    job_name = f"diamond_ccpvqz_0{i}"
    output_file = f"diamond_ccpvqz_0{i}.out"
    nodes = 1
    ntasks = 32
    time = "1:00:00"
    partition = "shared"

    # input file

    # output written converged result
    infile_diamond = f"/n/home02/hieudinh/scr_work/basis_series/diamond/diamond_ccpvqz_{i:02d}.in"
    outfile_diamond = f"/n/home02/hieudinh/scr_work/basis_series/diamond/converged_data/diamond_ccpvqz_{i:02d}_converged.mat"
    # infile_mgo = f"/n/home02/hieudinh/scr_work/omega_series/mgo/mgo_ccpvdz_{i:02d}.in"
    # outfile_mgo = f"/n/home02/hieudinh/scr_work/omega_series/mgo/converged_data/mgo_ccpvdz_{i:02d}_converged.mat"

    command = f"/n/holylabs/LABS/joonholee_lab/Users/hieudinh/qcpbc_jk_lowmem/build/libpbc/tests/pbc_screening_test {infile_diamond} {outfile_diamond}"
    # command = f"/n/holylabs/LABS/joonholee_lab/Users/hieudinh/qcpbc_jk_lowmem/build/libpbc/tests/pbc_screening_test {infile_mgo} {outfile_mgo}"

    slurm_filename = f"/n/home02/hieudinh/scr_work/script/diamond/" + f"diamond_ccpvqz_{i:02d}_job.sh"
    save_slurm_to_file(slurm_filename, job_name, output_file, nodes, ntasks, time, partition, command)
    print(f"SLURM script saved to {slurm_filename}")
