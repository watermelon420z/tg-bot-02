import wikipedia


wikipedia.set_lang("ru")

def search_wiki(word):
    try:
        w = wikipedia.search(word)
        if  w:
            w2 = wikipedia.page(word).url
            w1 = wikipedia.summary(word)
            return w1, f"\nСсылка: {w2}"
        return  "По запросу {word} ничего не найдено!", ""
    except:
        return "Произошла ошибка", ""
