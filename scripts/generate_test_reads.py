"""A script to generate fake perfect reads from a reference. """

import argparse
import sys
import random

def read_reference(args):
    with open(args.reference, 'r') as ref_fh:
        reference_seq = ""
        for i, line in enumerate(ref_fh):
            if line.startswith('>'):
                if i != 0:
                    raise ValueError("Silly you, you expect sillymap to accept more than one reference sequence?")
                reference_id = line[1:].strip()
            else:
                reference_seq += line.strip()
    return reference_id, reference_seq

def main(args):
    reference_id, reference_seq = read_reference(args)
    fastq_template = """@read{{0}}
{{1}}
+
{0}
""".format("A"*args.read_length)

    with open(args.read_output_file, 'w') as ofh:
        for i, start_pos in enumerate([random.randrange(0, len(reference_seq)-args.read_length, 1) for _ in range(args.nr_reads)]):
            ofh.write(fastq_template.format(i+1, reference_seq[start_pos:start_pos+args.read_length]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument("reference", help="The input reference fasta file")
    parser.add_argument("read_output_file")
    parser.add_argument("nr_reads", type=int, help="The number of reads to generate")
    parser.add_argument("--read_length", type=int, default=25)
    args = parser.parse_args()
    main(args)

