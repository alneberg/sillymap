#!/usr/bin/env python
from .backwards_search import backwards_search
from .index import translate_to_binary
import pickle
from mpi4py import MPI
import sys
import numpy as np

def read_reads(args):
    queue = []
    with open(args.reads) as reads_fh:
        for i, line in enumerate(reads_fh):
            if i % 4 == 0:
                read_id = line.strip()[1:]
            if i % 4 == 1:
                queue.append((read_id, line.strip()))
    return queue, int((i+1)/4)

def mapper_main(args):
    ref_output = "{}.silly".format(args.reference)
    with open(ref_output, 'rb') as ref_fh:
        count_lookup, rank, burrows_wheeler, sa_index = pickle.load(ref_fh)

    total_length = len(sa_index)
    
    comm = MPI.COMM_WORLD
    NUMBER_OF_PROCESSES = comm.size
    mpi_rank = comm.Get_rank()

    if mpi_rank == 0:
        all_reads, tot_nr_reads = read_reads(args)
        m = tot_nr_reads/NUMBER_OF_PROCESSES
        all_reads = [all_reads[int(m*i):int(m*(i+1))] for i in range(NUMBER_OF_PROCESSES)]
    else:
        all_reads = None

    all_reads = comm.scatter(all_reads)

    result = []
    for queue_t in all_reads:
        if queue_t is None:
            break
        read_id, line = queue_t
        line = translate_to_binary(line.strip())
        s, e = backwards_search(line, count_lookup, rank, total_length)
        if s <= e:
            result.append("{},{}".format(read_id, sa_index[s]))

    result = comm.gather(result)

    if mpi_rank == 0:
        sys.stdout.write("read,start_position\n")
        for rank_result in result:
            if rank_result == []:
                continue
            sys.stdout.write('\n'.join(rank_result))
            sys.stdout.write('\n')
