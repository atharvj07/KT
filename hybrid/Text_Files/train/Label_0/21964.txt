#include <bits/stdc++.h>
using namespace std;
int a[1001];
int main() {
  int n;
  cin >> n;
  int b[n];
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    a[x]++;
  }
  int cnt = 0;
  for (int i = 1; i <= 100; i++) {
    if (a[i] > 1) {
      if (a[i] % 2 != 0) {
        cnt += a[i] - 1;
      } else {
        cnt += a[i];
      }
    }
  }
  cout << cnt / 4 << '\n';
}
