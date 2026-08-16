#include <bits/stdc++.h>
using namespace std;
const double pi = acos(-1.0);
const double eps = 1e-11;
const int inf = 0x7FFFFFFF;
template <class T>
inline void checkmin(T &a, T b) {
  if (b < a) a = b;
}
template <class T>
inline void checkmax(T &a, T b) {
  if (b > a) a = b;
}
template <class T>
inline T sqr(T x) {
  return x * x;
}
template <class T>
void show(T a, int n) {
  for (int i = 0; i < n; ++i) cout << a[i] << ' ';
  cout << endl;
}
template <class T>
void show(T a, int r, int l) {
  for (int i = 0; i < r; ++i) show(a[i], l);
  cout << endl;
}
long long has[100005];
struct E {
  int v;
  int nxt;
} e[200005];
int ec, hd[100050];
bool vis[100050];
long long dfs(int u, long long &aa) {
  vis[u] = true;
  has[u]--;
  long long rem = 0, ret = 1;
  vector<long long> got;
  for (int ev = hd[u]; ev; ev = e[ev].nxt) {
    int v = e[ev].v;
    if (!vis[v]) got.push_back(dfs(v, rem));
  }
  if (got.size()) {
    sort(got.begin(), got.end());
    for (int k = got.size() - 1; k >= 0; k--)
      if (has[u] > 0) {
        ret += got[k] + 1;
        has[u]--;
      } else
        break;
  }
  if (has[u] >= rem) {
    has[u] -= rem;
    ret += rem * 2;
  } else {
    ret += has[u] * 2;
    has[u] = 0;
  }
  aa += has[u];
  return ret;
}
int main() {
  int n;
  while (cin >> n) {
    ec = 1;
    for (int i = 1; i <= n; i++) cin >> has[i];
    for (int j = 1; j < n; j++) {
      int u, v;
      cin >> u >> v;
      e[ec].v = v;
      e[ec].nxt = hd[u];
      hd[u] = ec++;
      swap(u, v);
      e[ec].v = v;
      e[ec].nxt = hd[u];
      hd[u] = ec++;
      swap(u, v);
    }
    int start;
    long long ans = 0;
    cin >> start;
    has[start]++;
    cout << dfs(start, ans) - 1 << endl;
  }
  return 0;
}
