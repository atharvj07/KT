#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int a[n];
  for (int x = 0; x < n; x++) {
    cin >> a[x];
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      for (int k = 0; k < n; ++k) {
        if (a[i] == a[j] + a[k] && (i != j && j != k && i != k)) {
          cout << i + 1 << " " << j + 1 << " " << k + 1 << endl;
          return 0;
        }
      }
    }
  }
  cout << "-1" << endl;
  return 0;
}
