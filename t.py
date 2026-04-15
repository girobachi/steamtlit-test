import MeCab

tagger = MeCab.Tagger()
text = "愛しながら運動している。"
node = tagger.parseToNode(text)

while node:
    if node.surface.strip():
        print(node.surface, "->", node.feature)
    node = node.next