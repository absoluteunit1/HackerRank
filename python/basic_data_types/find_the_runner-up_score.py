n = int(input())
scores = list(map(int, input().split()))

winner = max(scores)
runner_up = -100
for score in scores:
    if score >= runner_up and winner > score:
        runner_up = score
print(runner_up)