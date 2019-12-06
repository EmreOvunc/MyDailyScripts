#!/bin/bash
for i in {128..255}; do
	IPs=`cat 10.128.0.0.gnmap | cut -d" " -f2 | grep "10.$i." > _$i`
	size=`ls -la _$i | cut -d" " -f5`
	if [[ $size == 0 ]]; then
		rm -rf _$i
	fi
done
exit 0
