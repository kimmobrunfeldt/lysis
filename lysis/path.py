"""
Provides project's paths to all modules.
Note: Use only ascii filenames for internal purposes!
If the project's structure changes, you will only have to change this file.
"""

import os
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))


# Relative paths to common directories.
# Format: {short_cut: relative_path_from_project_root}
# Paths must not contain leading or trailing slashes('/').
# Use '/' slash on all platforms.
_paths = {
    'static': 'webstatic'
}


def get_path(relative_path):
    """Returns resource's full path from relative path."""
    frozen = getattr(sys, 'frozen', '')
    expanded_path = expand_path(relative_path)

    if not frozen:
        # Go back to root level of project.
        resource_dir = get_parent_dir(script_dir, steps=1)

    elif frozen in ('dll', 'console_exe', 'windows_exe'):
        # py2exe:
        resource_dir = os.path.dirname(sys.executable)

    elif frozen in ('macosx_app',):
        # py2app:
        # Notes on how to find stuff on MAC, by an expert (Bob Ippolito):
        # http://mail.python.org/pipermail/pythonmac-sig/2004-November/012121.html
        resource_dir = os.environ['RESOURCEPATH']

    return os.path.abspath(os.path.join(resource_dir, expanded_path))


def expand_path(file_path):
    """Finds out the full path of a file needed in the script.
    Example usages:
    >>> expand_path('{static}/logo.png')
    '/path/to/project/ocrbenchmark/webserver/static/logo.png'
    >>> expand_path('README.txt')
    '/path/to/project/README.txt'

    Args:
        file_path: Project-root relative path to the file.

    Returns:
        str. Full path to the file.
    """
    # Format all {img} etc paths to correct paths
    file_path = file_path.format(**_paths)
    return file_path


def get_parent_dir(directory, steps=1):
    """Finds out directory's parent path.

    Args:
        directory: Path to the original directory.
    Kwargs:
        steps: How many steps is taken backwards in the directory tree.
               1=parent, 2=parent's parent, etc.
    """
    for x in range(steps):
        directory = os.path.abspath(os.path.join(directory, os.path.pardir))
    return os.path.realpath(directory)



