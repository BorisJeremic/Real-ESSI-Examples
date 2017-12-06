# 1. Generate mesh from geometry
gmsh -3 Example_*.geo

# 2. Generate ESSI finite element inputs from mesh
gmessy Example_*.gmessi

# 3. Extend Real-ESSI DSL in ./Example_1_ESSI_Simulation/Example_1_analysis.fei
#    and then execute essi
essi -f Example_*_analysis_full.fei