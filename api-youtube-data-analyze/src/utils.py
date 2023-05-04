from unidecode import unidecode
import string
import demoji

class Utils: 
    def remove_duplicates(self, full_list, key):
        dictionary = {}
        for item in full_list:
            video_id = item[key]
            dictionary[video_id] = item
        return list(dictionary.values())

    def remove_emojis(self, text):
        return demoji.replace(text, '')
    
    def remove_escape_characters(self, text):
        return unidecode(
            text.replace('\n', '')
                .replace('\"', '`')
                .replace('\r', '')
                .replace('\t', '')
                .replace('\\', '')
        )
    
    def remove_duplicate_spaces(self, text):
        return ' '.join(text.split())
    
    def remove_numbers(self, text):
        return ''.join(caracter for caracter in text if not caracter.isdigit())    

    def remove_special_characters(self, text):
        return ''.join(caracter for caracter in text if caracter not in string.punctuation)
    
    
    def clear_text(self, text):
            return self.remove_duplicate_spaces(
                self.remove_escape_characters(
                    self.remove_emojis(text),
                )
            )