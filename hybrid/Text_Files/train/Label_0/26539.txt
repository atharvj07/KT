#include <bits/stdc++.h>
#define FOR(i, a, b)    for (int i = a; i <= b; ++i)
#define ii              pair <int, int>
using namespace std;
const int N = 2e5 + 3;
int n, dsu[N];
long long res;
vector <ii> V;
deque <int> dq;

void init() {
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    //freopen("main.inp","r",stdin);
    //freopen("main.out","w",stdout);
}

int root(int x) { return dsu[x] <= 0 ? x : dsu[x] = root(dsu[x]); }
void merge(int u, int v) {
    if (dsu[u] > dsu[v]) swap(u, v);
    dsu[u] += dsu[v], dsu[v] = u;
}

void solve() {
    cin >> n;
    FOR(i, 1, n) { int x; cin >> x; V.push_back({ x, i }); dq.push_back(i); }

    memset(dsu, -1, sizeof dsu);
    sort(V.begin(), V.end());
    for (ii it : V) {
        while (1) {
            int id1 = root(it.second);
            int id2 = root(dq.front()); dq.pop_front();
            if (id2 == id1) break;
            merge(id1, id2);
        }
        int id1 = root(it.second);
        res += 0LL - dsu[id1] - 1; dsu[id1]++;
        if (dsu[id1] < 0) dq.push_back(id1);
    }

    cout << res << '\n';
}

int main() {
    init(); solve();
}

