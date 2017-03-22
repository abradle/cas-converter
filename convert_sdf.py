import re,sys
from rdkit import Chem
from pubchempy import *

mols = Chem.SDMolSupplier(sys.argv[1])

for cmpd in mols:
  print Chem.MolToSmiles(cmpd,isomericSmiles=True)
  cmpds = get_compounds(Chem.MolToSmiles(cmpd,isomericSmiles=True), 'smiles')
  for c in cmpds:
    if c.canonical_smiles:
      print(c.synonyms)
      for syn in c.synonyms:
        if re.search('CAS-\d{2,7}-\d\d-\d',syn):
          print(syn)
