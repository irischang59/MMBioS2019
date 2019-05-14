#!/usr/bin/python

import os.path
import sys

PYTHONPATH = '/usr/local/lib/vmd/scripts/python:/usr/local/lib/vmd/plugins/noarch/python'

for path in PYTHONPATH.split(':'):
    if path and not path in sys.path:
        sys.path.append(path)
# If Python druggability package was not installed, enter the path to contents of the tarball
# e.g.  PACKAGE_PATH = '/home/username/druggability/lib'
PACKAGE_PATH = '/usr/local/lib/vmd/plugins/noarch/tcl/drugui'

if PACKAGE_PATH:
    sys.path.append(PACKAGE_PATH)
try:
    from druggability import *
except ImportError:
    raise ImportError('druggability package was not found. Edit {0:s} '
                      'to proceed with calculation'.format(__file__))

if len(sys.argv) > 1:
  # for VMD use. if console logging is enabled, VMD raises an error
  verbose = sys.argv[1]
else:
  verbose = 'info'
probe_grids = [
('IPRO', '/home/anilee/area/zsrc/t-drug/t-mdm2/zdrg1/al/dg_IPRO.dx'),
('IPAM', '/home/anilee/area/zsrc/t-drug/t-mdm2/zdrg1/al/dg_IPAM.dx'),
('ACAM', '/home/anilee/area/zsrc/t-drug/t-mdm2/zdrg1/al/dg_ACAM.dx'),
('ACET', '/home/anilee/area/zsrc/t-drug/t-mdm2/zdrg1/al/dg_ACET.dx'),
]
dia = DIA('dg', workdir='/home/anilee/area/zsrc/t-drug/t-mdm2/zdrg1/al/dg', verbose=verbose)
# check parameters for their correctness
dia.set_parameters(temperature=300) # K (productive simulation temperature)
dia.set_parameters(delta_g=-1) # kcal/mol (probe binding hotspots with lower values will be evaluated)
dia.set_parameters(n_probes=7) # (number of probes to be merged to determine achievable affinity of a potential site)
dia.set_parameters(min_n_probes=6) # (minimum number of probes to be merged for an acceptable soltuion)
dia.set_parameters(merge_radius=5.5) # A (distance within which two probes will be merged)
dia.set_parameters(low_affinity=10) # microMolar (potential sites with affinity better than this value will be reported)
dia.set_parameters(n_solutions=3) # (number of drug-size solutions to report for each potential binding site)
dia.set_parameters(max_charge=2) # (maximum absolute total charge, where total charge is occupancy weighted sum of charges on probes)
dia.set_parameters(n_charged=3) # (maximum number of charged hotspots in a solution)
dia.set_parameters(n_frames=1) # number of frames (if volmap was used (.dx), 1 is correct)
for probe_type, grid_file in probe_grids: dia.add_probe(probe_type, grid_file)
# Do the calculations
dia.perform_analysis()
dia.pickle()
# Evaluate a ligand. Be sure that the ligand bound structure is superimposed
# onto PROTEIN_heavyatoms.pdb
#dia.evaluate_ligand('only_ligand_coordinates.pdb') # remove # sign from the beginning of line
