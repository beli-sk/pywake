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

import socket
import sys

IPV6_DEST = 'ff02::1'
IPV4_DEST = '255.255.255.255'

address_family = {
        6: socket.AF_INET6,
        4: socket.AF_INET,
        0: socket.AF_UNSPEC,
        }

af2text = {
        socket.AF_INET6: 'IPv6',
        socket.AF_INET: 'IPv4',
        }

class MagicPacket(str):
    def __new__(self, mac):
        self.mac = mac.translate(None, '.:-')
        self.bytemac = self.mac.decode('hex')
        return super(MagicPacket, self).__new__(self,
                'ffffffffffff'.decode('hex') +
                ''.join([self.bytemac for i in range(16)])
                )

class PyWake(object):
    def __init__(self, mac, src_ip=None, dst_ip=None, port=9, ipv=0):
        self.mac = mac
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.ipv = ipv
        self.port = port

    def send_packet(self):
        if self.dst_ip:
            dest = self.dst_ip
        elif self.ipv == 4:
            dest = IPV4_DEST
        else:
            dest = IPV6_DEST
        for res in socket.getaddrinfo(dest, self.port, 
                address_family[self.ipv], socket.SOCK_DGRAM):
            af, socktype, proto, canonname, sa = res
            print 'sending %s packet%s to IP %s for MAC %s' % (
                    af2text[af],
                    (' from IP ' + self.src_ip) if self.src_ip else '',
                    sa[0],
                    self.mac
                    )
            s = socket.socket(af, socktype, proto)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            if self.src_ip:
                s_addr = socket.getaddrinfo(self.src_ip, None, af, socket.SOCK_DGRAM, 0, socket.AI_PASSIVE)[0][4]
                s.bind(s_addr)
            packet = MagicPacket(self.mac)
            s.sendto(packet, sa)

