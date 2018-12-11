import cobra
from cobra import Model, Reaction, Metabolite
output=cobra.io.read_sbml_model('Methylocystis_spSB2.xml')

with open("Methylocystis_spSB2_reactions.txt","w") as text_file:
	line='Reaction id'+'\t'+'Reaction name'+'\t'+'stoichiometry'+'\t'+'Genes'+'\r'
	text_file.write(line)
	for r in output.reactions:
		genes=''
		for g in r.genes:
			if type(g.id) is str:
			
				genes=genes+g.id+';'
		if type(r.name) is str:
			line=r.id+'\t'+r.name+'\t'+r.reaction+'\t'+genes+'\r'
			text_file.write(line)

with open("Methylocystis_spSB2_metabolites.txt","w") as text_file:
	line='Metabolite id'+'\t'+'metabolite name'+'\r'
	text_file.write(line)
	for m in output.metabolites:
		
		if type(m.name) is str:
			line=m.id+'\t'+m.name+'\r'
			text_file.write(line)
