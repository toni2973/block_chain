from bigchaindb_driver import BigchainDB
from create import create_tx
from transfer import transfer_tx
import logging


def process(materials, recovery, owner, name, size, unit, place, manufacturer, amount):
    logger = logging.getLogger(__name__)
    bdb = BigchainDB('http://localhost:9984/api/v1')

    # 消耗原材料或者中间产物
    for m in materials:
        transfer_tx(owner, m['id'], recovery, m['amount'], 'USE')

    # 生成新的中间产物或最终产品
    create_tx(owner, name=name, size=size, unit=unit, place=place, manufacturer=manufacturer, amount=amount,
              materials=materials, type='MID_Material', detail="use the materials produce the " + name)
    logger.info("produce some material:%s", id)



