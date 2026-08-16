#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    long long d, m;
    cin >> d >> m;
    long long ans = 1, i = 0;
    while ((1 << i + 1) <= d) ans = (ans * (1 + (1 << i++))) % m;
    ans = (ans * (1 + (d - (1 << i) + 1))) % m;
    cout << (ans + m - 1) % m << '\n';
  }
}
