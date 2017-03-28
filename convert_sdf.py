import re,sys
from rdkit import Chem
from pubchempy import *

mols = Chem.SDMolSupplier(sys.argv[1])
for cmpd in mols:
  cmpds = get_compounds(Chem.MolToSmiles(cmpd,isomericSmiles=True), 'smiles')
  for c in cmpds:
    cas_id = None
    if c.canonical_smiles:
      for syn in c.synonyms:
        if re.search('CAS-\d{2,7}-\d\d-\d',syn):
          cas_id = syn
          break
    if cas_id:
      print(c.canonical_smiles,syn)
    break
