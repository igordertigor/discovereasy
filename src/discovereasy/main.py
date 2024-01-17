import typer
from .opportunity_tree import app as opportunity_tree_app
from .assumptions import app as assumptions_app

app = typer.Typer()
app.add_typer(opportunity_tree_app)
app.add_typer(assumptions_app)

if __name__ == '__main__':
    app()
