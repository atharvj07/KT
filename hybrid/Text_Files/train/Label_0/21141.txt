#include <bits/stdc++.h>
using namespace std;
const int N = 100100;
int main() {
  int a[N];
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  sort(a, a + n);
  for (int i = 0; i < n - 2;) {
    if (a[i] + a[i + 1] <= a[i + 2]) {
      i += 1;
    } else {
      cout << "YES" << endl;
      return (0);
    }
  }
  cout << "NO" << endl;
  return 0;
}
