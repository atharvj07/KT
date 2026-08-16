#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, l = 0, r = 0;
  cin >> n;
  int* A = new int[n + 2];
  for (int i = 1; i <= n; i++) cin >> A[i];
  int i = 1;
  while (i <= n && A[i] == i) {
    i++;
  }
  if (i < n) {
    l = i;
    r = A[i];
    bool f = false;
    for (; i <= r; i++)
      if (A[i] != r + l - i) f = true;
    for (; i <= n; i++)
      if (A[i] != i) f = true;
    if (f) {
      cout << "0 0";
      return 0;
    }
  }
  cout << l << " " << r;
  return 0;
}
