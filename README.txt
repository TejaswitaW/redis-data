> docker cp "D:\redis-data\bulk_data.txt" redis:/data/bulk_data.txt

Successfully copied 6.14kB to redis:/data/bulk_data.txt

> docker exec -it redis /bin/bash

root@8aa1b6515bb8:/data# cat /data/bulk_data.txt | redis-cli --pipe
All data transferred. Waiting for the last reply...
Last reply received from server.
errors: 0, replies: 165