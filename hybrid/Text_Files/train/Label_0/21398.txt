#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int ind = 0, n, k, x[100000];
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
      cin >> x[i];
      if (x[i] == k) {
        x[i] = 1;
        ind = 1;
      } else if (x[i] > k)
        x[i] = 2;
      else
        x[i] = 0;
    }
    if (!ind) {
      cout << "no\n";
      continue;
    }
    if (n == 1) {
      cout << "yes\n";
      continue;
    }
    bool res = 0;
    for (int i = 0; i < n; i++)
      for (int j = i + 1; j < i + 3 && j < n; j++)
        if (x[i] > 0 && x[j] > 0) res = 1;
    if (res)
      cout << "yes";
    else
      cout << "no";
    cout << '\n';
  }
  return 0;
}
