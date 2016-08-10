model_name = "TET12SN"
annotated_sequence = """
M
LEE ELKQLEE ELQAIEE QLAQLQW KAQARKE KLAQLKE KL	|APHshSN
SGPGS
SPED EIQQLEE EISQLEQ KNSELKE KNQELKY	|P3SN
SGPGS
DIEQ ELERAKE SIRRLEQ EVNQERS RMQYLQT LLEK	|BCRSN
SGPGS
QLED KVEELLS KNYHLEN EVERLKK LV	|GCNshSN
SGPGS
LEE ELKQLEE ELQAIEE QLAQLQW KAQARKE KLAQLKE KL	|APHshSN
SGPGS
SPED EIQQLEE KNSQLKQ EISQLEE KNQELKY	|P7SN
SGPGS
QLED KVEELLS KNYHLEN EVERLKK LV	|GCNshSN
SGPGS
SPED KISQLKE KIQQLKQ ENQQLEE ENSQLEY	|P4SN
SGPGS
SPED ENSQLEE KISQLKQ KNSELKE EIQQLEY	|P5SN
SGPGS
SPED KISELKE ENQQLEQ KIQQLKE ENSQLEY	|P8SN
SGPGS
DIEQ ELERAKE SIRRLEQ EVNQERS RMQYLQT LLEK	|BCRSN
SGPGS
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
    import ppmod.make_json as mj   
    import ppmod.segment_assignment as sa
    entire_sequence = sa.deannotate_sequence(annotated_sequence, remove_whitespace=True)  
    pairs = mj.load_pairs(pairs_info)    
    mj.generate_json(model_name, entire_sequence, annotated_sequence, pairs)

