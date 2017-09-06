#!/usr/bin/env python
from multiprocessing import Process, Queue, cpu_count
from .backwards_search import backwards_search
from .index import translate_to_binary
import pickle
import sys

def serve(queue, args):
    with open(args.reads) as reads_fh:
        for i, line in enumerate(reads_fh):
            if i % 4 == 0:
                read_id = line.strip()[1:]
            if i % 4 == 1:
                queue.put((read_id, line))
    return True

def work(queue, count_lookup, rank, total_length, sa_index):
    while True:
        queue_t = line = queue.get()
        if queue_t is None:
            break
        read_id, line = queue_t
        line = translate_to_binary(line.strip())
        s, e = backwards_search(line, count_lookup, rank, total_length)
        if s <= e:
            sys.stdout.write("\n{},{}".format(read_id, sa_index[s]))

def mapper_main(args):
    ref_output = "{}.silly".format(args.reference)
    with open(ref_output, 'rb') as ref_fh:
        count_lookup, rank, burrows_wheeler, sa_index = pickle.load(ref_fh)

    total_length = len(sa_index)

    queue = Queue()
    NUMBER_OF_PROCESSES = cpu_count()
    workers = [Process(target=work, args=(queue, count_lookup, rank, total_length, sa_index)) 
            for i in range(NUMBER_OF_PROCESSES)]

    sys.stdout.write("read,start_position")
    for w in workers:
        w.start()

    serve_result = serve(queue, args)
    for w in workers:
        queue.put(None)
    [worker.join(10) for worker in workers]
    queue.close()
    sys.stdout.write('\n')
