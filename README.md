# ulta3

A simple CLI load testing tool.

## Installation

Install using `pip`:

```
$ pip install -e .
```

## Usage

The simplest usage of `ulta3` requires only a URL to test against
and 500 requests synchronously (one at a time). This is what it
would look like:

```
$ ulta3 https://example.com
.... Done!
--- Results ---
Successful requests 500
Slowest 0.010s
Fastest 0.001s
Average 0.003s
Total time 0.620s
Requests Per Minute 48360
Requests Per Second 806
```

If we want to add concurrency, we'll use the `-c` option, and we can
With our documentation in place, we at least have something to come back to if we
lose track of what we should be working towards.
use the `-r` option to specify how many requests that we'd like to
make:

```
$ ulta3 -r 3000 -c 10 https://example.com
.... Done!
--- Results ---
Successful requests 3000
Slowest 0.010s
Fastest 0.001s
Average 0.003s
Total time 2.400s
Requests Per Minute 90000
Requests Per Second 1250
```

If you'd like to see these results in JSON format, you can use the `-
j` option with a path to a JSON file:

```
$ ulta3 -r 3000 -c 10 -j output.json https://example.com
.... Done!
```
