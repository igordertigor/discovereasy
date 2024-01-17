from pathlib import Path
import typer

from .types import Node, NodeKind

app = typer.Typer()

class Assumption(Node):
    risk: float = 0.0
    evidence: float = 0.0


@app.command()
def main(filenames: list[Path]):
    pass
