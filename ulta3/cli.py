import click
from rich.console import Console
from ulta3.http import run
from ulta3.stats import Results

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
console = Console()


@click.command(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)
@click.option("--request", "-r", default=100, help="Number of requests (Default: 100)")
@click.option(
    "--concurrency", "-c", default=3, help="Number of concurrency (Default: 3)"
)
@click.option("--process", "-p", default=1, help="Number of process (Default: 1)")
@click.option(
    "--json-file",
    "-j",
    default=None,
    type=click.Path(),
    help="Output json file (Default: None)",
)
@click.argument("url", required=False)
def cli(request, concurrency, process, json_file, url):
    """... Ulta3 ..."""
    console.print(f"Request: {request}")
    console.print(f"Concurrency: {concurrency}")
    console.print(f"Process: {process}")
    console.print(f"Json-file: {json_file}")
    console.print(f"URL: {url}")
    total, results = run(url, request, concurrency)
    display_results(Results(total, results), json_file)


def display_results(results, json_file):
    console.print("... Done!", style="bold")
    if json_file:
        with open(json_file, "w") as file:
            file.write(results.json())
    else:
        console.print("--- Results ---", style="bold dark_sea_green4")
        console.print_json(results.json())


if __name__ == "__main__":
    cli()
