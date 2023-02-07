#!/bin/bash
for filename in *.pdb; do
	./reduce -BUILD "$filename" > "reduce_$filename" 2>reduce_log.txt
done
