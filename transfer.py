from bigchaindb_driver import BigchainDB
import time


#
# def create_asset(name, spec, place, manufacturer, type='material', amount=1):
#     asset = {
#         'data': {
#             'name': name,
#             'spec': spec,
#             'amount': amount,
#             'place': place,
#             'manufacturer': manufacturer,
#             'type': type
#         },
#
#     }
#     return asset


def transfer_tx(owner_before, id, owner_after, transfer_amount, type,detail, *args):
    bdb = BigchainDB('http://localhost:9984/api/v1')
    timeStamp = time.strftime('%Y-%m-%d %X', time.localtime())
    metadata = {'timestamp': timeStamp, 'type': type,'detail':detail}
    input_tx = bdb.transactions.retrieve(id)

    # from bigchaindb_driver.crypto import generate_keypair
    #
    # alice = generate_keypair()
    # carly = generate_keypair()
    condition = input_tx['transaction']['conditions'][0]

    transfer_input = {
        'fulfillment': condition['condition']['details'],
        'input': {
            'cid': 0,
            'txid': input_tx['id'],
        },
        'owners_before': condition['owners_after'],

    }
    amount = input_tx['transaction']['conditions'][0]['amount']
    prepared_creation_tx = bdb.transactions.prepare(
        operation='TRANSFER',
        owners_before=owner_before.verifying_key,
        asset=input_tx['transaction']['asset'],
        metadata=metadata,
        inputs=transfer_input,
        owners_after=[([owner_after.verifying_key], transfer_amount),
                      ([owner_before.verifying_key], amount - transfer_amount)] if
        input_tx['transaction']['asset']['divisible'] and amount - transfer_amount > 0 else [
            ([owner_after.verifying_key], transfer_amount)]
    )

    fulfilled_creation_tx = bdb.transactions.fulfill(
        prepared_creation_tx, private_keys=owner_before.signing_key)

    sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)

    return fulfilled_creation_tx['id']
