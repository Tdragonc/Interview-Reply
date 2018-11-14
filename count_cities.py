import csv

def sep(sent):
    return sent.split(' ')

def cap(word):
    return word.capitalize()

def cap_word(lists):
    lists1 = []
    for a in lists:
        leng = len(sep(a))
        sent = sep(a)
        if leng == 1:
            lists1 += [ cap(a) ]
        else:
            lists2 = []
            for b in sent:
                lists2 += [cap(b)]
            c = comb_list_sent(lists2)
            lists1 += [c]
    return lists1

def check_word_in_cities(word):
    with open('worldcities.csv','r') as cities_csv:
        cities_read = csv.reader(cities_csv)

        for line in cities_read:
            if word in line:
                return word

def check_word_in_countries(word):
    with open('countries.csv','r') as countries_csv:
        countries_read = csv.reader(countries_csv)

        for line in countries_read:
            line1 = []
            for a in line:
                line1 += [ a[3:] ]
            line1 += ['Us', 'Uk', 'N Korea', 'S Korea']
            if word in line1 :
                return word

def check_list_words_cities_countries(lists):
    lists1 = []
    for a in lists:
        if check_word_in_cities(a):
            lists1 += [a]
        elif check_word_in_countries(a):
            lists1 += [a]
    return lists1

def comb_list_sent(lists):
    leng = len(lists)
    a = 0
    sent = ''
    while a < leng:
        if a < leng-1:
            sent += lists[a] +' '
            a += 1
        else:
            sent += lists[a]
            a += 1
    return cap(sent[0]) + sent[1:]

def is_not_capitalized(word):
    if word != word.capitalize():
        return True
    else:
        return False

def re_arrange(sentence):
    sent = sep(sentence)
    leng = len(sent)
    lists1 = []
    a = 0
    for a in sent:
        if is_not_capitalized(a) and a not in lists1 and a.capitalize() not in lists1:
            lists1 += [a]
        elif not is_not_capitalized(a) and a.lower() in lists1:
            lists1.remove(a.lower())
            lists1.append(a)
        elif not is_not_capitalized(a) and a not in lists1:
            lists1.append(a)
    return lists1 
    
def re_write(lists):
    lists1 = []
    for a in lists:
        sent = sep(a)
        leng = len(sent)
        if leng == 1:
            if cap(a) in check_list_words_cities_countries(cap_word(lists)):
                lists1 += [cap(a)]
            else:
                lists1 += [a]
        else:
            if comb_list_sent(cap_word(sent)) in check_list_words_cities_countries(cap_word(lists)):
                lists1 += [comb_list_sent(cap_word(sent))]
            else:
                lists1 += [a]
    return comb_list_sent(re_arrange(comb_list_sent(lists1)))

def comp_2_words(sentence):
    sent = sep(sentence)
    leng = len(sent)
    a = 0
    lists1 = []
    while a < leng - 1:
        lists1 += [ sent[a] + ' ' + sent[a+1] ]
        a += 1
    return lists1

def comp_3_words(sentence):
    sent = sep(sentence)
    leng = len(sent)
    a = 0
    lists1 = []
    while a < leng - 2:
        lists1 += [ sent[a] + ' ' + sent[a+1] + ' ' + sent[a+2] ]
        a += 1
    return lists1

def remove_change(sentence):
    sent = cap_word(sep(sentence))
    sent_1 = cap_word(comp_2_words(sentence))
    sent_2 = cap_word(comp_3_words(sentence))
    if check_list_words_cities_countries(sent) != []:
        return re_write(sep(sentence))
    elif check_list_words_cities_countries(sent_1) != []:
        return re_write(comp_2_words(sentence))
    elif check_list_words_cities_countries(sent_2) != []:
        return re_write(sep(sentence))
    else:
        return []

def count_cap(sentence):
    sent = sep(sentence)
    a = 0
    for b in sent:
        if not is_not_capitalized(b):
            a += 1
    return a



with open('abcnews-date-text.csv','r') as news_csv:
    news_read = csv.reader(news_csv)

    next(news_read)

    with open('new_abcnews_1.csv', 'w' ) as new_news:
        news_write = csv.writer(new_news)

        a = 1
        for line in news_read:
            a += 1
            if remove_change(line[1]) == []:
                continue
            else:
                line_1 = remove_change(line[1])
                print(a)
                news_write.writerow([line[0], line_1])

