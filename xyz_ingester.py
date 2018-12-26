import os
import csv
import pandas as pd
import json
import numpy as np
from pypif.obj import *
from pypif import pif

xyzf = ".\\xyz\\" 
files = os.listdir(xyzf)
limit = len(files)

#Two methods are present. One method called xyztopanda() creates a Pandas DataFrame out of the file that is currently open,
#The other Method creates a PIF from that pandas dataframe called "harmonic_max_json()"

def xyztopanda(file):
	for i in range(0,limit):
		with open(file) as fullarray:
			passlist = []
			xyz_panda = pd.DataFrame(passlist)
			for line in csv.reader(fullarray, delimiter = "\t"):
				passlist.append(line)
		xyz_panda = xyz_panda.append(passlist)
		return xyz_panda

def harmonic_max_json(xyz_panda):
	my_pif = System()
	b = str(xyz_panda.loc[1,0])
	a = b.strip(" ")
	n_atom = int(xyz_panda.loc[0,0])
	smiles = n_atom + 3
	inchi = n_atom + 4
	atom_line = []
	harmony = n_atom+2
	harmony_np = xyz_panda.loc[harmony,:].dropna().values
	harmony_line = list(np.ndarray.tolist(harmony_np))
	harmonic_max = [harmony_line]
	
	#this loop extracts the atomic coordinates and Mulliken charges from the compound.
	for i in range(2,n_atom+2):
		atom_line.append([xyz_panda.loc[i,0],xyz_panda.loc[i,1],xyz_panda.loc[i,2],xyz_panda.loc[i,3],xyz_panda.loc[i,4]])


	#These lines take each of the properties encoded in the second line of the xyz file into individual instances of the Property() class.
	Inchi = Property(name="InChI Key Identifier", scalars=xyz_panda.loc[inchi,0])
	SMILES = Property(name="(SMILES) Chemical Identifier", scalars=xyz_panda.loc[smiles,0])
	Atom_Number = Property(name = "Number of Atoms", scalars = xyz_panda.loc[0,0])
	Tag = Property(name = "Database Tag + Id", scalars = xyz_panda.loc[1,0])
	Rotational_Constant_A = Property(name = "Rotational Constant A", scalars = xyz_panda.loc[1,1], units = "GHz", data_type = "COMPUTATIONAL")
	Rotational_Constant_B = Property(name = "Rotational Constant B", scalars = xyz_panda.loc[1,2], units = "GHz", data_type = "COMPUTATIONAL")
	Rotational_Constant_C = Property(name = "Rotational Constant C", scalars = xyz_panda.loc[1,3], units = "GHZ", data_type = "COMPUTATIONAL")
	Dipole_Moment = Property(name= "Dipole Moment",scalars = xyz_panda.loc[1,4], units = "Debye", data_type = "COMPUTATIONAL")
	Isotropic_polarizability = Property(name= "Isotropic polarizability", scalars = xyz_panda.loc[1,5], units = "Å^3", data_type = "COMPUTATIONAL")
	Energy_of_HOMO = Property(name= "Energy of HOMO",scalars= xyz_panda.loc[1,6], units= "Ha", data_type="COMPUTATIONAL")
	Energy_of_LUMO = Property(name= "Energy of LUMO",scalars= xyz_panda.loc[1,7], units= "Ha", data_type="COMPUTATIONAL")
	Band_Gap = Property(name= "Band Gap", scalars= xyz_panda.loc[1,8], units= "Ha", data_type= "COMPUTATIONAL")
	Electronic_spactial_extent = Property(name= "Electronic spactial extent", scalars= xyz_panda.loc[1,9], units= "Ha", data_type= "COMPUTATIONAL")
	Zero_point_vibrational_energy = Property(name="Zero point vibrational energy", scalars= xyz_panda.loc[1,10], units="Ha",data_type="COMPUTATIONAL")
	Internal_energy_at_0K = Property(name= "Internal energy at 0K", scalars= xyz_panda.loc[1,11], units= "Ha", data_type="COMPUTATIONAL")
	Internal_energy_at_298_K = Property(name= "Internal energy at 298 K", scalars= xyz_panda.loc[1,12], units= "Ha", data_type="COMPUTATIONAL")
	Enthalpy_at_298_K = Property(name= "Enthalpy at 298 K", scalars= xyz_panda.loc[1,13],units= "Ha", data_type="COMPUTATIONAL")
	Free_energy_at_298_K = Property(name="Free energy at 298 K", scalars= xyz_panda.loc[1,14], units="Ha", data_type="COMPUTATIONAL")
	Heat_capacity_at_298_K =Property(name="Heat capacity at 298 K", scalars= xyz_panda.loc[1,15], units="Ha",data_type="COMPUTATIONAL")
	Atomic_coordinates = Property(name="Atom Coordinates for (Atom, Position Vector, Mulliken Charge)", matrices=atom_line,units="Chemical, (x,y,z), e" ,data_type="COMPUTATIONAL")
	Ref = Reference(title="Quantum chemistry structures and properties of 134 kilo molecules.",publisher="Nature",url="https://www.nature.com/articles/sdata201422",authors="R. Ramakrishnan, Dral P. O., Rupp, M.")
	Harmonic = Property(name="Harmonic Vibrational Frequencies",matrices=harmonic_max,units="cm^-1",data_type="COMPUTATIONAL")
	#collecting all the features for the PIF
	my_pif.properties = [SMILES,Inchi,Atom_Number,Tag,Rotational_Constant_A,Rotational_Constant_B, Rotational_Constant_C, Dipole_Moment,Isotropic_polarizability,Energy_of_HOMO,Energy_of_LUMO,Band_Gap,Electronic_spactial_extent,Zero_point_vibrational_energy,Internal_energy_at_0K,Internal_energy_at_298_K,Enthalpy_at_298_K,Free_energy_at_298_K,Heat_capacity_at_298_K,Harmonic,Atomic_coordinates]
	my_pif.resources = [Ref]

	with open(a+".json","w") as outfile:
		pif.dump(my_pif,outfile)

def main():
	xyzf = ".\\xyz\\"
	files = os.listdir(xyzf)
	for i in range(0,limit):
		file = str(xyzf+files[i])
		xyz_panda = xyztopanda(file)
		harmonic_max_json(xyz_panda)
	print("All done!")
if __name__ == "__main__":
	main()
