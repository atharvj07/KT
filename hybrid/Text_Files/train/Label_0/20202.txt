#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using P = pair<int, int>;

class union_find {
public:
    union_find(int n)
        : par_(n, -1)
    {}
    void init(int n) {
        par_.assign(n, -1);
    }

    int root(int x) {
        return par_[x] < 0 ? x : par_[x] = root(par_[x]);
    }

    bool unite(int x, int y) {
        x = root(x); y = root(y);
        if(x == y) {
            return false;
        } else {
            if(par_[x] < par_[y]) {
                par_[x] += par_[y];
                par_[y] = x;
            } else {
                par_[y] += par_[x];
                par_[x] = y;
            }
            return true;
        }
    }

    bool same(int x, int y) {
        return root(x) == root(y);
    }

    int size(int x) {
        return -par_[root(x)];
    }

private:
    std::vector<int> par_;
};

int main() {
    int N;
    cin >> N;
    vector<int> c(N);
    for(int i=0; i<N; ++i) {
        cin >> c[i];
    }
    int M;
    cin >> M;
    union_find uf(N);
    vector<vector<int>> g(N);
    vector<vector<P>> neib(N);
    for(int i=0; i<M; ++i) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        if(c[a] > c[b]) {
            g[b].push_back(a);
        } else if(c[a] < c[b]) {
            g[a].push_back(b);
        } else {
            uf.unite(a, b);
        }
        neib[a].push_back(make_pair(c[b], b));
        neib[b].push_back(make_pair(c[a], a));
    }

    for(int i=0; i<N; ++i) {
        if(neib[i].size() == 0) {
            continue;
        }
        sort(neib[i].begin(), neib[i].end());
        for(int j=0; j<neib[i].size()-1; ++j) {
            P u = neib[i][j], v = neib[i][j+1];
            if(u.first == v.first) {
                uf.unite(u.second, v.second);
            } else {
                g[u.second].push_back(v.second);
            }
        }
    }

    vector<int> order;
    vector<ll> dp(N);
    for(int i=0; i<N; ++i) {
        if(uf.root(i) == i) {
            order.push_back(i);
            dp[i] = 1;
        } else {
            for(auto& v : g[i]) {
                g[uf.root(i)].push_back(v);
                g[i].clear();
            }
        }
    }
    sort(order.begin(), order.end(), [&](int const v1, int const v2) {
        return c[v1] < c[v2];
    });

    ll res = 0;
    for(auto i : order) {
        for(auto to : g[i]) {
            dp[uf.root(to)] = max(dp[uf.root(to)], dp[i]+1);
        }
        res += dp[i] * uf.size(i);
    }
    cout << res << endl;
}