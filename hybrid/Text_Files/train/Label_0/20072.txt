#include <bits/stdc++.h>
using namespace std;
int t, n, k;
int main() {
  cin >> t;
  while (t--) {
    cin >> n;
    int a[101] = {0};
    for (int i = 1; i <= n; i++) {
      cin >> k;
      a[k]++;
    }
    int i = 0, j = 0;
    while (a[i] >= 2) {
      i++;
    }
    while (a[j] >= 1) {
      j++;
    }
    cout << i + j << endl;
  }
  return 0;
}
