from chemspipy import ChemSpider
from rdkit import Chem
cs = ChemSpider('2d0c1601-b15e-4e49-9ad3-36c64141b9ce')
data = [x.rstrip().split("\t")[1] for x in open("test_data.cs").readlines() if x.rstrip()]
out_sd = Chem.SDWriter("test_mols.sdf")
for id_pair in data:
  cas_id = id_pair[1]
  result = cs.search(cas_id)
  mol = None
  smiles = None
  if result.count:
    smiles = result[0].smiles
    mol = Chem.MolFromSmiles(smiles)
  print smiles
  if mol:
    out_sd.write(mol)

out_sd.close()
