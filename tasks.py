import os
import platform
from invoke import task

@task
def start(ctx):
    """Start the application."""
    src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
    os.chdir(src_dir)  # Change the current working directory to the src folder
    ctx.run(f"python index.py")

@task
def test(ctx):
    ctx.run("poetry run pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
    
@task
def lint(ctx): 
    ctx.run(f"poetry run pylint src/index.py")