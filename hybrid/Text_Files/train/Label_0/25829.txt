#include <bits/stdc++.h>
using namespace std;
#define int long long   // <-----!!!!!!!!!!!!!!!!!!!

#define rep(i,n) for (int i=0;i<(n);i++)
#define rep2(i,a,b) for (int i=(a);i<(b);i++)
#define rrep(i,n) for (int i=(n)-1;i>=0;i--)
#define rrep2(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define all(a) (a).begin(),(a).end()

typedef long long ll;
typedef pair<int, int> Pii;
typedef tuple<int, int, int> TUPLE;
typedef vector<int> V;
typedef vector<V> VV;
typedef vector<VV> VVV;
const int inf = 1e9;
const int mod = 1e9 + 7;

typedef vector<set<int>> Graph;

// false -> "contains cycle"
bool dfs(int now, int start, const Graph &G, vector<bool> &visited) {
    visited[now] = true;
    for (auto nxt : G[now]) {
        if (nxt == start) return false;
        if (!visited[nxt] && !dfs(nxt, start, G, visited)) return false;
    }
    return true;
}

bool isDAG(const Graph &G) {
    int n = G.size();
    rep(i, n) {
        vector<bool> visited(n);
        if (!dfs(i, i, G, visited)) return false;
    }
    return true;
}

bool solve(int n) {
    vector<string> s(n);
    rep(i, n) cin >> s[i];

    Graph G(26);
    rep(l, 10) {
        rep(i, n) {
            rep2(j, i + 1, n) {
                if (s[i].size() >= l && s[j].size() >= l && s[i].substr(0, l) == s[j].substr(0, l)) {
                    if (s[i].size() < l + 1) continue;
                    if (s[j].size() < l + 1) return false;
                    if (s[i][l] == s[j][l]) continue;
                    G[s[i][l] - 'a'].insert(s[j][l] - 'a');
                }
            }
        }
    }

    return isDAG(G);
}

signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int n;
    while (cin >> n, n) {
        cout << (solve(n) ? "yes" : "no") << endl;
    }
}