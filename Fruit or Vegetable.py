x = input()


dict = {'fruit':['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes'],'vegetable':['tomato', 'cucumber', 'pepper', 'carrot']}

if x in dict.get('fruit'):
    print('fruit')
elif x in dict.get('vegetable'):
    print('vegetable')
else:
    print('unknown')

