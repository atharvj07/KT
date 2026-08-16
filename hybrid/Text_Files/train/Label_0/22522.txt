#include <bits/stdc++.h>
using namespace std;
const int maxn = 3e5 + 5;
const int maxm = 305;
long long arr[maxn];
long long arr1[maxn];
const long long mod = 1e9 + 7;
long long n, m, k, q, D, H, a, b, c, h, d, x, y, z, t, p;
string s, s1, s2;
long long gcd(long long a, long long b) {
  long long t;
  while (b) {
    t = a;
    a = b;
    b = t % b;
  }
  return a;
}
long long par[maxn];
void init() {
  for (int i = 0; i < maxn; i++) par[i] = i;
}
void init(int n) {
  for (int i = 0; i < n + 10; i++) par[i] = i;
}
long long find(int i) {
  if (par[i] != i) {
    return par[i] = find(par[i]);
  } else
    return i;
}
void merge(int x, int y) { par[find(x)] = par[find(y)]; }
long long presum[100];
bool isVowel(char c) {
  if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
    return true;
  else
    return false;
};
vector<int> get_pi(const string s) {
  int n = s.length();
  vector<int> pi(n);
  int k = 0;
  for (int i = 1; i < n; i++) {
    while (k > 0 && s[i] != s[k]) k = pi[k - 1];
    if (s[i] == s[k]) k++;
    pi[i] = k;
  }
  return pi;
}
struct Line {
  Line(int _from, int _to, int _val) {
    from = _from;
    to = _to;
    val = _val;
  }
  int from;
  int to;
  int val;
};
set<int> edges[100010];
set<int> allnodes;
bool visited[100010];
void dfs(int cur) {
  queue<int> q;
  q.push(cur);
  allnodes.erase(cur);
  while (q.size() > 0) {
    int y = q.front();
    q.pop();
    if (visited[y]) continue;
    visited[y] = 1;
    for (auto it = allnodes.begin(); it != allnodes.end();) {
      int v = *it;
      ++it;
      if (edges[y].find(v) == edges[y].end()) {
        q.push(v);
        allnodes.erase(v);
      }
    }
  }
}
int main() {
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    cin >> a >> b;
    edges[a].insert(b);
    edges[b].insert(a);
  }
  for (int i = 1; i <= n; i++) {
    allnodes.insert(i);
  }
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    if (!visited[i]) {
      ans++;
      dfs(i);
    }
  }
  cout << ans - 1 << endl;
}
