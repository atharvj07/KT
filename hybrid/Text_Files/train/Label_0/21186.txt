#include <bits/stdc++.h>
using namespace std;
const int N = 2e5 + 5;
vector<string> ans;
int ptr[32 * N][2];
int mask[32 * N];
int n, node;
bool en[32 * N];
bool isdigit(char c) { return '0' <= c && c <= '9'; }
int getint(string &s) {
  int res = 0;
  while (s.size() && isdigit(s.back())) {
    res = 10 * res + (s.back() - '0');
    s.pop_back();
  }
  return res;
}
int getbit(long long x, int i) { return (x >> i) & 1; }
void add(long long val, int lim, int t) {
  int cur = 0;
  mask[cur] |= t;
  for (int i = 31; i >= lim; i--) {
    int &p = ptr[cur][getbit(val, i)];
    if (!p) p = ++node;
    if (en[cur]) t |= mask[cur];
    cur = p;
    mask[cur] |= t;
  }
  en[cur] = true;
  if (mask[cur] == 3) {
    cout << -1;
    exit(0);
  }
}
string strint(int x) {
  string res = "";
  if (x == 0) return "0";
  while (x > 0) {
    res += (x % 10) + '0';
    x /= 10;
  }
  reverse(res.begin(), res.end());
  return res;
}
string subnet(long long val, int i) {
  string res = "";
  for (int j = 1; j <= 4; j++) {
    string tmp = strint(val % (1 << 8));
    reverse(tmp.begin(), tmp.end());
    res += tmp;
    val >>= 8;
    if (j < 4) res += '.';
  }
  reverse(res.begin(), res.end());
  res += '/';
  res += strint(i);
  return res;
}
void dfs(int u, int i, long long val) {
  if (!getbit(mask[u], 1)) {
    ans.push_back(subnet(val, i));
    return;
  }
  for (int j = 0; j <= 1; j++) {
    int v = ptr[u][j];
    if (v == 0) continue;
    dfs(v, i + 1, val + ((long long)j << (32 - i - 1)));
  }
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 1; i <= n; i++) {
    char c;
    cin >> c;
    int t = (c == '+') + 1;
    string s;
    cin >> s;
    reverse(s.begin(), s.end());
    long long val = 0;
    for (int i = 1; i <= 4; i++) {
      val = (val << 8) + getint(s);
      if (i < 4) s.pop_back();
    }
    int x = 0;
    if (s.size()) {
      s.pop_back();
      x = 32 - getint(s);
    }
    add(val, x, t);
  }
  dfs(0, 0, 0);
  cout << ans.size() << "\n";
  for (string s : ans) cout << s << "\n";
  return 0;
}
