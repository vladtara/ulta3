from statistics import mean


class Results:
    """
    Results handles calculating statistics based on a list of
    requests that were made.
    Here's an example of what the information will look like:
        Successful requests 500
        Slowest 0.010s
        Fastest 0.001s
        Average 0.003s
        Total time 0.620s
        Requests Per Minute 48360
        Requests Per Second 806
    """

    def __init__(self, total: float, requests: list[dict]) -> None:
        self.total = total
        self.requests = requests

    def slowest(self) -> float:
        """
        Returns the slowest request's completion time
        >>> results = Results(10.6, [{
        ... 'status_code': 200,
        ... 'time': 3.4
        ... }, {
        ... 'status_code': 500,
        ... 'time': 6.1
        ... }, {
        ... 'status_code': 200,
        ... 'time': 1.04
        ... }])
        >>> results.slowest()
        6.1
        """
        return max(self.requests, key=lambda x: x["time"])["time"]

    def fastest(self) -> float:
        """
        Returns the fastest request's completion time
        >>> results = Results(10.6, [{
        ... 'status_code': 200,
        ... 'time': 3.4
        ... }, {
        ... 'status_code': 500,
        ... 'time': 6.1
        ... }, {
        ... 'status_code': 200,
        ... 'time': 1.04
        ... }])
        >>> results.fastest()
        1.04
        """
        return min(self.requests, key=lambda x: x["time"])["time"]

    def average(self) -> float:
        """
        Returns the average_time request's completion time
        >>> results = Results(10.6, [{
        ... 'status_code': 200,
        ... 'time': 3.4
        ... }, {
        ... 'status_code': 500,
        ... 'time': 6.1
        ... }, {
        ... 'status_code': 200,
        ... 'time': 1.04
        ... }])
        >>> results.average()
        3.513333333333333
        """
        return mean([x["time"] for x in self.requests])

    def total_time(self) -> float:
        return len([x["time"] for x in self.requests])

    def successful_requests(self) -> int:
        """
        Returns the slowest request's completion time
        >>> results = Results(10.6, [{
        ... 'status_code': 200,
        ... 'time': 3.4
        ... }, {
        ... 'status_code': 500,
        ... 'time': 6.1
        ... }, {
        ... 'status_code': 200,
        ... 'time': 1.04
        ... }])
        >>> results.successful_requests()
        2
        """
        return len(list(filter(lambda x: x["status_code"] == 200, self.requests)))
