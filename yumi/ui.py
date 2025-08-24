import time
import random
import pyfiglet
from rich.console import Console
from rich.progress import Progress

console = Console()
tips = [
    "Pro tip: Always check JS files for hardcoded secrets!",
    "Bug bounty rule: Don't ignore old endpoints in JS.",
    "Remember: Subdomains love hiding vulnerable JS."
]

def display_logo_and_loading():
    logo = pyfiglet.figlet_format("YUMI")
    console.print(f"[bold cyan]{logo}[/bold cyan]")
    console.rule("[bold purple]The Ultimate JS Recon & P1 Bug Hunter[/bold purple]")
    console.print(f"[italic yellow]{random.choice(tips)}[/italic yellow]")
    console.print("\n[green]Initializing modules...[/green]\n")
    with Progress() as progress:
        task = progress.add_task("[cyan]Starting Yumi...", total=100)
        while not progress.finished:
            progress.update(task, advance=2.5)
            time.sleep(0.05)
    console.print("[bold green]Ready![/bold green]")

