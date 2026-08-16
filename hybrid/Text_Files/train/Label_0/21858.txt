#include <bits/stdc++.h>
using namespace std;
template <class T>
T gcd(T a, T b) {
  return b == 0 ? a : gcd(b, a % b);
}
template <typename T>
T lcm(T a, T b) {
  return a / gcd(a, b) * b;
}
template <class T>
T my_pow(T n, T p) {
  if (p == 0) return 1;
  T x = my_pow(n, p / 2);
  x = (x * x);
  if (p & 1) x = (x * n);
  return x;
}
template <class T>
T big_mod(T n, T p, T m) {
  if (p == 0) return (T)1;
  T x = big_mod(n, p / 2, m);
  x = (x * x) % m;
  if (p & 1) x = (x * n) % m;
  return x;
}
template <class T>
T extract(string s, T ret) {
  stringstream ss(s);
  ss >> ret;
  return ret;
}
string itos(long long n) {
  string s;
  while (n) {
    s += (n % 10 + 48);
    n /= 10;
  }
  reverse(s.begin(), s.end());
  return s;
}
long long stoi(string s) {
  long long n = 0;
  for (__typeof(s.size()) i = 0; i < (s.size()); i++) n = n * 10 + (s[i] - 48);
  return n;
}
struct info {
  long long x, y;
  string yy;
} arr[100005];
bool com(info a, info b) { return (a.x > b.x) or (a.x == b.x and a.yy < b.yy); }
long long ar[100001], vis[100001];
long long a = 0, b = 0, c = 0, r = 0, rr = 0, res = 0, n, m, t = 0, ks = 0, w;
string s;
vector<long long> v[100005];
long long idx = 0, mx = 0;
long long dfs(long long node, long long dis) {
  vis[node] = 1;
  if (dis > mx) {
    mx = dis;
    idx = node;
  }
  for (int i = 0; i < (v[node].size()); i++) {
    if (!vis[v[node][i]]) {
      dfs(v[node][i], dis + 1);
    }
  }
  return 0;
}
int main() {
  cin >> m;
  m--;
  for (__typeof(m) i = 0; i < (m); i++) {
    cin >> a >> b;
    v[a].push_back(b);
    v[b].push_back(a);
  }
  mx = 0;
  for (__typeof(100001) i = 1; i <= (100001); i++) {
    long long aa = v[i].size();
    aa--;
    mx += ((aa) * (aa + 1)) / 2;
  }
  printf("%lld\n", mx);
  return 0;
}
