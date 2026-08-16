#include <bits/stdc++.h>

using ll = long long;

template <typename T> T inf;
template <> constexpr int inf<int> = 1e9;
template <> constexpr ll inf<ll> = 1e18;

constexpr int M = 1e9 + 7;


class aho_corasick {
    struct PMA {
        std::weak_ptr<PMA> fail;
        std::vector<std::shared_ptr<PMA>> next;
        std::vector<int> accept;

        PMA()
            : fail(), next(alphabets)
        {}
    };

public:
    aho_corasick(std::vector<std::string> const& ts)
        : K(ts.size()), root(std::make_shared<PMA>())
    {
        root->fail = root;
        for(int i = 0; i < K; ++i) {
            PMA* t = root.get();
            for(auto cc : ts[i]) {
                int c = cc - alphabet_base;
                if(!t->next[c]) {
                    t->next[c] = std::make_shared<PMA>();
                }
                t = t->next[c].get();
            }
            t->accept.push_back(i);
        }

        std::queue<std::shared_ptr<PMA>> que;
        for(int c = 0; c < alphabets; ++c) {
            if(root->next[c]) {
                root->next[c]->fail = root;
                que.push(root->next[c]);
            }
        }
        while(!que.empty()) {
            auto t = que.front();
            que.pop();
            for(int c = 0; c < alphabets; ++c) {
                if(t->next[c]) {
                    que.push(t->next[c]);
                    // assert(!t->fail.expired());
                    auto r = t->fail.lock();
                    while(!r->next[c] && r != root) {
                        r = r->fail.lock();
                    }
                    auto& nxt = r->next[c];
                    if(!nxt) { // root
                        nxt = root;
                    }
                    t->next[c]->fail = nxt;
                    for(auto ac : nxt->accept) {
                        t->next[c]->accept.push_back(ac);
                    }
                }
            }
        }
    }

    std::vector<std::vector<int>> match(std::string const& s, std::vector<std::string> const& ts, ll& cnt) {
        std::vector<std::vector<int>> res(K);
        std::vector<ll> dp(s.size() + 1);
        dp[0] = 1;
        PMA* now = root.get();
        for(int i = 0; i < (int)s.size(); ++i) {
            int c = s[i] - alphabet_base;
            while(!now->next[c] && now != root.get()) {
                now = now->fail.lock().get();
            }
            now = now->next[c].get();
            if(now == nullptr) {
                now = root.get();
            }
            for(auto k : now->accept) {
                //res[k].push_back(i);
                (dp[i + 1] += dp[i - ts[k].size() + 1]) %= M;
            }
        }
        cnt = dp[s.size()];
        return res;
    }

private:
    static int const alphabets = 26;      // a-z
    static int const alphabet_base = 'a'; // a
    int const K;
    std::shared_ptr<PMA> root;
};


using namespace std;
int main() {
    int N;
    cin >> N;
    string t;
    vector<string> s(N);
    for(int i = 0; i < N; ++i) {
        cin >> s[i];
    }
    cin >> t;

    aho_corasick aho(s);
    ll res = 0;
    auto match_pos = aho.match(t, s, res);
    cout << res << endl;
}

