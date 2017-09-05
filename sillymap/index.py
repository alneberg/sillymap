import pickle
from .count_lookup import count_lookup
from .rank_lookup import Rank
from .burrows_wheeler import burrows_wheeler

import numpy as np

def index_main(args):
    with open(args.reference, 'r') as ref_fh:
        reference_seq = ""
        for i, line in enumerate(ref_fh):
            if line.startswith('>'):
                if i != 0:
                    raise ValueError("Silly you, you expect sillymap to accept more than one reference sequence?")
                reference_id = line[1:].strip()
            else:
                reference_seq += line.strip()
    reference_seq_binary = translate_to_binary(reference_seq)
    bw, sa_index = burrows_wheeler(reference_seq_binary)
    cl = count_lookup(bw)
    rank = Rank()
    rank.add_text(bw)

    ref_output = "{}.silly".format(args.reference)
    with open(ref_output, "wb") as pickle_fh:
        pickle.dump((cl, rank, bw, sa_index), pickle_fh)

def translate_to_binary(seq_string):
    nucl_to_bin = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    try:
        return np.asarray([nucl_to_bin[nucl] for nucl in seq_string], dtype='B')
    except KeyError:
        raise ValueError("Sequence contain more than standard nucleotides ACGT, aborting.")

