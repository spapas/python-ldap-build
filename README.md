# python-ldap Windows wheels

This repository is based on Christoph Gohlke's original
[python-ldap-build](https://github.com/cgohlke/python-ldap-build) project.
It is maintained separately so I can build and publish new
[python-ldap](https://github.com/python-ldap/python-ldap) releases whenever I
choose. Push a `vX.Y.Z` tag to build the upstream `python-ldap-X.Y.Z` source
and publish all Windows wheels to this repository's GitHub Release.

The workflow builds CPython 3.11 through 3.14 for both 32-bit (`win32`) and
64-bit (`win_amd64`). For example, the Python 3.12 64-bit wheel is installed
with:

```powershell
py -3.12 -m pip install python_ldap-3.4.8-cp312-cp312-win_amd64.whl
```

The OpenLDAP and OpenSSL static libraries are built from source during each
workflow run; they are not committed to this repository.
