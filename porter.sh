#!/bin/bash

filename="image.conf"
while read -r line; do
    if  [[ $line == \#* ]] ;
    then
        continue
    fi

    s2d=${line//,/ }
    docker pull ${s2d[0]}
    docker tag ${s2d[0]} ${s2d[1]}
    docker push ${s2d[1]}

done < "$filename"