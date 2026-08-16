#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <queue>
#include <bitset>
#include <stack>
#include <functional>

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 42
#endif

#define rep_(i, a_, b_, a, b, ...) for (int i = (a), i##_len = (b); i < i##_len; ++i)
#define rep(i, ...) rep_(i, __VA_ARGS__, __VA_ARGS__, 0, __VA_ARGS__)
#define reprev_(i, a_, b_, a, b, ...) for (int i = (b-1), i##_min = (a); i >= i##_min; --i)
#define reprev(i, ...) reprev_(i, __VA_ARGS__, __VA_ARGS__, 0, __VA_ARGS__)
#define all(x) (x).begin(), (x).end()
template <class T> bool chmax(T &a, const T &b) { if (a < b) { a = b; return 1; } return 0; }
template <class T> bool chmin(T &a, const T &b) { if (b < a) { a = b; return 1; } return 0; }
template <class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair <int,int> P;
typedef long double ld;

int main (void)
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n; cin >> n;
    vector<vector<int> > graph(n);
    vector<int> hen(n);
    rep (i, n - 1) {
        int a, b; cin >> a >> b; a--; b--;
        graph[a].push_back(b);
        graph[b].push_back(a);
        hen[a]++; hen[b]++;
    }
    vector<int> dist_tmp(n);
    vector<bool> used_tmp(n);
    used_tmp[0] = true;
    priority_queue<P> q; q.emplace(0, 0);
    while (!q.empty()) {
        P p = q.top(); q.pop();
        dist_tmp[p.second] = p.first;
        for (int i : graph[p.second]) {
            if (!used_tmp[i]) {
                used_tmp[i] = true;
                q.emplace(p.first + 1, i);
            }
        }
    }
    rep (i, n) eprintf("%d ", dist_tmp[i]); eprintf("\n");
    int u = 0, u_len = 0;
    rep (i, n) if (chmax(u_len, dist_tmp[i])) u = i;
    vector<int> dist_u(n);
    vector<bool> used_u(n);
    used_u[u] = true;
    q.emplace(0, u);
    while (!q.empty()) {
        P p = q.top(); q.pop();
        dist_u[p.second] = p.first;
        for (int i : graph[p.second]) {
            if (!used_u[i]) {
                used_u[i] = true;
                q.emplace(p.first + 1, i);
            }
        }
    }
    rep (i, n) eprintf("%d ", dist_u[i]); eprintf("\n");
    int v = u, longest = 0;
    rep (i, n) if (chmax(longest, dist_u[i])) v = i;
    eprintf("%d %d %d\n", u, v, longest);
    vector<int> dist_v(n);
    vector<bool> used_v(n);
    used_v[v] = true;
    q.emplace(0, v);
    while (!q.empty()) {
        P p = q.top(); q.pop();
        dist_v[p.second] = p.first;
        for (int i : graph[p.second]) {
            if (!used_v[i]) {
                used_v[i] = true;
                q.emplace(p.first + 1, i);
            }
        }
    }
    rep (i, n) eprintf("%d ", dist_v[i]); eprintf("\n");

    int m = 0;
    rep (i, n) {
        if (hen[i] != 1 || i == u || i == v) continue;
        chmax(m, max(dist_u[i], dist_v[i]));
    }
    bool flg = true;
    rep (i, n) {
        if ((m == max(dist_u[i], dist_v[i]) && (m != dist_u[i] || m != dist_v[i]))) {
            if (hen[i] != 1 || i == u || i == v) continue;
            flg = false;
        }
            // eprintf("%d %d")
    }

    rep (k, 1, n + 1) {
        bool ok = true;
        if (k <= 2 || k > longest) {
            cout << 1;
            continue;
        }
        if (m < k || (m == k && flg)) cout << 1;
        else cout << 0;
    }
    cout << "\n";
    return 0;
}
