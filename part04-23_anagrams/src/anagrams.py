# Write your solution here
def anagrams(word1, word2):
    list_w1 = []
    for char in word1:
        list_w1.append(char)
    list_w2 = []
    for char in word2:
        list_w2.append(char)
    return sorted(list_w1) == sorted(list_w2)
    
if __name__ == "__main__":
    print(anagrams("tame", "meta"))