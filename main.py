class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''


codes = dict()

def Codes(node, val=''):
    newVal = val + str(node.code)
    if(node.left):
        Codes(node.left, newVal)
    if(node.right):
        Codes(node.right, newVal)
    if(not node.left and not node.right):
        codes[node.symbol] = newVal
    return codes

def Dictionary(text):
    dictionary = dict()
    for element in text:
        if dictionary.get(element) == None:
            dictionary[element] = 1
        else:
            dictionary[element] += 1
    return dictionary


def Coding(text):
    dictionary = Dictionary(text)
    chars = dictionary.keys()


    #print("Znaki: ",list(chars))
    #print("Częstotliwość: ",list(dictionary.values()))
    nodes = []
    for symbol in chars:
        nodes.append(Node(dictionary.get(symbol), symbol))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = Codes(nodes[0])
    print("Słownik:")
    for key, value in huffman_encoding.items():
        print('%s:%s' % (key, value))

    encoded_output = []
    for i in text:
        encoded_output.append(huffman_encoding[i])
    string = ''.join([str(item) for item in encoded_output])

    file2 = open("coded.txt", "w")
    for key, value in huffman_encoding.items():
        file2.write('%s:%s\n' % (key, value))

    file2.write(string)
    file2.close()

    return string, nodes[0]


def Decoding(encoded, tree):
    tree_peak = tree
    decoded= []
    for i in encoded:
        if i == '1':
            tree = tree.right
        elif i == '0':
            tree = tree.left
        try:
            if tree.left.symbol == None and tree.right.symbol == None:
                pass
        except AttributeError:
            decoded.append(tree.symbol)
            tree = tree_peak

    string = ''.join([str(item) for item in decoded])
    return string



file = open("text.txt")
text = file.read()
file.close()
encoding, tree = Coding(text)
print("Zakodowany tekst", encoding)
#print("Odkodowany output", Decoding(encoding,tree))


