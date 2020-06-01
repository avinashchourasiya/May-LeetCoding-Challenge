class Trie:

    def __init__(self):
        self.stack=[];


    def insert(self, word: str) -> None:
        self.stack.append(word);

    def search(self, word: str) -> bool:
        return word in self.stack;

    def startsWith(self, prefix: str) -> bool:
        if(len(self.stack)>0):
            return (self.stack[-1].startswith(prefix));
        return False;


trie=Trie();
print(trie.startsWith("app"));
# trie.insert("apple");
# print(trie.search("apple"));   # returns true
# print(trie.search("app"));     # returns false
# print(trie.startsWith("app")); # returns true
# trie.insert("app");
# print(trie.search("app"));     # returns true
["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
[[],     ["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
 [null,   null,     null,    null,     null     ,null, null,      false,   true,   false,   false,      false,   false,  false,   true,    true,    false,  false, false,   false,     false,    false,   true,   false,  false]