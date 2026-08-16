#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, a[10000];
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int sum = 0;
  sort(a, a + n);
  for (int i = 0; i < n - 1; i++) {
    if (a[i] == a[i + 1] && a[i] != 0) {
      if (a[i + 1] == a[i + 2]) {
        cout << -1;
        return 0;
      }
      sum++;
      i++;
    }
  }
  cout << sum;
}
