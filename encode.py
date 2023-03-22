from cose.messages import Sign1Message
from cose.keys import EC2Key
from cose.headers import Algorithm, KID
from cose.algorithms import Es256
import json, zlib, base45, cbor2, datetime, qrcode, os

now = int(datetime.datetime.now().timestamp())

json_repr = json.load(open("pers_test.json"))
adjusted = {
	1: 'GB',
	4: now + 31536000,
	6: now,
	-260: {
		1: json_repr
	}
}

cbor_repr = cbor2.dumps(adjusted)

private_key = os.urandom(32)
key = EC2Key(
	crv='P_256', 
	d=private_key, 
	optional_params={'ALG': 'ES256'}
)

msg = Sign1Message(
	phdr = {Algorithm: Es256, KID: private_key},
    payload=cbor_repr
)

msg.key = key

cose_repr = msg.encode(message = cbor_repr)


compr = zlib.compress(cose_repr)
base45_enc = base45.b45encode(compr)

res = "HC1:" + base45_enc.decode('utf-8')

img = qrcode.make(res)
img.save("output.png")

print(res)
print(len(res))