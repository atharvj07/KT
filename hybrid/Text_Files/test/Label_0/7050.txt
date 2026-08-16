#include <bits/stdc++.h>
using namespace std;
template <typename T>
using V = vector<T>;
template <typename T>
using VV = vector<V<T>>;
template <typename T>
using Mi = map<long long, T>;
template <typename T>
using MMi = map<long long, Mi<T>>;
vector<long long> tree;
void build(vector<long long> &arr, long long ind, long long l, long long r) {
  if (l == r) {
    tree[ind] = arr[l];
    return;
  }
  long long mid = (l + r) / 2;
  build(arr, ind * 2, l, mid);
  build(arr, ind * 2 + 1, mid + 1, r);
  tree[ind] = max(tree[ind * 2], tree[ind * 2 + 1]);
}
long long getMax(long long ind, long long tl, long long tr, long long l,
                 long long r) {
  if (l > r) return 0;
  if (l == tl && r == tr) return tree[ind];
  long long tm = (tl + tr) / 2;
  long long a = getMax(ind * 2, tl, tm, l, min(r, tm));
  long long b = getMax(ind * 2 + 1, tm + 1, tr, max(l, tm + 1), r);
  return max(a, b);
}
vector<bool> prim;
void er() {
  long long n = 1e6;
  prim = vector<bool>(n + 1, true);
  prim[0] = prim[1] = false;
  for (long long i = 2; i <= n; i++) {
    if (prim[i]) {
      for (long long j = i * i; j <= n; j += i) {
        prim[j] = false;
      }
    }
  }
}
vector<long long> topSort(long long v, V<set<long long>> &g) {
  vector<long long> ans;
  vector<bool> viz(g.size(), false);
  return ans;
}
long long rast(pair<long long, long long> &a, pair<long long, long long> &b) {
  return abs(a.first - b.first) + abs(a.second - b.second);
}
vector<long long> z_function(string &s) {
  long long n = s.length();
  vector<long long> z(n, 0);
  long long l = 0, r = 0;
  for (long long i = 1; i < n; i++) {
    if (i <= r) {
      z[i] = min(r - i + 1, z[i - l]);
    }
    while (i + z[i] < n && s[z[i]] == s[z[i] + i]) {
      z[i]++;
    }
    if (i + z[i] - 1 > r) {
      l = i;
      r = i + z[i] - 1;
    }
  }
  return z;
}
bool comp(const string &a, const string &b) { return a.size() < b.size(); }
void printTest() {
  freopen("output.txt", "w", stdout);
  cout << "1000 500 1000" << '\n';
  for (int i = 0; i < 500; i++) {
    cout << i * 2 << " " << i * 2 + 1 << '\n';
  }
  for (int i = 0; i < 1000; i++) {
    cout << i << " " << 1000 - i << '\n';
  }
}
void dfs(long long v, long long mid, VV<pair<long long, long long>> &g,
         vector<bool> &viz, long long &ans, vector<bool> &need) {
  viz[v] = true;
  if (need[v]) {
    ans++;
  }
  for (pair<long long, long long> &p : g[v]) {
    long long &w = p.first;
    long long &u = p.second;
    if (w >= mid) {
      return;
    }
    if (!viz[u]) {
      dfs(u, mid, g, viz, ans, need);
    }
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  string s;
  cin >> s;
  for (long long i = 1; i < s.size(); i++) {
    if (s[i] == s[i - 1]) {
      s[i] = 'a';
      while (s[i] == s[i - 1] || (i + 1 < s.size() && s[i] == s[i + 1])) {
        s[i]++;
      }
    }
  }
  cout << s;
  return 0;
}
