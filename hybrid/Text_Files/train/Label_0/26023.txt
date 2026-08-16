#include <bits/stdc++.h>
using namespace std;
int main() {
  int x;
  cin >> x;
  bool rjesenja[x];
  for (int k = 0; k < x; k++) {
    int n, sum = 0;
    cin >> n;
    int niz[n];
    for (int i = 0; i < n; i++) {
      cin >> niz[i];
      if (niz[i] <= 2048) sum += niz[i];
    }
    if (sum >= 2048)
      rjesenja[k] = true;
    else
      rjesenja[k] = false;
  }
  for (int i = 0; i < x; i++) {
    if (rjesenja[i] == true)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}
