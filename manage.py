#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    import sys
    sys.path.append(os.path.dirname(__file__))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'userdata/'))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'env/lib/python2.7/site-packages'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "userdata.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
