#/usr/bin/env bash
. set_default_server.sh
(cd typescript && npm install && ./test.sh)
(cd python/test && ./test.sh)
