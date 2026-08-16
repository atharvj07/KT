#include <bits/stdc++.h>
using namespace std;
const long long mod = (long long)1e9 + 7;
map<long long, long long> c;
int main() {
  long long m = 998244353;
  int n;
  cin >> n;
  int a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    c[a[i]] = i;
  }
  long long w = c[a[0]];
  long long res = 1;
  for (int i = 0; i < n; i++) {
    if (i > w) {
      res = (res * 2) % m;
    }
    w = max(w, c[a[i]]);
  }
  cout << res << endl;
}
