#!/bin/bash
#SBATCH --job-name=diamond_ccpvtz_09
#SBATCH --output=diamond_ccpvtz_09.out
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --time=1:00:00
#SBATCH -o diamond_ccpvtz_09_%j.out
#SBATCH -e diamond_ccpvtz_09_%j.err
#SBATCH --mail-type=END
#SBATCH --mail-user=hieudinh@g.harvard.edu
#SBATCH --partition=serial_requeue

module purge
module load gmp/6.3.0-fasrc01
module load mpc/1.3.1-fasrc01
module load mpfr/4.2.1-fasrc01
module load intel/24.0.1-fasrc01 intel-mkl/24.0.1-fasrc01 intelmpi/2021.11-fasrc01
module load cmake/3.28.3-fasrc01
module load Mambaforge/23.11.0-fasrc01
module load python/3.10.13-fasrc01

/n/holylabs/LABS/joonholee_lab/Users/hieudinh/qcpbc_jk_lowmem/build/libpbc/tests/pbc_screening_test /n/home02/hieudinh/scr_work/basis_series/diamond/diamond_ccpvtz_09.in /n/home02/hieudinh/scr_work/basis_series/diamond/converged_data/diamond_ccpvtz_09_converged.mat

printf "... Done with the calculation..."
        