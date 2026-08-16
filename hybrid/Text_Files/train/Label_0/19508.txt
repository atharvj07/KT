#include <bits/stdc++.h>
using namespace std;
int main() {
  int a, b, c, d, i, j, k, m, n, v;
  cin >> n;
  int A[n];
  cin >> A[0];
  if (A[0] > 15) {
    cout << 15;
    return (0);
  }
  for (j = 1; j < n; j++) {
    cin >> A[j];
  }
  for (i = 1; i < n; i++) {
    if ((A[i] - A[i - 1]) > 15) {
      cout << A[i - 1] + 15;
      return (0);
    }
  }
  if (90 - A[n - 1] > 15)
    cout << A[n - 1] + 15;
  else
    cout << 90;
  return (0);
}
