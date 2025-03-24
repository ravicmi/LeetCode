class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sen_out = []
        trailing = 'a'
        vowels = ['a', 'e', 'i', 'o', 'u']
        sentence = sentence.split(' ')
        for w in sentence:
            if w[0].lower() in vowels: 
                w_out = w+'ma'+trailing
            else: 
                w_out = w[1:]+w[0]+'ma'+trailing
            sen_out.append(w_out)
            trailing += 'a'
        return ' '.join(sen_out)

