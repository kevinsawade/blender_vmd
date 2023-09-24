"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Blender VMD."""


if __name__ == "__main__":
    main(prog_name="blender_vmd")  # pragma: no cover
