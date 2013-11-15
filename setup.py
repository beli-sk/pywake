# This file is part of PyWake.
# 
# PyWake is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# PyWake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with PyWake.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(name='pywake',
        version='0.1.2',
        author='Michal Belica',
        author_email='devel@beli.sk',
        url='https://github.com/beli-sk/pywake',
        description='Python Wake-On-LAN client',
        long_description="""Python Wake-On-LAN client
with advanced options and IPv6 capability.""",
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Topic :: Utilities',
            ],
        py_modules=['pywake'],
        scripts=['scripts/pywake'],
        )

