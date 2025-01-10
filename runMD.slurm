#!/bin/bash
#SBATCH --partition=gpuA40x4
#SBATCH --mem=16G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --gpus-per-node=1
#SBATCH --account=bbow-delta-gpu
#SBATCH -t 00:30:00

source ~/.bashrc

conda activate mdtools

python peptideMD.py > peptideMD.out
