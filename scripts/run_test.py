import argparse
import pathlib
import subprocess
import sys

ROOT_DIR = pathlib.Path(__file__).parent.parent


def build(image: str) -> None:
    sys.exit(
        subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "-it",
                f"devcontainer:{image}",
            ],
            stderr=sys.stderr,
            stdout=sys.stdout,
            stdin=sys.stdin,
            check=False,
        ).returncode
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", choices=["python", "node", "pythonnode"])
    args = parser.parse_args()

    build(args.image)
