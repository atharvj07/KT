#include <bits/stdc++.h>
#define ll long long
#define ull int64_t
#define vll vector<ll>
using namespace std;
ull mod = 1e9 + 7;
ull g(int c){
  return (((ull)(1)) << c);
}
int f(ull x, int c) {
  if (x & g(c))
    return 1;
  return 0;
}
inline void sol() {
  int n;
  cin >> n;
  vector<ull> x(n);
  for (auto &i : x)
    cin >> i;
  vector<int> fre(60);
  for (int j = 0; j < 60; j++) {
    for (int i = 0; i < n; i++) {
      if (f(x[i], j))
        fre[j]++;
    }
  }
  ull ans = 0;
  for (int j = 0; j < n; j++) {
    ull p1 = 0, p2 = 0;
    for (ull c = 0; c < 60; c++) {
      p1 += (g(c) % mod) * f(x[j], c) * fre[c];
      p1 %= mod;
      p2 += (g(c) % mod) * ((n - (1 - f(x[j], c)) * (n - fre[c])) % mod);
      p2 %= mod;
    }
    ans += ((p1 % mod) * (p2 % mod)) % mod;
    ans %= mod;
  }
  cout << ans << endl;
}
int main() {
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  while (t--)
    sol();

  return 0;
}