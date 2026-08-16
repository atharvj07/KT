#include <bits/stdc++.h>
using namespace std;
const long double pi = acos(-1);
long long n, m, k;
int main() {
  cin.tie(0);
  cin.sync_with_stdio(0);
  int t = 1;
  while (t--) {
    cin >> n;
    int o = 0, tw = 0;
    for (int i = 0; i < n; i++) cin >> m, o += m == 1, tw += m == 2;
    if (tw) cout << "2 ", tw--;
    if (o) cout << "1 ", o--;
    for (int i = 0; i < tw; i++) cout << "2 ";
    for (int i = 0; i < o; i++) cout << "1 ";
  }
  return 0;
}
