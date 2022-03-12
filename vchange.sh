#!/bin/bash

if [[ $# -eq 2 ]]; then
  PREV=$1
  NEXT=$2
  
  echo "Changing version: $PREV -> $NEXT";
else
  echo "Expected 2 arguments: PREV_VERSION / NEXT_VERSION";
  return 1;
fi

for f in setup.cfg .vscode/launch.json mkdocs.yml src/rmlab/_version.py; do
  sed -i "s/$PREV/$NEXT/g" $f
done
