
# GLOBAL VARIABLES FOR LestoBot - Luca Scotton

import private_info # python file where my private info are stored. It's not syncronized with online repository

TOKEN = private_info.TOKEN # set your own Telegram Bot token
MY_TELEGRAM_ID = private_info.MY_TELEGRAM_ID # set your own Telegram user ID
REFRESH_TIME = 60       # expressed in seconds
CACHED_ANNOUNCES = 40   # max annunci in cache
CACHE_FILE = "cache.bin"

LOOKUP_STRING = "6000"      # case sensitive (scrivere solo in minuscolo)
PAGES_LIST = ["http://www.subito.it/annunci-italia/vendita/fotografia/?q=sony"]


#PAGES_LIST = [
#    "http://www.subito.it/annunci-trentino-alto-adige/vendita/fotografia/?q=sony",
#    "http://www.subito.it/annunci-veneto/vendita/fotografia/?q=sony",
#    "http://www.subito.it/annunci-veneto/vendita/fotografia/?q=sony&o=2"
#]
