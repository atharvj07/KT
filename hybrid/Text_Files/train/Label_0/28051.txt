#include <bits/stdc++.h>
using namespace std;
int MOD = 1e9 + 7;
int PRIME = 102838201;
int INF = 1e9;
vector<string> &split(const std::string &s, char delim, vector<string> &e) {
  stringstream ss(s);
  string item;
  while (getline(ss, item, delim)) e.push_back(item);
  return e;
}
int Pow(int a, int b, int Mo) {
  int ans = 1;
  for (; b; b >>= 1, a = a * a % Mo)
    if (b & 1) ans = ans * a % Mo;
  return ans;
}
int nCr(int n, int r) {
  static int MAXF = 1e6;
  static std::vector<int> fact(MAXF, 1);
  for (int i = 1; i < MAXF; ++i) fact[i] = (fact[i - 1] * i) % MOD;
  MAXF = 0;
  return (fact[n] * Pow((fact[r] * fact[n - r]) % MOD, MOD - 2, MOD)) % MOD;
}
vector<int> Zfunc(string &s) {
  int n = s.length();
  vector<int> z(n, 0);
  for (int i = 1, l = 0, r = 0; i < n; i++) {
    if (i <= r) z[i] = min(z[i - l], r - i + 1);
    while (i + z[i] < n && s[i + z[i]] == s[z[i]]) z[i]++;
    if (r < i + z[i] - 1) l = i, r = i + z[i] - 1;
  }
  z[0] = s.length();
  return z;
}
int solve() { return 0; }
int di(int x) {
  int c = 0;
  while (x > 0) {
    x /= 10;
    c++;
  }
  if (!c) c++;
  return c;
}
std::vector<int> DP;
std::vector<std::vector<int> > lon;
int n;
int moves = 0;
int main(int argc, char const *argv[]) {
  std::ios::sync_with_stdio(false);
  cin.tie(0);
  string s;
  cin >> s;
  n = s.length();
  DP.resize(n + 1, INF);
  lon.resize(n + 1);
  DP[n] = 0;
  for (int i = 0; i < n; ++i) {
    string s2 = s.substr(i, n - i);
    lon[i] = Zfunc(s2);
  }
  for (int index = n - 1; index >= 0; --index) {
    int ans = 1 + n - index;
    for (int j = index; j < n; ++j) {
      ans = min(1 + j - index + 1 + DP[(j + 1)], ans);
    }
    for (int p = 1; p + index < n; ++p) {
      int common = lon[index][p] + p;
      int repeatedlen = (common) / p;
      for (int k = 1; k <= repeatedlen; ++k) {
        ans = min(di(k) + p + DP[(k * p + index)], ans);
      }
    }
    DP[index] = ans;
  }
  cout << DP[0];
  return 0;
}
