calls = 0
def count_calls():
    global calls
    calls = calls+1
def string_info(string):
         count_calls()
         t = (len(string), string.upper(), string.lower())
         return t
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string in list_to_search:

             print(True)
        else:
             print(False)

print(string_info('Capibara'))
print(string_info('Армагеддон'))
print(is_contains('cycle', ['recycling',  'cyclik']))
print(calls)
print (is_contains)('Urban', ['ban', 'BaNaN', 'urBAN'])












