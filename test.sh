#/usr/bin/env bash
export SERVER_ADDRESS=az.hopto.org
export SERVER_PORT=8000
(cd typescript && ./test.sh)
(cd python/test && ./test.sh)
