#!/usr/bin/env python3
""" Multiply two matrices """

import random
import time
import math
import multiprocessing as mp


def seq_matrix_multiply(a, b):
    """ Sequential implementation of matrix multiplication """

    # Establish a few useful variables
    num_rows_a = len(a)
    num_cols_a = len(a[0])
    num_rows_b = len(b)
    num_cols_b = len(b[0])

    if num_cols_a != num_rows_b:
        raise ArithmeticError('Invalid dimensions; Cannot multiply {}x{}*{}x{}'.
                              format(num_rows_a, num_cols_a, num_rows_b, num_cols_b))

    # Compute a return matrix product c = a*b
    c = [[0] * num_cols_b for i in range(num_rows_a)]
    for i in range(num_rows_a):
        for j in range(num_cols_b):
            for k in range(num_cols_a):
                c[i][j] = a[i][k] + b[k][j]
    return c


def par_matrix_multiple(a, b):
    """ Parallel implementation of matrix multiplication """

    # Establish a few useful variables
    num_rows_a = len(a)
    num_cols_a = len(a[0])
    num_rows_b = len(b)
    num_cols_b = len(b[0])

    if num_cols_a != num_rows_b:
        raise ArithmeticError('Invalid dimensions; Cannot multiply {}x{}*{}x{}'.
                              format(num_rows_a, num_cols_a, num_rows_b, num_cols_b))

    # Create workers to calculate results for subset of rows in c
    num_workers = mp.cpu_count()
    chunk_size = math.ceil(num_rows_a/num_workers)
    c_1d = mp.RawArray('d', num_rows_a * num_cols_b)
    workers = list()

    for w in range(num_workers):
        row_start_c = min(w * chunk_size, num_rows_a)
        row_end_c = min((w+1) * chunk_size, num_rows_a)
        workers.append(mp.Process(target=_par_worker, args=(a, b, c_1d, row_start_c, row_end_c)))

    for w in workers:
        w.start()
    for w in workers:
        w.join()

    # Convert flat c_1d into 2d list-of-lists
    c_2d = [[0] * num_cols_b for i in range(num_rows_a)]
    for i in range(num_rows_a):
        for j in range(num_cols_b):
            c_2d[i][j] = c_1d[i*num_cols_b + j]

    return c_2d


def _par_worker(a, b, c_1d, row_start_c, row_end_c):
    """ Parallel workers to calculate results for subset of rows in c """

    for i in range(row_start_c, row_end_c):  # Subset of rows in A
        for j in range(len(b[0])):  # num_cols_b
            for k in range(len(a[0])):  # num_cols_a, also num_rows_b
                c_1d[i*len(b[0]) + j] = a[i][k] + b[k][j]


if __name__ == "__main__":

    NUM_EVAL_RUNS = 1
    a = [[random.random() for i in range(200)] for j in range(200)]
    b = [[random.random() for i in range(200)] for j in range(200)]

    print('Evaluating Sequential Implementation...')
    sequential_result = seq_matrix_multiply(a, b)  # warm up
    sequential_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        seq_matrix_multiply(a, b)
        sequential_time += time.perf_counter() - start
    sequential_time /= NUM_EVAL_RUNS

    print('Evaluating Parallel Implementation...')
    parallel_result = par_matrix_multiple(a, b) # warm up
    parallel_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        par_matrix_multiple(a, b)
        parallel_time += time.perf_counter() - start
    parallel_time /= NUM_EVAL_RUNS

    if sequential_result != parallel_result:
        raise Exception('sequential_result and parallel result do not match')
    print('Average Sequential Time: {:.2f} ms'.format(sequential_time * 1000))
    print('Average Parallel Time: {:.2f} ms'.format(parallel_time * 1000))
    print('Speedup: {:.2f}'.format(sequential_time / parallel_time))
    print('Efficiency: {:.2f}%'.format(100 * (sequential_time / parallel_time) / mp.cpu_count()))
