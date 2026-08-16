#include <bits/stdc++.h>
using namespace std;
int a[2001] = {0}, b[2001];
int main() {
  int n;
  cin >> n;
  for (int i = 1, j; i <= n; i++) {
    cin >> j;
    a[j]++;
    b[i] = j;
  }
  int ranking = 1, temp;
  for (int i = 2000; i >= 1; i--) {
    if (a[i] != 0) {
      temp = a[i];
      a[i] = ranking;
      ranking += temp;
    }
  }
  for (int i = 1; i <= n; i++) {
    if (i == n) {
      cout << a[b[i]];
      break;
    }
    cout << a[b[i]] << " ";
  }
  return 0;
}
