# Python_Git_Linux_Project

1. Find a website that have some dynamic information which changes each minute or so.
https://www.coingecko.com/en/coins/magic

2. That specific information should be (scrapped) using bash.
curl -s https://www.coingecko.com/en/coins/magic > magic_price.txt

sudo yum install nano

sudo yum install python-pip

pip install dash

pip install pandas

python project_SF.py 

curl -s https://www.coingecko.com/en/coins/magic > magic.html

name=$(grep -m 1 '<h1 class="coin-name">' magic.html | sed -n 's/.*<h1 class="coin-name">\(.*\)<\/h1>/\1/p' | sed 's/^\s*//;s/\s*$//')

symbol=$(grep -m 1 '<span class="coin-symbol">' magic.html | sed -n 's/.*<span class="coin-symbol">\(.*\)<\/span>/\1/p' | sed 's/^\s*//;s/\s*$//')

price=$(grep -m 1 '<span class="no-wrap">' magic.html | sed -n 's/.*<span class="no-wrap">\(.*\)<\/span>/\1/p' | sed 's/^\s*//;s/\s*$//')

market_cap=$(grep '<div class="stats-container">' magic.html | grep '<div class="value">' | awk 'NR==2' | sed -n 's/.*<div class="value">\(.*\)<\/div>/\1/p' | sed 's/^\s*//;s/\s*$//')

echo "Nom, Symbole, Prix, Capitalisation boursière" > magic_data.csv

echo "$name, $symbol, $price, $market_cap" >> magic_data.csv

rm magic.html

