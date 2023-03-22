import json, sys, zlib, base45, cbor2
from cose.messages import CoseMessage

#payload = sys.argv[1][4:] # trim "HC1:" prefix

payload = '6BFNX1:HM*I0PS3TLU.NGMU5AG8JKM:SF9VN1RFBIKJ:3AXL1RR+ 8::N$OAG+RC4NKT1:P4.33GH40HD*98UIHJIDB 4N*2R7C*MCV+1AY3:YP*YVNUHC.G-NFPIR6UBRRQL9K5%L4.Q*4986NBHP95R*QFLNUDTQH-GYRN2FMGO73ZG6ZTJZC:$0$MTZUF2A81R9NEBTU2Y437XCI9DU 4S3N%JRP:HPE3$ 435QJ+UJVGYLJIMPI%2+YSUXHB42VE5M44%IJLX0SYI7BU+EGCSHG:AQ+58CEN RAXI:D53H8EA0+WAI9M8JC0D0S%8PO00DJAPE3 GZZB:X85Y8345MOLUZ3+HT0TRS76MW2O.0CGL EQ5AI.XM5 01LCWBA.RE.-SUYH+S7SBE0%B-KT+YSMFCLTQQQ6LEHG.P46UNL6DA2C$AF-SQ00A58HYO5:M8 7S$ULGC-IP49MZCSU8ST3HDRJNPV3UJADJ9BVV:7K13B4WQ+DCTEG4V8OT09797FZMQ3/A7DU0.3D148IDZ%UDR9CYF'


unradix = base45.b45decode(payload)
decompr = zlib.decompress(unradix)
cose = CoseMessage.decode(decompr)
represt = cbor2.loads(cose.payload)

print(represt)

print(f"Issuing country: {represt[1]}")
print(f"Unique vaccination ID: {represt[-260][1]['v'][0]['ci']}")
print(f"Name of recipient: {represt[-260][1]['nam']['gn']} {represt[-260][1]['nam']['fn']}")
