from bigchaindb_driver import BigchainDB
from create import create_tx
from transfer import transfer_tx
import logging


def process(materials, recovery, owner, name, size, unit, place, manufacturer, amount):
    logger = logging.getLogger(__name__)
    # from utils import valid
    # from transfer import transfer_tx
    bdb = BigchainDB('http://localhost:9984/api/v1')
    # alice = generate_keypair()
    # asset = create_asset('gangtie', 'kg', 'wuhan', 'zt')
    # id = create_tx(alice, 'gangtie', 'g', 'shenyang', 'zt', 1, 1, 1,materials[0])
    # valid(id)
    # # asset2 = create_asset('gangtie2', 'kg2', 'wuhan2', 'zt2')
    # tx = bdb.transactions.retrieve(id)
    # bog = generate_keypair()
    # id2 = transfer_tx(alice, tx, bog, 1)
    # logging.basicConfig(format='%(asctime)-15s %(status)-3s %(message)s')

    for m in materials:
        transfer_tx(owner, m['id'], recovery, m['amount'], 'USE')
    create_tx(owner, name=name, size=size, unit=unit, place=place, manufacturer=manufacturer, amount=amount,
              materials=materials, type='MID_Material',detail="use the materials produce the "+name)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')
    logger.info("produce some material:%s", id)
