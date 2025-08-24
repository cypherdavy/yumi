import json
from rich.console import Console
from rich.table import Table

console = Console()

def generate_report(findings):
    if not findings:
        console.print("[bold green]No critical findings detected![/bold green]")
        return

    table = Table(title="Yumi Scan Findings")
    table.add_column("URL", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Match", style="yellow")

    for f in findings:
        table.add_row(f["url"], f["type"], f["match"])

    console.print(table)

    with open("report.json", "w") as f:
        json.dump(findings, f, indent=4)
    console.print("[bold blue]Report saved to 'report.json'[/bold blue]")

