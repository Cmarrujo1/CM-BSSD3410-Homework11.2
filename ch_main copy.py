
# source code taken from: https://rosettacode.org/wiki/Markov_chain_text_generator#Procedural
# no author listed
# Content is available under GNU Free Document License 1.3 unless otherwise noted.
# accessed on: 10/24/24

import random, sys


def makerule(data, context):
    '''Make a rule dict for given data.'''
    rule = {}
    words = data#.split(' ')
    index = context

    for word in words[index:]:
        print("word:", word)
        key = ''.join(words[index - context:index])
        print("key:", key)
        if key in rule:
            rule[key].append(word)
        else:
            rule[key] = [word]
        index += 1
    print(rule)
    return rule


def makestring(rule, length):
    '''Use a given rule to make a string.'''
    oldwords = random.choice(list(rule.keys()))
    print("starting with:", oldwords)
    string = oldwords

    for i in range(length):
        try:
            key = ''.join(oldwords)
            print("key:", key)
            newword = random.choice(rule[key])
            string += newword
            oldwords = oldwords [1:] + newword
            print("onm:", oldwords)

        except KeyError:
            print("key error:", key)
            return string
    return string


if __name__ == '__main__':
    with open('alice_oz.txt', encoding='utf8') as f:
        data = f.read()
    #data = "anne and anna are angry"
    rule = makerule(data, 4)
    string = makestring(rule, 10)
    print(string)