from Bio import SeqIO

def remove_reads(input_fasta, reads_to_remove, output_fasta):
    reads_set = set(record.id for record in SeqIO.parse(reads_to_remove, "fasta"))

    with open(output_fasta, "w") as output_handle:
        for record in SeqIO.parse(input_fasta, "fasta"):
            if record.id not in reads_set:
                SeqIO.write(record, output_handle, "fasta")

# Replace these filenames with your actual filenames
input_fasta = "Francois_extracted_P22_C_MINUS_204065.fasta"
reads_to_remove = "Sal_Origin_C_MINUS_same_hits.fasta"
output_fasta = "P22_without_sal_CM.fasta"

remove_reads(input_fasta, reads_to_remove, output_fasta)

