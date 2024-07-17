import click
from ulta3.http import run
from ulta3.stats import Results


@click.command()
@click.option("--request", "-r", default=500, help="Number of requests. Default 500.")
@click.option(
    "--concurrency", "-c", default=1, help="Number of concurrency. Default 1."
)
@click.option("--out-json", "-j", default=None, help="Output json file. Default None.")
@click.argument("url", required=True)
def cli(request, concurrency, out_json, url):
    """This script prints hello world"""
    click.echo(f"Request: {request}")
    click.echo(f"Concurrency: {concurrency}")
    click.echo(f"Out-json: {out_json}")
    click.echo(f"URL: {url}")
    total, results = run(url, request, concurrency)
    display_results(Results(total, results), out_json)


def display_results(results, out_json):
    if out_json:
        with open(out_json, "w") as file:
            file.write(results.json())
    else:
        TEXT = f"""
.... Done!
--- Results ---
Successful requests {results.successful_requests()} 
Failed requests     {results.failed_requests()} 
Slowest             {results.slowest()}s
Fastest             {results.fastest()}s
Average             {results.average()}s
Total time          {results.total_time()}s
Requests Per Minute {results.requests_per_minute()}
Requests Per Second {results.requests_per_second()}   
"""
        click.echo(TEXT)


if __name__ == "__main__":
    cli()
