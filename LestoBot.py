import telepot
import time
import string
import subito_scraper as ss
import myvariables as myvar

token = myvar.TOKEN
MY_TELEGRAM_ID = myvar.MY_TELEGRAM_ID


def main():

    intro()
    
    bot = telepot.Bot(token)
    now = []
    prev = importCache()
    max_prev_cache = myvar.CACHED_ANNOUNCES
    refresh = myvar.REFRESH_TIME

    while True:
        import subito_scraper as ss
        now = ss.getAnnounces()
        now = list( set(now) - set(prev) )
        notifyMe(now,bot)
        if(len(now) is 0):
            print("---")
        prev = now + prev
        if len(prev) > max_prev_cache:
            removeOlds(prev,max_prev_cache)
        
        exportCache(prev)
        
        time.sleep(refresh)

def removeOlds(lista,maxsize):
    while len(lista) > maxsize:
        lista.pop()

def notifyMe(news,bot):
    for (i,l,d,pos) in news:
        message = d+" - "+pos+"\n"+i
        message = message.title()+"\n"+l
        print(message)
        bot.sendMessage(MY_TELEGRAM_ID, message)

def exportCache(lista):
    filename = myvar.CACHE_FILE
    with open(filename, 'w') as f:
        for (i,l,d,pos) in lista:
            tmp = i+"|"+l+"|"+d+"|"+pos
            print(tmp,file = f)
        f.close()
    print("Cache exported.")
    
def importCache():
    filename = myvar.CACHE_FILE
    lista = list()
    try:
        with open(filename, 'r') as f:
            for line in f:
                row = tuple(line.replace('\n','').split('|'))
                lista.append(row)
        print("Cache imported.")
    except:
        pass
    return lista
def intro():
    print("\n\t/\\/  LestoBot - Luca Scotton  \\/\\\n")
    print("\t     the all in none solution\n\n")
main()
























