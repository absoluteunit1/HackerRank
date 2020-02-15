def devisible_sum_pairs(n, k, ar):
    pairs = 0 
    for i in range(0, len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                pairs += 1
    return pairs

