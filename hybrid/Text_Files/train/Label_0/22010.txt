#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k, t;
  cin >> n >> k;
  int *a = new int[2 * n + 1];
  for (int i = 0; i < (int)2 * n + 1; i++) cin >> a[i];
  for (int i = 0; i < (int)2 * n + 1; i++) {
    if (!((i + 1) % 2)) {
      if (k && a[i] - a[i - 1] >= 2 && a[i] - a[i + 1] >= 2) {
        k--;
        a[i]--;
      }
    }
    cout << a[i] << " ";
  }
  cout << endl;
  return 0;
}
