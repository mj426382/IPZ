#!/bin/bash
for filename in *.pdb; do
	pdb_delhetatm "$filename" > "nohetatm_$filename"
done
