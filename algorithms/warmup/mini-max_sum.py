  def miniMaxSum(arr):
    minimum = sum([i for i in sorted(arr)[0:4]])
    maximum = sum([i for i in sorted(arr)[1:5]])
    print(f"{minimum} {maximum}")