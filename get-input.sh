#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "${SCRIPT_DIR}" || exit 1

if [[ -n "$1" ]]; then
  DAY=$1
else
  printf "Please enter the day number.\n"
  exit 2
fi

if [[ ! -e "${SCRIPT_DIR}/cookie.txt" ]]; then
  echo Please create the file \""${SCRIPT_DIR}"/cookie.txt\" which should contain your session cookies for adventofcode.com.
  exit 3
fi

if [[ ! -d "${DAY}" ]]; then
  mkdir "${DAY}"
fi

cd "${DAY}" || exit 4

curl 'https://adventofcode.com/2022/day/'${DAY}'/input' \
  -H 'authority: adventofcode.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H "$(cat ${SCRIPT_DIR}/cookie.txt)" \
  -H 'referer: https://adventofcode.com/2022/day/'${DAY} \
  -H 'sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' \
  --compressed > input.txt || echo Couldn\'t download the day ${DAY} input\!

if [[ ! -e "solve.py" ]]; then
  echo 'def main():
    with open("input.txt", "r") as in_file:
        data = in_file.readlines()


if __name__ == "__main__":
    main()' > solve.py
fi