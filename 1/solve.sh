#!/usr/bin/env bash

ELF=0
TOTAL=0
ELVES=()

while read -r line; do
	if [[ -z "$line" ]]; then
		ELVES+=(${TOTAL})
		ELF=$((ELF + 1))
		TOTAL=0
		continue
	fi
	TOTAL=$((TOTAL + line))
done < input

IFS=$'\n' sorted=($(sort -nr <<<"${ELVES[*]}"))

biggest="${sorted[0]}"

for (( elf=0; elf<ELF; elf++ )); do
	if [[ biggest -eq "${ELVES[$elf]}" ]]; then
		echo Elf $((elf + 1)) has the most calories at ${biggest}.
	fi
done

echo The top 3 elves have a total of $(( sorted[0] + sorted[1] + sorted[2] )) calories.
