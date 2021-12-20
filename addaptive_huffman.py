import time
import bitstring

from huffman_tree import AdaptiveHuffmanTree


class Coder:
    def __init__(self, text=''):
        self.tree = AdaptiveHuffmanTree()
        self.text = text
        self.symbol_dict = {}

    def squeeze(self):
        result = ''
        for symbol in self.text:
            if self.symbol_dict.get(symbol, None):
                bin_code = self.tree.get_path(symbol)
                result += bin_code
            else:
                self.symbol_dict[symbol] = 1
                bin_code = '0' * max(self.tree.count_symbol, 1) + bin(ord(symbol))[2:].zfill(8)
                result += bin_code
            self.tree.add(symbol)
        return result


class Decoder:
    def __init__(self, text=''):
        self.tree = AdaptiveHuffmanTree()
        self.text = text

    def unclench(self):
        result = ''
        current_index = 0
        while current_index < len(self.text):
            end = current_index + max(self.tree.count_symbol, 1)
            if self.text[current_index:end] == '0'*max(self.tree.count_symbol, 1):
                binary_symbol_code = self.text[end: end+8]
                symbol = chr(int(binary_symbol_code, 2))
                end += 8
            else:
                end = self.text.find('1', current_index) + 1
                symbol = self.tree.search_by_path(self.text[current_index:end])
                if symbol == -1:
                    raise Exception('Ошибка, не существует такого кода')
            current_index = end
            result += symbol
            self.tree.add(symbol)
        return result


if __name__ == '__main__':
    time_to_start = time.time()


    with open('picture.jpg', 'rb') as file:
        words = ''.join([chr(i) for i in file.read()])
    # words = ''
    text3 = ''.join([bin(ord(symbol))[2:].zfill(8) for symbol in words])
    c = Coder(words)
    res = c.squeeze()
    print(len(words) * 8, len(res), len(words) * 8 / len(res))
    d = Decoder(res)
    text2 = d.unclench()
    text = ''.join([bin(ord(symbol))[2:].zfill(8) for symbol in text2])
    print(text, '-' * 100)
    time_to_end = time.time()
    print(f'Функция работала {time_to_end - time_to_start} секунд')
    with open('pictureres.jpg', 'wb') as f:
        bitstring.Bits(bin=text).tofile(f)


