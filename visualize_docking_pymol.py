# load 7NN0 - reference structure
cmd.load("7NN0_A_ready.pdbqt")
set surface_color, gray
show surface

# load ligand
cmd.load("EOS100357_processed_out.pdbqt")

# select ligand
select my_ligand, EOS100357_processed_out

# select protein
select protein, 7NN0_A_ready and polymer

# select environment
select env, protein within 5 of my_ligand
set transparency, 0.2, env

# selecte amino-acids from the ADP binding site
select aa, /7NN0_A_ready//A/ASP`374/
color magenta, aa
show sticks, aa

select aa, /7NN0_A_ready//A/GLU`375/
color magenta, aa
show sticks, aa

select aa, /7NN0_A_ready//A/SER`377/
color magenta, aa
show sticks, aa

select aa, /7NN0_A_ready//A/ASP`401/
color magenta, aa
show sticks, aa

select aa, /7NN0_A_ready//A/GLN`404/
color magenta, aa
show sticks, aa

select aa, /7NN0_A_ready//A/ARG`443/
color magenta, aa
show sticks, aa

select aa, /7NN0_A_ready//A/LYS`288/
color magenta, aa
show sticks, aa

select aa, /7NN0_A_ready//A/SER`289/
color magenta, aa
show sticks, aa

select aa, /7NN0_A_ready//A/ARG`567/
color magenta, aa
show sticks, aa

select aa, /7NN0_A_ready//A/GLY`538/
color magenta, aa
show sticks, aa

