#include <bits/stdc++.h>
using namespace std;

template <int char_size, int margin>
struct Trie{
    struct TrieNode{
        int nxt[char_size];
        vector<int> idx;
        TrieNode(){
            fill(nxt, nxt+char_size, -1);
        }
    };

    vector<TrieNode> nodes;
    Trie(){
        nodes.push_back(TrieNode());
    };
    void add(const string &str, int id){
        int node_index = 0;
        nodes[0].idx.push_back(id);
        for(int i=0;i<int(str.size());i++){
            int c = str[i] - margin;
            if(nodes[node_index].nxt[c] == -1){
                nodes[node_index].nxt[c] = int(nodes.size());
                nodes.push_back(TrieNode());
            }
            node_index = nodes[node_index].nxt[c];
            nodes[node_index].idx.push_back(id);
        }
    }
    void add(const string &str){
        add(str, int(nodes[0].idx.size()));
    }
    int find(const string &str){
        int node_index = 0;
        for(int i=0;i<int(str.size());i++){
            int c = str[i] - margin;
            if(nodes[node_index].nxt[c] == -1){
                return -1;
            }
            node_index = nodes[node_index].nxt[c];
        }
        return node_index;
    }
};

int N, Q;
vector<string> words;
Trie<26, 'a'> trie;
vector<int> ls;

int main() {
    cin >> N >> Q;
    words.resize(N);
    for(int i=0;i<N;i++) cin >> words[i];
    sort(words.begin(), words.end());
    // suffix trie木の構築
    for(int i=0;i<N;i++){
        reverse(words[i].begin(), words[i].end());
        trie.add(words[i]);
        reverse(words[i].begin(), words[i].end());
    }
    string pre, suf;
    for(int i=0;i<Q;i++){
        cin >> pre >> suf;
        // suffixの一致するnodeを探索
        reverse(suf.begin(),suf.end());
        int id = -1;
        if((id = trie.find(suf)) < 0 || id >= trie.nodes.size()){
            cout << 0 << endl;
            continue;
        }
        ls = trie.nodes[id].idx;  // suffixの一致する文字列の番号集合
        // prefixを二分探索
        int lo, hi;
        lo = lower_bound(words.begin(), words.end(), pre) - words.begin();
        lo = lower_bound(ls.begin(), ls.end(), lo) - ls.begin();
        pre += '~';
        hi = lower_bound(words.begin(), words.end(), pre) - words.begin();
        hi = lower_bound(ls.begin(), ls.end(), hi) - ls.begin();
        cout << hi - lo << endl;
    }
    return 0;
}

