results = {}


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                string = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    string = string.replace(i, '')
                all_words[file_name] = string.split()
                return all_words

    def find(self, word):
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word.lower() in words:
                results[file_name] = words.index(word.lower()) + 1
        return results

    def count(self, word):
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                results[file_name] = count
        return results


print('test_file:')
finder2 = WordsFinder('test_file.txt')
print('Все слова:', finder2.get_all_words())
print('3 слово по счёту:', finder2.find('TEXT'))
print('4 слова teXT в тексте всего:', finder2.count('teXT'))

print('\n')
print('Mother Goose - Monday’s Child:')
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

print('\n')
print('Rudyard Kipling - If:')
finder1 = WordsFinder('Rudyard Kipling - If.txt')
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

print('\n')
print('Walt Whitman - O Captain! My Captain!:')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
