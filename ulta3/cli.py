import click
from ulta3.http import run
from ulta3.stats import Results


@click.command()
@click.option("--request", "-r", default=500, help="Number of requests. Default 500.")
@click.option(
    "--concurrency", "-c", default=1, help="Number of concurrency. Default 1."
)
@click.option("--json-file", "-j", default=None, help="Output json file. Default None.")
@click.argument("url", required=True)
def cli(request, concurrency, json_file, url):
    """This script prints hello world"""
    click.echo(f"Request: {request}")
    click.echo(f"Concurrency: {concurrency}")
    click.echo(f"Json-file: {json_file}")
    click.echo(f"URL: {url}")
    total, results = run(url, request, concurrency)
    display_results(Results(total, results), json_file)


def display_results(results, json_file):
    click.echo("... Done!")
    if json_file:
        with open(json_file, "w") as file:
            file.write(results.json())
    else:
        click.echo(results.text())


if __name__ == "__main__":
    cli()
