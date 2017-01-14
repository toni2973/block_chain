from bigchaindb_driver import BigchainDB
# from bigchaindb_driver.crypto import generate_keypair
from create import create_tx

import logging


def produce(owner, name, size, util, place, manufacturer, detail, amount):
    logger = logging.getLogger(__name__)
    # from utils import valid
    # from transfer import transfer_tx
    # bdb = BigchainDB('http://localhost:9984/api/v1')
    # alice = generate_keypair()
    # asset = create_asset('gangtie', 'kg', 'wuhan', 'zt')
    id = create_tx(creater=owner, name=name, size=size, unit=util, place=place, manufacturer=manufacturer, detail=detail,
                   amount=amount)
    # valid(id)
    # # asset2 = create_asset('gangtie2', 'kg2', 'wuhan2', 'zt2')
    # tx = bdb.transactions.retrieve(id)
    # bog = generate_keypair()
    # id2 = transfer_tx(alice, tx, bog, 1)
    # logging.basicConfig(format='%(asctime)-15s %(status)-3s %(message)s')
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')
    logger.info("produce some material:%s", id)
