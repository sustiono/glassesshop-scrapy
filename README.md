# Bestsellers Glassesshop Scrapy

Scrap best seller Products from https://www.glassesshop.com/bestsellers using Scrapy

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some packages needed.

```bash
git clone git@github.com:sustiono/glassesshop-scrapy.git
cd glassesshop-scrapy
pip3 install virtualenv
virtualenv .env
source .env/bin/activate
cd glassesshop
pip install -r requirements.txt
```

## Usage
Choose one of the commands below to get the results in the desired format

```bash
scrapy crawl bestsellers -o bestsellers.csv
scrapy crawl bestsellers -o bestsellers.json
scrapy crawl bestsellers -o bestsellers.xml
```
