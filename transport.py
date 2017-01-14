from bigchaindb_driver import BigchainDB
from create import create_tx
from transfer import transfer_tx
import logging


def transport(owner_before, owner_after, goods_id, amount):
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


    transfer_tx(owner_before=owner_before, id=goods_id, owner_after=owner_after, transfer_amount=amount,
                type='TRANSPORT', detail='')

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='myapp.log',
                        filemode='w')
    logger.info("transport some material:%s from %s to %s", id, owner_before, owner_after)
