import json
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

    def _filter_requests(self, *args) -> list[dict]:
        """
        Filter requests based on status code
        """
        return list(filter(lambda x: x["status_code"] in range(*args), self.requests))

    def _try_stats_func(func):
        """
        Try to run a function and return the results or float(0)
        """

        def apply(self):
            try:
                return func(self)
            except ValueError:
                return 0.0

        return apply

    @_try_stats_func
    def slowest(self) -> float:
        """
        Returns the slowest request's completion time
        """
        return round(
            max(self._filter_requests(200, 299), key=lambda x: x["time"])["time"], 2
        )

    @_try_stats_func
    def fastest(self) -> float:
        """
        Returns the fastest request's completion time
        """
        return round(
            min(self._filter_requests(200, 299), key=lambda x: x["time"])["time"], 2
        )

    @_try_stats_func
    def average(self) -> float:
        """
        Returns the average_time request's completion time
        """
        # return round(mean(self._filter_requests(200, 299))["time"], 2)
        return round(mean([x["time"] for x in self._filter_requests(200, 299)]), 2)

    @_try_stats_func
    def successful_requests(self) -> float:
        """
        Returns the successful request's completion time
        """
        return round(len(self._filter_requests(200, 299)), 2)

    @_try_stats_func
    def failed_requests(self) -> float:
        """
        Returns the failed request's completion time
        """
        return round(len(self._filter_requests(500, 599)), 2)

    def total_time(self) -> float:
        """
        Returns the total time
        """
        return round(self.total, 2)

    def requests_per_minute(self) -> float:
        """
        Returns the requests per minute
        """
        return round(len(self.requests) / self.total * 60, 2)

    def requests_per_second(self) -> float:
        """
        Returns the requests per second
        """
        return round(len(self.requests) / self.total, 2)

    def json(self) -> str:
        """
        Returns the json representation of the results
        """
        return json.dumps(
            {
                "successful_requests": self.successful_requests(),
                "failed_requests": self.failed_requests(),
                "slowest": self.slowest(),
                "fastest": self.fastest(),
                "average": self.average(),
                "total_time": self.total_time(),
                "requests_per_minute": self.requests_per_minute(),
                "requests_per_second": self.requests_per_second(),
            }
        )
