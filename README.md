# python-ldap Windows wheels

This repository builds and publishes Windows wheels for the upstream
[python-ldap](https://github.com/python-ldap/python-ldap) releases. Push a
`vX.Y.Z` tag to build the upstream `python-ldap-X.Y.Z` source and publish all
Windows wheels to this repository's GitHub Release.

The workflow builds CPython 3.6 through 3.13 for both 32-bit (`win32`) and
64-bit (`win_amd64`). For example, the Python 3.12 64-bit wheel is installed
with:

```powershell
py -3.12 -m pip install python_ldap-3.4.8-cp312-cp312-win_amd64.whl
```

The OpenLDAP and OpenSSL static libraries are built from source during each
workflow run; they are not committed to this repository. Python 3.6 uses a
small build-time metadata compatibility path because the 3.4.8 build requires
setuptools 61+, which dropped Python 3.6 support.
