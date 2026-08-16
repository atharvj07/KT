#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  long long t;
  cin >> t;
  while (t--) {
    long long d, m;
    cin >> d >> m;
    long long res = 1;
    long long msb = 1;
    while (msb <= d) {
      res *= min(msb, d - msb + 1) + 1;
      res %= m;
      msb <<= 1;
    }
    cout << (res - 1 + m) % m << endl;
  }
}
