#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, p, q;
  string s;
  cin >> n >> p >> q >> s;
  for (int i = 0; i <= n; i++)
    for (int j = 0; j <= n; j++)
      if (n == i * p + j * q) {
        int k = 0;
        cout << i + j << endl;
        while (i--) {
          cout << s.substr(k, p) << endl;
          k += p;
        }
        while (j--) {
          cout << s.substr(k, q) << endl;
          k += q;
        }
        return 0;
      }
  cout << -1 << endl;
  return 0;
}
