from bigchaindb_driver import BigchainDB
def valid(id):
    trials = 0
    bdb = BigchainDB('http://localhost:9984/api/v1')
    while bdb.transactions.status(id).get('status') != 'valid' :
        trials += 1
    print(trials)
