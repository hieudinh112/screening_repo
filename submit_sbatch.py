import subprocess
import os

def submit_jobs(job_files):
    """
    Submit multiple SLURM job scripts and return their job IDs.

    Parameters:
        job_files (list of str): List of job script file paths.

    Returns:
        list of str: List of SLURM job IDs for submitted jobs.
    """
    job_ids = []
    
    for job_file in job_files:
        if not os.path.isfile(job_file):
            print(f"Error: File not found: {job_file}")
            continue

        try:
            result = subprocess.run(["sbatch", job_file], capture_output=True, text=True)
            if result.returncode == 0:
                # Extract the job ID from the output
                output = result.stdout.strip()
                print(f"Submitted {job_file}: {output}")
                job_id = output.split()[-1]
                job_ids.append(job_id)
            else:
                print(f"Failed to submit {job_file}: {result.stderr.strip()}")
        except Exception as e:
            print(f"Error submitting {job_file}: {e}")

    return job_ids

if __name__ == "__main__":
    # List your job files here
    job_scripts = []
    for i in range(1, 11):
        job_scripts.append(f"/n/home02/hieudinh/scr_work/script/diamond/diamond_ccpvqz_{i:02d}_job.sh")
        job_scripts.append(f"/n/home02/hieudinh/scr_work/script/diamond/diamond_ccpvtz_{i:02d}_job.sh")

    print("Submitting jobs...")
    submitted_job_ids = submit_jobs(job_scripts)

    if submitted_job_ids:
        print("\nSuccessfully submitted jobs:")
        for job_id in submitted_job_ids:
            print(f"Job ID: {job_id}")
    else:
        print("\nNo jobs were submitted.")