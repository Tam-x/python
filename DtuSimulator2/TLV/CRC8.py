#                          The MIT License (MIT)
#
#                     Copyright (c) 2016 Nicco Kunzmann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
"""The crc8 module.

The crc8 module provides the same interface as the hashlib module.
    https://docs.python.org/2/library/hashlib.html

Some code was copied from here:
    https://dzone.com/articles/crc8py
and gave credit "From the PyPy project" and the link
    http://snippets.dzone.com/posts/show/3543

"""
import sys

__author__="Nicco Kunzmann"
__version__="0.0.4"

PY2 = sys.version_info[0] == 2


class crc8(object):

    digest_size = 1
    block_size = 1

    _table = [	0, 94, 188, 226, 97, 63, 221, 131, 194, 156, 126, 32, 163, 253, 31, 65, 157, 195, 33, 127, 252, 162, 64, 30,
			95, 1, 227, 189, 62, 96, 130, 220, 35, 125, 159, 193, 66, 28, 254, 160, 225, 191, 93, 3, 128, 222, 60, 98, 190, 224, 2,
			92, 223, 129, 99, 61, 124, 34, 192, 158, 29, 67, 161, 255, 70, 24, 250, 164, 39, 121, 155, 197, 132, 218, 56, 102,
			229, 187, 89, 7, 219, 133, 103, 57, 186, 228, 6, 88, 25, 71, 165, 251, 120, 38, 196, 154, 101, 59, 217, 135, 4, 90, 184,
			230, 167, 249, 27, 69, 198, 152, 122, 36, 248, 166, 68, 26, 153, 199, 37, 123, 58, 100, 134, 216, 91, 5, 231, 185,
			140, 210, 48, 110, 237, 179, 81, 15, 78, 16, 242, 172, 47, 113, 147, 205, 17, 79, 173, 243, 112, 46, 204, 146, 211, 141,
			111, 49, 178, 236, 14, 80, 175, 241, 19, 77, 206, 144, 114, 44, 109, 51, 209, 143, 12, 82, 176, 238, 50, 108, 142,
			208, 83, 13, 239, 177,
			240, 174, 76, 18, 145,
			207, 45, 115, 202, 148,
			118, 40, 171, 245, 23,
			73, 8, 86, 180, 234, 105,
			55, 213, 139, 87, 9, 235,
			181, 54, 104, 138, 212,
			149, 203, 41, 119, 244,
			170, 72, 22, 233, 183,
			85, 11, 136, 214, 52,
			106, 43, 117, 151, 201,
			74, 20, 246, 168, 116,
			42, 200, 150, 21, 75,
			169, 247, 182, 232, 10,
			84, 215, 137, 107, 53]

    def __init__(self, initial_string=b''):
        """Create a new crc8 hash instance."""
        self._sum = 0x00
        self._update(initial_string)

    def update(self, bytes_):
        """Update the hash object with the string arg.

        Repeated calls are equivalent to a single call with the concatenation
        of all the arguments: m.update(a); m.update(b) is equivalent
        to m.update(a+b).
        """
        self._update(bytes_)

    def digest(self):
        """Return the digest of the bytes passed to the update() method so far.

        This is a string of digest_size bytes which may contain non-ASCII
        characters, including null bytes.
        """
        return self._digest()

    def hexdigest(self):
        """Return digest() as hexadecimal string.

        Like digest() except the digest is returned as a string of double
        length, containing only hexadecimal digits. This may be used to
        exchange the value safely in email or other non-binary environments.
        """
        return hex(self._sum)[2:].zfill(2)

    def string2Hex(self, string):
        bytes = []
        for i in range(len(string) / 2):
            pos = i * 2;
            byte = string[i]
            high = int(string[pos], 16) << 4;
            int
            low = int(string[pos + 1], 16);
            bytes.append(high | low)
        return bytes
        
    if PY2:
        def _update(self, bytes_):
            if isinstance(bytes_):
                bytes_ = bytes_.encode()
            elif isinstance(bytes_, str):
                bytes_ = self.string2Hex(bytes_)
                if len(bytes_) % 2 != 0:
                    raise TypeError("The length of string must be even number")
            table = self._table
            _sum = self._sum
            for byte in bytes_:
                _sum = table[(_sum^byte)]
            self._sum = _sum

        def _digest(self):
            return chr(self._sum)
    else:
        def _update(self, bytes_):
            if isinstance(bytes_, str):
                raise TypeError("Unicode-objects must be encoded before"\
                                " hashing")
            elif not isinstance(bytes_, (bytes, bytearray)):
                raise TypeError("object supporting the buffer API required")
            table = self._table
            _sum = self._sum
            for byte in bytes_:
                _sum = table[_sum^byte]
            self._sum = _sum
            
        def _digest(self):
            return bytes([self._sum])
    
    def copy(self):
        """Return a copy ("clone") of the hash object.
        
        This can be used to efficiently compute the digests of strings that
        share a common initial substring.
        """
        crc = crc8()
        crc._sum = self._sum
        return crc

__all__ = ['crc8']
if __name__ == '__main__':
    cr = crc8()
    print(bytes(bytearray.fromhex("AAFF01000B00020201000000000000000005000191039E02")))
    cr.update(bytes(bytearray.fromhex("AAFF01000B00020201000000000000000005000191039E")))

    print(cr.hexdigest())
