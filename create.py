from bigchaindb.common.transaction import Asset
from bigchaindb_driver import BigchainDB
import time

def create_tx(creater,name, size,unit, place, manufacturer,detail, amount=1,materials=None,type='material'):

    bdb = BigchainDB('http://localhost:9984/api/v1')
    timeStamp = time.strftime('%Y-%m-%d %X', time.localtime())
    metadata = {'timestamp': timeStamp,'detail':detail}
    # from bigchaindb_driver.crypto import generate_keypair
    #
    # alice = generate_keypair()
    # carly = generate_keypair()
    if amount>1:
        asset = {
            'divisible': True,
            'data': {
                'name': name,
                'size':size,
                'unit':unit,
                'place': place,
                'manufacturer': manufacturer,
                'type': type,

                'materials': materials
            },

        }
        prepared_creation_tx = bdb.transactions.prepare(
            operation='CREATE',
            owners_before=creater.verifying_key,
            asset=asset,
            metadata=metadata,
            owners_after=[([creater.verifying_key], amount)]
        )
    else:
        asset = {

            'data': {
                'name': name,
                'size': size,
                'unit': unit,
                'place': place,
                'manufacturer': manufacturer,
                'type': type,
                'materials': materials
            },

        }
        prepared_creation_tx = bdb.transactions.prepare(
            operation='CREATE',
            owners_before=creater.verifying_key,
            asset=asset,
            metadata=metadata,

        )
        print(creater.signing_key)
    fulfilled_creation_tx = bdb.transactions.fulfill(
        prepared_creation_tx, private_keys=creater.signing_key)

    sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)
    return fulfilled_creation_tx['id']