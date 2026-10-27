import subprocess
import sys
from pathlib import Path


START = "  # BEGIN python-ldap-build legacy Python 3.6 metadata\n"
END = "  # END python-ldap-build legacy Python 3.6 metadata\n"


def main() -> None:
    setup_py = Path(__file__).resolve().parents[1] / "setup.py"
    source = setup_py.read_text(encoding="utf-8")

    if sys.version_info < (3, 7):
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "setuptools==60.10.0", "wheel"]
        )
        if START not in source:
            source = source.replace(
                "from setuptools import setup, Extension",
                "from setuptools import setup, Extension, find_packages",
                1,
            )
            legacy_metadata = (
                START
                + "  name = 'python-ldap',\n"
                + "  version = pkginfo.__version__,\n"
                + "  packages = find_packages('Lib'),\n"
                + "  package_dir = {'': 'Lib'},\n"
                + "  py_modules = ['ldapurl', 'ldif'],\n"
                + "  install_requires = ['pyasn1>=0.3.7', 'pyasn1_modules>=0.1.5'],\n"
                + "  python_requires = '>=3.6',\n"
                + "  include_package_data = True,\n"
                + END
            )
            source = source.replace(
                "setup(\n  ext_modules = [",
                "setup(\n" + legacy_metadata + "  ext_modules = [",
                1,
            )
            if START not in source:
                raise RuntimeError("Could not add Python 3.6 package metadata to setup.py")
        setup_py.write_text(source, encoding="utf-8")
    else:
        if START in source:
            before, remainder = source.split(START, 1)
            _, after = remainder.split(END, 1)
            source = before + after
            source = source.replace(
                "from setuptools import setup, Extension, find_packages",
                "from setuptools import setup, Extension",
                1,
            )
            setup_py.write_text(source, encoding="utf-8")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "setuptools>=61", "wheel"]
        )


if __name__ == "__main__":
    main()
