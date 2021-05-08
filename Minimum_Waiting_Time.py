def minimumWaitingTime(queries):
    queries = sorted(queries)
    waitingTime = 0
    for idx in range(len(queries) - 1):
        waitingTime = waitingTime + sum(queries[0:idx + 1])

    return waitingTime
