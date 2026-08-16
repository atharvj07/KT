#include <bits/stdc++.h>
using namespace std;
template <class T>
inline T BMOD(T p, T e, T m) {
  T ret = 1;
  while (e) {
    if (e & 1) ret = (ret * p) % m;
    p = (p * p) % m;
    e >>= 1;
  }
  return (T)ret;
}
template <class T>
inline T MODINV(T a, T m) {
  return BMOD(a, m - 2, m);
}
template <class T>
inline T isPrime(T a) {
  for (T i = 2; i <= sqrt(double(a)); i++) {
    if (a % i == 0) {
      return 0;
    }
  }
  return 1;
}
template <class T>
inline T lcm(T a, T b) {
  return (a / __gcd(a, b)) * b;
}
template <class T>
inline T power(T a, T b) {
  return (b == 0) ? 1 : a * power(a, b - 1);
}
int vs[300010], lv[300010], pr[300010], Ans[300010];
vector<int> g[300010];
void dfs(int s, int p = 0) {
  int cnt = 0;
  for (int i = 0; i < (int)g[s].size(); i++) {
    int t = g[s][i];
    if (t != p) {
      dfs(t, s);
      cnt++;
    }
  }
  lv[s] = cnt;
  return;
}
void dfs2(int s, int p = 0) {
  for (int i = 0; i < (int)g[s].size(); i++) {
    int t = g[s][i];
    if (t != p) {
      dfs2(t, s);
      lv[s] += lv[t];
    }
  }
  return;
}
priority_queue<pair<int, int>, vector<pair<int, int> >,
               greater<pair<int, int> > >
    pq[300010];
int mx[300030];
void dfs3(int s, int p = 0) {
  lv[s] = 1;
  int mid = s, mxz = 0;
  for (int i = 0; i < (int)g[s].size(); i++) {
    int t = g[s][i];
    if (t != p) {
      dfs3(t, s);
      lv[s] += lv[t];
      mx[s] = max(mx[s], lv[t]);
      if (pq[t].size() > mxz) {
        mxz = pq[t].size();
        mid = t;
      }
    }
  }
  swap(pq[s], pq[mid]);
  pq[s].push({lv[s], s});
  for (int i = 0; i < (int)g[s].size(); i++) {
    int t = g[s][i];
    if (t == p || mid == t) continue;
    while (!pq[t].empty()) {
      pq[s].push(pq[t].top());
      pq[t].pop();
    }
  }
  while (!pq[s].empty()) {
    int t = pq[s].top().first;
    if (t * 2 < lv[s])
      pq[s].pop();
    else
      break;
  }
  Ans[s] = pq[s].top().second;
  return;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n, m, a;
  cin >> n >> m;
  pr[1] = -1;
  for (int i = 2; i <= n; i++) {
    cin >> a;
    g[a].push_back(i);
  }
  dfs3(1);
  while (m--) {
    cin >> a;
    cout << Ans[a] << endl;
  }
  return 0;
}
