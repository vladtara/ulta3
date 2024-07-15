import click
from ulta3.http import run


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
    run(url, request, concurrency)


if __name__ == "__main__":
    cli()
