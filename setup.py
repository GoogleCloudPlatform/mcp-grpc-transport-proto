import sys
from pathlib import Path

import setuptools
from setuptools.command.build_py import build_py as _build_py

sys.path.insert(0, str(Path(__file__).parent))
from generate import ProtoGenerationError, generate_protos


class build_py(_build_py):
    def run(self):
        try:
            generate_protos()
        except ProtoGenerationError as e:
            sys.exit(f"error: {e}")
        super().run()


setuptools.setup(cmdclass={"build_py": build_py})
