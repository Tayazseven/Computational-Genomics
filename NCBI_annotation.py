from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
import time
import csv

seq_id=[]
seq_orto=[]
seq_def= []
timestart = time.clock()
for record in SeqIO.parse("ch_ests_8.fasta", "fasta"):
    result_handle = NCBIWWW.qblast(program="blastx",database="refseq_protein",sequence= record.seq,entrez_query= "txid9606[ORGN]")
    blast_records = NCBIXML.parse(result_handle)
    blast_record = blast_records.next()
    #print "# alignments:",len(blast_record.alignments)
    for alignment in blast_record.alignments[0:1]:
        seq_id.append(record.id)
        seq_orto.append(alignment.hit_id)
        seq_def.append(alignment.hit_def)
result_handle.close()
timestop = time.clock()
print "time",timestop-timestart
with open('seqout_ch_8.tsv', 'wb') as f: #writing to tsv file
    a = csv.writer(f, delimiter='\t')
    a.writerows(zip(seq_id,seq_orto,seq_def))

## time 45633.3465951 = 12.6 hours