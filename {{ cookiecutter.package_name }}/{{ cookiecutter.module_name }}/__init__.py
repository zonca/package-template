# Licensed under a 3-clause BSD style license - see LICENSE.rst

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._{{ cookiecutter._parent_project }}_init import *   # noqa
# ----------------------------------------------------------------------------

# Enforce Python version check during package import.
# This is the same check as the one at the top of setup.py
import sys
from distutils.version import LooseVersion

__minimum_python_version__ = "{{ cookiecutter.minimum_python_version }}"

__all__ = []


class UnsupportedPythonError(Exception):
    pass


if LooseVersion(sys.version) < LooseVersion(__minimum_python_version__):
    raise UnsupportedPythonError("{{ cookiecutter.module_name }} does not support Python < {}"
                                 .format(__minimum_python_version__))

if not _ASTROPY_SETUP_:   # noqa
    # For egg_info test builds to pass, put package imports here.
{%- if cookiecutter.include_example_code != 'y' %}
    pass
{%- else %}
    from .example_mod import *   # noqa
    # Then you can be explicit to control what ends up in the namespace,
    __all__ += ['do_primes']   # noqa
    # or you can keep everything from the subpackage with the following instead
    # __all__ += example_mod.__all__
{%- endif %}
