#!/bin/bash
SRC=$1
OUT="icons"
mkdir -p "$OUT"

for SIZE in 16 32 64 128 256 512 1024; do
    sips -z $SIZE $SIZE "$SRC" --out "$OUT/icon_${SIZE}.png" > /dev/null
done

echo "Done → $OUT/"