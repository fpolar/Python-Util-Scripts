#Each assignment for a certain class had long compression and quantazation questions.
#Once I felt I had understood the topic and that doing more by hand wouldn't be as helpful,
#so I wrote this script to quantize, compress, then give me info about a given sequence of numbers 

import numpy as np

nums_raw = "5.8, 6.2, 6.2, 7.2, 7.3, 7.3, 6.5, 6.8, 6.8, 6.8, 5.5, 5.0, 5.2, 5.2, 5.8, 6.2, 6.2, 6.2, 5.9, 6.3, 5.2, 4.2, 2.8, 2.8, 2.3, 2.9, 1.8, 2.5, 2.5, 3.3, 4.1, 4.9"
nums_str_arr = nums_raw.split(", ")
num_arr = [float(num_str) for num_str in nums_str_arr]

nums_np = np.array(num_arr)
bins = [ (x / 100.0) for x in range(25, 825, 25)]
# print(bins)
bins_np = np.array(bins)
inds = np.digitize(nums_np, bins_np)
print(inds)
sequence =  [bins[num] for num in inds]
print(sequence)

diffs = [x - sequence[i - 1] for i, x in enumerate(sequence) if i > 0]
print(diffs)

print(max(diffs))
print(min(diffs))