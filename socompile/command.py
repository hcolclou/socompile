"""Commands"""

import click
import os
from pathlib import Path

from socompile.compile import run

@click.command()
@click.option('-i', '--in_dir', default='.', help='Input directory with grades.')
@click.option('-o', '--out_file', default='output.csv', help="File to write " + 
    "output to.")
def compile(in_dir, out_file) -> None:
    """parse data and output to CSV file"""

    in_path = os.path.abspath(in_dir)
    out_path = os.path.abspath(out_file)
    
    run(in_path, out_path)