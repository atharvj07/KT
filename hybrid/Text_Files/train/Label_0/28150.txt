#include <bits/stdc++.h>
using namespace std;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
template <class T>
void IN(T& x) {
  cin >> x;
}
template <class H, class... T>
void IN(H& h, T&... t) {
  IN(h);
  IN(t...);
}
template <class T1, class T2>
void OUT(const pair<T1, T2>& x);
template <class T>
void OUT(const T& x) {
  cout << x;
}
template <class H, class... T>
void OUT(const H& h, const T&... t) {
  OUT(h);
  OUT(t...);
}
template <class T1, class T2>
void OUT(const pair<T1, T2>& x) {
  OUT(x.first, ' ', x.second);
}
template <class... T>
void OUTL(const T&... t) {
  OUT(t..., "\n");
}
template <class H>
void OUTLS(const H& h) {
  OUTL(h);
}
template <class H, class... T>
void OUTLS(const H& h, const T&... t) {
  OUT(h, ' ');
  OUTLS(t...);
}
void program();
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  program();
}
const int MX = 5e5;
int n, m, k;
vector<pair<int, int> > adj[MX];
long long h[MX];
long long f[10][10];
long long tot;
int getAns(int i, long long bm) {
  if (i == k) {
    if (bm == tot) return 1;
    return 0;
  }
  int ans = 0;
  for (int j = int(0); j < int(i + 1); j++) {
    bm ^= f[i][j];
    ans += getAns(i + 1, bm);
    bm ^= f[i][j];
  }
  return ans;
}
void program() {
  IN(n, m, k);
  for (int i = int(0); i < int(m); i++) {
    int u, v, w;
    IN(u, v, w);
    u--;
    v--;
    adj[u].push_back({w, v});
  }
  for (int i = int(0); i < int(n); i++) sort(adj[i].begin(), adj[i].end());
  for (int i = int(0); i < int(n); i++) h[i] = rng();
  for (int i = int(0); i < int(10); i++)
    for (int j = int(0); j < int(10); j++) f[i][j] = 0;
  for (int u = int(0); u < int(n); u++) {
    for (int i = int(0); i < int(adj[u].size()); i++) {
      f[adj[u].size() - 1][i] ^= h[adj[u][i].second];
    }
  }
  tot = 0;
  for (int i = int(0); i < int(n); i++) tot ^= h[i];
  OUTL(getAns(0, 0));
}
