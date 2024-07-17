from statistics import mean


class Results:
    """
    Results handles calculating statistics based on a list of
    requests that were made.
    Here's an example of what the information will look like:
        Successful requests 500
        Failed requests 0
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
        return round(max(self.requests, key=lambda x: x["time"])["time"], 2)

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
        return round(min(self.requests, key=lambda x: x["time"])["time"], 2)

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
        3.51
        """
        return round(mean([x["time"] for x in self.requests]), 2)

    def successful_requests(self) -> int:
        """
        Returns the successful request's completion time
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
        return len(
            list(filter(lambda x: x["status_code"] in range(200, 299), self.requests))
        )

    def failed_requests(self) -> int:
        """
        Returns the failed request's completion time
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
        >>> results.failed_requests()
        1
        """
        return len(
            list(filter(lambda x: x["status_code"] in range(500, 599), self.requests))
        )

    def total_time(self) -> float:
        """
        Returns the total time
        >>> results = Results(10.64, [{
        ... 'status_code': 200,
        ... 'time': 3.4
        ... }, {
        ... 'status_code': 500,
        ... 'time': 6.1
        ... }, {
        ... 'status_code': 200,
        ... 'time': 1.04
        ... }])
        >>> results.total_time()
        10.64
        """
        return round(self.total, 2)

    def requests_per_minute(self) -> float:
        """
        Returns the requests per minute
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
        >>> results.requests_per_minute()
        16.98
        """
        return round(len(self.requests) / self.total * 60, 2)

    def requests_per_second(self) -> float:
        """
        Returns the requests per second
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
        >>> results.requests_per_second()
        0.28
        """
        return round(len(self.requests) / self.total, 2)
