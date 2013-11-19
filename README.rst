PyWake
======

Python Wake-On-LAN client with advanced options and IPv6 capability.

Features
--------

* No privileges required (sending UDP packets)
* Advanced configuration options
   - source IP address
   - destination IP address
   - destination UDP port
   - target MAC address
* IPv6 by default (who uses IPv4 these days anyway)
* Contains re-usable module for use in other scripts

Locations
---------

PyWake packages are available from Cheese shop (PyPI)
at https://pypi.python.org/pypi/pywake

The `project page <https://github.com/beli-sk/pywake>`_ is hosted on Github.

If you've never worked with *git* or contributed to a project on Github,
there is a `quick start guide <https://help.github.com/articles/fork-a-repo>`_.

If you find something wrong or know of a missing feature, please
`create an issue <https://github.com/beli-sk/pywake/issues>`_ on the project
page. If you find that inconvenient or have some security concerns, you could
also drop me a line at <devel@beli.sk>.

How to use
----------

Install
~~~~~~~

::

    pip install pywake

Examples
~~~~~~~~

Wake up a MAC with default settings (IPv6 UDP packet to "all nodes" multicast
address ff02::1 and port 9 - discard)::

    pywake 00:11:22:33:44:55

You may need to specify a source interface (or scope) for the multicast packets
if there are more possibilities::

    pywake -d ff02::1%eth0 00:11:22:33:44:55

Or use a plain old IPv4 UDP subnet directed broadcast::

    pywake -4 -d 192.168.1.255 00:11:22:33:44:55

License
-------

Copyright 2013 Michal Belica <devel@beli.sk>

::

    PyWake is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    PyWake is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with PyWake.  If not, see < http://www.gnu.org/licenses/ >.

