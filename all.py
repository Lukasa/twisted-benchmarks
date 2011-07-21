
from twisted.python.reflect import namedAny

from benchlib import multidriver

allBenchmarkNames = [
    "iteration", "names", "threads", "web", "pb", "amp",
    "deferred_callback_chains",
    "linereceiver", "lineonlyreceiver","int16receiver",

    "tcp_connect", "ssh_connect", "ssl_connect", "sslbio_connect",
    "tcp_throughput", "ssh_throughput", "ssl_throughput", "sslbio_throughput",
    ]

allBenchmarks = []

for name in allBenchmarkNames:
    name = name + '.main'
    try:
        main = namedAny(name)
    except Exception, e:
        print 'Skipping', name, ':', e
    else:
        allBenchmarks.append(name)

if __name__ == '__main__':
    multidriver(allBenchmarks)
