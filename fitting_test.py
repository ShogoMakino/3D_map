#! /usr/bin/env python3
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    range_num = 10
    sample_p = [[0.25, 0.75] for l in range(range_num)]
    sample_x = [[l + sample_p[l][0], l + sample_p[l][1]] for l in range(range_num)]
    sample_h = [[math.sin(sample_x[l][0]), math.sin(sample_x[l][1])] for l in range(range_num)]

    k = 0.2

    h = [0 for l in range(range_num + 1)]
    prev_coef = [0 for l in range(range_num + 1)]
    this_coef = [0 for l in range(range_num + 1)]
    next_coef = [0 for l in range(range_num + 1)]
    constant = [0 for l in range(range_num + 1)]
    for i in range (range_num + 1):
        if i == 0:
            h[i] = sample_h[i][0]
            prev_coef[i] = 0
            this_coef[i] = 2 * ((1 - sample_p[i][0]) ** 2
                                + (1 - sample_p[i][1]) ** 2)
            next_coef[i] = 2 * (sample_p[i][0] * (1 - sample_p[i][0])
                                + sample_p[i][1] * (1 - sample_p[i][1]))
            constant[i] = -2 * ((1 - sample_p[i][0]) * sample_h[i][0]
                                + (1 - sample_p[i][1]) * sample_h[i][1])
        elif i == range_num:
            h[i] = sample_h[i - 1][1]
            next_coef[i] = 0
            prev_coef[i] = 2 * (sample_p[i - 1][0] * (1 - sample_p[i - 1][0])
                                + sample_p[i - 1][1] * (1 - sample_p[i - 1][1]))
            this_coef[i] = 2 * (sample_p[i - 1][0] ** 2
                                + sample_p[i - 1][1] ** 2)
            constant[i] = -2 * (sample_p[i - 1][0] * sample_h[i - 1][0]
                                + sample_p[i - 1][1] * sample_h[i - 1][1])
        else:
            h[i] = (sample_h[i][0] + sample_h[i - 1][1]) / 2
            prev_coef[i] = 2 * (sample_p[i - 1][0] * (1 - sample_p[i - 1][0])
                                + sample_p[i - 1][1] * (1 - sample_p[i - 1][1]))
            this_coef[i] = 2 * (sample_p[i - 1][0] ** 2 + (1 - sample_p[i][0]) ** 2
                                + sample_p[i - 1][1] ** 2 + (1 - sample_p[i][1]) ** 2)
            next_coef[i] = 2 * (sample_p[i][0] * (1 - sample_p[i][0])
                                + sample_p[i][1] * (1 - sample_p[i][1]))
            constant[i] = -2 * (sample_p[i - 1][0] * sample_h[i - 1][0]
                                + sample_p[i - 1][1] * sample_h[i - 1][1]
                                + (1 - sample_p[i][0]) * sample_h[i][0]
                                + (1 - sample_p[i][1]) * sample_h[i][1])

    x_list = sum(sample_x, [])
    h_list = sum(sample_h, [])

    h = [0 for l in range(range_num + 1)]

    for i in range(10):
        h_diff = [0 for l in range(len(h))]
        for j in range(len(h_diff)):
            p = 0 if j == 0 else h[j - 1]
            t = h[j]
            n = 0 if j == range_num else h[j + 1]
            h_diff[j] = p * prev_coef[j] + t * this_coef[j] + n * next_coef[j] + constant[j]
        h = [(l - k * m) for l, m in zip(h, h_diff)] 
        
        plt.clf()
        plt.plot(x_list, h_list) 
        plt.plot(range(range_num + 1), h)
        plt.pause(1)
    
if __name__ == '__main__':
    main()
