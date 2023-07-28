import random
import jieba

# 1. 随机删除一个字
def random_remove_char(text):
    char_list = list(text)
    if char_list:
        random_idx = random.randint(0, len(char_list) - 1)
        char_list.pop(random_idx)
    return "".join(char_list)


# 2. 随机插入一个字
def random_insert_char(text):
    char_list = list(text)
    random_idx = random.randint(0, len(char_list))
    char_list.insert(random_idx, "随")
    return "".join(char_list)


# 3. 随机2个字交换位置
def random_swap_chars(text):
    char_list = list(text)
    if len(char_list) >= 2:
        idx1, idx2 = random.sample(range(len(char_list)), 2)
        char_list[idx1], char_list[idx2] = char_list[idx2], char_list[idx1]
    return "".join(char_list)


# 4. 随机2个词交换位置（分词）
def random_swap_words(text):
    word_list = list(jieba.cut(text))
    if len(word_list) >= 2:
        idx1, idx2 = random.sample(range(len(word_list)), 2)
        word_list[idx1], word_list[idx2] = word_list[idx2], word_list[idx1]
    return "".join(word_list)


# 5. 随机插入一个符号（不能在头、尾和符号后面插入）
def random_insert_symbol(text):
    char_list = list(text)
    symbol = random.choice("。，！？")
    while True:
        random_idx = random.randint(1,len(char_list))
        if char_list[random_idx-1] not in ['。','，','！','？']:
            char_list.insert(random_idx, symbol)
        if len(char_list) > len(list(text)):
            break
    return "".join(char_list)


# 6. 随机找个字重叠（周杰杰伦）
def random_duplicate_char(text):
    char_list = list(text)
    if char_list:
        random_idx = random.randint(0, len(char_list) - 1)
        char_list.insert(random_idx, char_list[random_idx])
    return "".join(char_list)


# 7. 尾部随机加入语气助词
def add_modal_particle(text):
    modal_particles = ["呀", "啊", "哦", "哇"]
    return text + random.choice(modal_particles)


# 8. 随机找词进行同义词替换（同义字替换）
def random_synonym_replace(text,stopwords, synonyms):

    words = list(text)
    replaced_words = []

    for word in words:
        if word in synonyms:
            synonym_list = synonyms[word]
            replaced_word = synonym_list[0]  # 默认使用同义词表中的第一个同义词
            replaced_words.append(replaced_word)
        else:
            replaced_words.append(word)

    return "".join(replaced_words)


# 9. 随机插入停用词
def random_insert_stopword(text, stopwords,synonyms):
    word_list = list(jieba.cut(text))
    if len(word_list) > 1:
        random_idx = random.randint(1, len(word_list) - 1)
        word_list.insert(random_idx, random.choice(stopwords))
    return "".join(word_list)


# 10. 创建1个方法：输入一条数据，使用run()方法以上9种方式分别输入增强后的结果
def run_data_augmentation(text, stopwords,synonyms):
    augmented_texts = [
        random_remove_char(text),
        random_insert_char(text),
        random_swap_chars(text),
        random_swap_words(text),
        random_insert_symbol(text),
        random_duplicate_char(text),
        add_modal_particle(text),
        random_synonym_replace(text,stopwords,synonyms),
        random_insert_stopword(text, stopwords,synonyms)
    ]
    return augmented_texts


# 11. 创建一个方法：输入一条数据，生成5条增强后的数据，按照抽中1-3的概率50%，抽中4-6的概率30%，抽中7-9的概率20%
def generate_multiple_augmentations(text, stopwords,synonyms):
    augmentation_funcs = [
        random_remove_char, random_insert_char, random_swap_chars,
        random_swap_words, random_insert_symbol, random_duplicate_char,
        add_modal_particle, random_synonym_replace, random_insert_stopword
    ]

    num_augmentations = 5
    augmented_texts = []

    for _ in range(num_augmentations):
        probability = random.random()
        if probability <= 0.5:
            func = random.choice(augmentation_funcs[:3])
            augmented_texts.append(func(text))
        elif probability <= 0.8:
            func = random.choice(augmentation_funcs[3:6])
            augmented_texts.append(func(text))
        elif probability <= 0.9:
            func = random.choice(augmentation_funcs[6:7])
            augmented_texts.append(func(text))
        else:
            func = random.choice(augmentation_funcs[7:])
            augmented_texts.append(func(text, stopwords,synonyms))

    return augmented_texts


# 示例用法：
if __name__ == "__main__":
    synonyms = {
        "玩": ["游玩", "玩耍", "游逛"],
        "好": ["优秀", "出色", "棒"],
        # Add more synonyms as needed
    }
    text = '今天天气真好，我们一起出去玩吧！'
    stopwords = ["一起", "真好"]

    print("单条数据增强：")
    augmented_texts = run_data_augmentation(text, stopwords,synonyms)
    for idx, augmented_text in enumerate(augmented_texts, 1):
        print(f"{idx}. {augmented_text}")

    print("\n多条数据增强：")
    multiple_augmented_texts = generate_multiple_augmentations(text, stopwords,synonyms)
    for idx, augmented_text in enumerate(multiple_augmented_texts, 1):
        print(f"{idx}. {augmented_text}")
