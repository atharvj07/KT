#include <bits/stdc++.h>
using namespace std;
void aps554(long long int n = 10) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cout << setprecision(n) << fixed;
}
long long int M = 1e9 + 7;
long long int M1 = 998244353;
int32_t main() {
  aps554();
  map<long long int, long long int> haaas;
  for (long long int i = 0; i < 35; i++) {
    for (long long int j = 0; j < 16; j++) {
      haaas[i * 3 + j * 7]++;
    }
  }
  long long int t;
  cin >> t;
  while (t--) {
    long long int n;
    cin >> n;
    if (haaas[n])
      cout << "YES\n";
    else
      cout << "NO\n";
  }
}
