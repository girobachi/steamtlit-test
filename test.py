import MeCab

def extract_words(text: str) -> list[str]:
    tagger = MeCab.Tagger()
    node = tagger.parseToNode(text)
    
    results = []
    target_pos = {"名詞", "形容詞", "動詞"}
    exclude_pos_detail = {"非自立可能", "サ変可能"}
    
    while node:
        feature = node.feature.split(",")
        surface = node.surface
        
        if not surface.strip():
            node = node.next
            continue
        
        pos = feature[0]
        pos_detail = feature[1] if len(feature) > 1 else ""
        
        # feature[7]がカタカナならfeature[8]を試す、それもダメならsurface
        base_form = feature[7] if len(feature) > 7 else surface
        if all("\u30A0" <= c <= "\u30FF" for c in base_form):
            base_form = feature[8] if len(feature) > 8 else surface
        
        if pos in target_pos and pos_detail not in exclude_pos_detail:
            results.append(base_form)
        
        node = node.next
    
    return results

if __name__ == "__main__":
    text = "彼女は美しい花を愛し、東京で毎日散歩している。"
    words = extract_words(text)
    print(words)

# import ipadic
# import MeCab

# def extract_words(text: str) -> list[str]:
#     tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
#     node = tagger.parseToNode(text)
    
#     results = []
#     target_pos = {"名詞", "形容詞", "動詞"}
#     exclude_pos_detail = {"非自立", "サ変接続", "接尾"}
    
#     while node:
#         feature = node.feature.split(",")
#         surface = node.surface
        
#         if not surface.strip():
#             node = node.next
#             continue
        
#         pos = feature[0]
#         pos_detail = feature[1] if len(feature) > 1 else ""
#         base_form = feature[6] if len(feature) > 6 else surface
        
#         if pos in target_pos and pos_detail not in exclude_pos_detail:
#             results.append(base_form)
        
#         node = node.next
    
#     return results

# if __name__ == "__main__":
#     text = "彼女は美しい花を愛し、東京で毎日散歩している。"
#     words = extract_words(text)
#     print(words)
#     # ['美しい', '花', '愛する', '東京', '毎日', '散歩']



# import MeCab

# tagger = MeCab.Tagger()
# text = "愛しながら運動している。"
# node = tagger.parseToNode(text)

# while node:
#     if node.surface.strip():
#         print(node.surface, "->", node.feature)
#     node = node.next