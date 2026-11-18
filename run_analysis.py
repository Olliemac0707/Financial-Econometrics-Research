"""Execute the research notebook in a fresh kernel with the current interpreter."""

from pathlib import Path
import os
import sys

import nbformat
from jupyter_client import KernelManager
from nbclient import NotebookClient


def main():
    root = Path(__file__).resolve().parent
    data_file = root / "data" / "market_macro_data.xlsx"
    if not data_file.is_file():
        raise FileNotFoundError(
            "Supply data/market_macro_data.xlsx as described in data/README.md"
        )

    notebook = nbformat.read(root / "analysis.ipynb", as_version=4)
    manager = KernelManager(kernel_name="python3")
    manager.kernel_spec.argv[0] = sys.executable
    profile = root / "analysis_outputs" / "ipython"
    profile.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["IPYTHONDIR"] = str(profile)

    client = NotebookClient(
        notebook,
        km=manager,
        timeout=600,
        allow_errors=False,
        resources={"metadata": {"path": str(root)}},
    )
    client.execute(cleanup_kc=True, env=environment)
    nbformat.validate(notebook)
    output_file = root / "analysis_outputs" / "analysis_executed.ipynb"
    nbformat.write(notebook, output_file)
    print(f"Executed notebook saved to {output_file.relative_to(root)}")


if __name__ == "__main__":
    main()
