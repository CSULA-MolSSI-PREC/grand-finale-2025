# grand-finale-2024
Final day exercises for 2024 PREC computational molecular science workshop

### Setup
This exercise is intended to be run on NCSA Delta. Before you begin with the activities,
ensure that you have created an account on NCSA Delta. This may also require that you create
an account on ACCESS. You will also need to have access to a GPU allocation on Delta.

Enter the following commands in the terminal in order to setup the simulation environment.

1. Login to Delta:\
  `ssh username@login.delta.ncsa.illinois.edu`

2. Installing Conda:\
  `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`\
  `bash Miniconda3-latest-Linux-x86_64.sh` (answer YES to lots of questions!)\
  `source .bashrc`

3. Create Conda Environment:\
  `conda create -n mdtools python=3.9`\
  `conda activate mdtools`\
  `conda install -c conda-forge openmm mdtraj jupyter matplotlib scikit-learn nglview`

4. Clone the Repo:\
  `git clone https://github.com/CSULA-MolSSI-PREC/grand-finale-2024`


To use the Jupyter notebooks associated with this repo, you can use the NCSA 
OpenOnDemand portal, which can be found here: http://openondemand.delta.ncsa.illinois.edu/

This repo contains the data for ten different peptide chains. Each peptide chain contains 
16 amino acid residues. Below is peptide sequence for each:

 > 6D0 = ALA ASP ALA ALA ASP ALA ASP ALA ALA ASP ALA ASP ALA ALA ASP ALA\
  6E0 = ALA GLU ALA ALA GLU ALA GLU ALA ALA GLU ALA GLU ALA ALA GLU ALA\
  6F0 = ALA PHE ALA ALA PHE ALA PHE ALA ALA PHE ALA PHE ALA ALA PHE ALA\
  6G0 = ALA GLY ALA ALA GLY ALA GLY ALA ALA GLY ALA GLY ALA ALA GLY ALA\
  6H0 = ALA HIS ALA ALA HIS ALA HIS ALA ALA HIS ALA HIS ALA ALA HIS ALA\
  6K0 = ALA LYS ALA ALA LYS ALA LYS ALA ALA LYS ALA LYS ALA ALA LYS ALA\
  6M0 = ALA MET ALA ALA MET ALA MET ALA ALA MET ALA MET ALA ALA MET ALA\
  6N0 = ALA ASN ALA ALA ASN ALA ASN ALA ALA ASN ALA ASN ALA ALA ASN ALA\
  6P0 = ALA PRO ALA ALA PRO ALA PRO ALA ALA PRO ALA PRO ALA ALA PRO ALA\
  6V0 = ALA VAL ALA ALA VAL ALA VAL ALA ALA VAL ALA VAL ALA ALA VAL ALA
