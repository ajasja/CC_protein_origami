model_name = "TET12SN"
annotated_sequence = """
M
LEE ELKQLEE ELQAIEE QLAQLQW KAQARKE KLAQLKE KL	|APHshSN
GSGPG
SPED EIQQLEE EISQLEQ KNSELKE KNQELKY	|P3SN
GSGPG
DIEQ ELERAKE SIRRLEQ EVNQERS RMQYLQT LLEK	|BCRSN
GSGPG
QLED KVEELLS KNYHLEN EVERLKK LV	|GCNshSN
GSGPG
LEE ELKQLEE ELQAIEE QLAQLQW KAQARKE KLAQLKE KL	|APHshSN
GSGPG
SPED EIQQLEE KNSQLKQ EISQLEE KNQELKY	|P7SN
GSGPG
QLED KVEELLS KNYHLEN EVERLKK LV	|GCNshSN
GSGPG
SPED KISQLKE KIQQLKQ ENQQLEE ENSQLEY	|P4SN
GSGPG
SPED ENSQLEE KISQLKQ KNSELKE EIQQLEY	|P5SN
GSGPG
SPED KISELKE ENQQLEQ KIQQLKE ENSQLEY	|P8SN
GSGPG
DIEQ ELERAKE SIRRLEQ EVNQERS RMQYLQT LLEK	|BCRSN
GSGPG
SPED KNSELKE EIQQLEE ENQQLEE KISELKY	|P6SN
LEHHHHHHHH
"""

pairs_info = """
- 'pair': 'APHshSN:APHshSN'
  'type': 'A'
  'template': 'APH.pdb'
  'chains': 'A:B'
  'color': '#D62728'
  'strength': 76.0
- 'pair': 'P3SN:P4SN'
  'type': 'P'
  'template': 'p3_p4.pdb'
  'chains': 'A:B'
  'color': '#1F77B4'
  'strength': 63.0
- 'pair': 'BCRSN:BCRSN'
  'type': 'A'
  'template': 'BCR.pdb'
  'chains': 'A:B'
  'color': '#2CA02C'
  'strength': 56.0
- 'pair': 'P5SN:P6SN'
  'type': 'P'
  'template': 'p5_p6.pdb'
  'chains': 'A:B'
  'color': '#FF7F0E'
  'strength': 50.0
- 'pair': 'P7SN:P8SN'
  'type': 'P'
  'template': 'p7_p8.pdb'
  'chains': 'A:B'
  'color': '#9467BD'
  'strength': 47.0
- 'pair': 'GCNshSN:GCNshSN'
  'type': 'P'
  'template': 'GCN.pdb'
  'chains': 'A:B'
  'color': '#8C564B'
  'strength': 38.0
     
"""   

if __name__ == "__main__":
    import cocopod.make_json as mj   
    import cocopod.segment_assignment as sa
    import cocopod.make_color as mc
    import cocopod.utils as u
    entire_sequence = sa.deannotate_sequence(annotated_sequence, remove_whitespace=True)  
    pairs = mj.load_pairs(pairs_info)    

    #generate json file 
    mj.generate_json(model_name, entire_sequence, annotated_sequence, pairs)
    print("Written: "+model_name+".json")    
    
    #create chimera script for coloring.
    mc.chimera_color(model_name+".json", model_name+".chimera", verbose=False)
    print("Written: "+model_name+".chimera")
    
    #write fasta file
    u.write_fasta_file(model_name+".fasta", model_name, entire_sequence)
    print("Written: "+model_name+".fasta")

