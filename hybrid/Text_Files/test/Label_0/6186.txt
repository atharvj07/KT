#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, d;
  cin >> n >> d;
  int *a = new int[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  sort(a, a + n);
  int ans = 0;
  for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
      if (a[j] - a[i] <= d && j - i + 1 > ans) {
        ans = j - i + 1;
      }
    }
  }
  cout << (n - ans) << endl;
}
