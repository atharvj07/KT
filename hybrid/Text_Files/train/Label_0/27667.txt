#include <bits/stdc++.h>
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
using namespace std;
int ni() {
  int val;
  scanf("%i", &val);
  return val;
}
pair<int, int> npi() {
  pair<int, int> val;
  scanf("%i %i", &val.first, &val.second);
  return val;
}
int64_t nll() {
  int64_t val;
  scanf("%I64d", &val);
  return val;
}
vector<int> nvi(int n, int corr = 0) {
  vector<int> a(n);
  for (int i = 0; i < n; ++i) a[i] = ni() + corr;
  return move(a);
}
char nc() {
  char val;
  do {
    val = getchar();
  } while (val == ' ' || val == '\r' || val == '\n');
  return val;
}
char ncs() {
  char val;
  do {
    val = getchar();
  } while (false);
  return val;
}
string ns() {
  static char buff[1024 * 4000];
  scanf("%s", buff);
  return string{buff};
}
int64_t gcd(int64_t a, int64_t b) {
  while (b) {
    auto tmp = a % b;
    a = b;
    b = tmp;
  }
  return a;
}
int64_t tr2(int xv1, int yv1, int xv2, int yv2, int x3, int y3) {
  return 1LL * (xv2 - xv1) * (y3 - yv1) - 1LL * (yv2 - yv1) * (x3 - xv1);
}
const long double eps = 1e-12;
const long double pi = acos(-1.0);
bool eq(long double a, long double b) { return abs(a - b) <= eps; }
int8_t bits_cnt[256];
const string input_dir = "inputs\\";
string input_file = input_dir + "input.txt";
string output_file = input_dir + "output.txt";
void init_streams() {}
void init_data() {
  for (int i = 1; i <= 255; ++i)
    for (int j = 0; j < 8; ++j)
      if ((1 << j) & i) ++bits_cnt[i];
}
int bit_count(int v) {
  return bits_cnt[v & 0xFF] + bits_cnt[(v >> 8) & 0xFF] +
         bits_cnt[(v >> 16) & 0xFF] + bits_cnt[(v >> 24) & 0xFF];
}
const int maxn = 100000 + 1;
int n, m;
int E[maxn];
std::vector<int> adj[maxn];
bool vis[maxn];
int mx[maxn];
int dfs(int u) {
  if (vis[u]) return mx[u];
  vis[u] = true;
  mx[u] = E[u];
  for (auto to : adj[u]) mx[u] = max(mx[u], (E[u] && !E[to]) + dfs(to));
  return mx[u];
}
int main() {
  init_streams();
  init_data();
  auto n = ni(), m = ni();
  for (int i = 0; i < n; ++i) E[i] = ni();
  for (int i = 0; i < m; ++i) {
    auto u = ni();
    auto v = ni();
    adj[u].emplace_back(v);
  }
  int ans = 0;
  for (int i = 0; i < n; ++i) ans = max(ans, dfs(i));
  cout << ans << endl;
  return 0;
}
