#include <bits/stdc++.h>
using namespace std;
long long a[100000], b[100000];
int main() {
  long long p, k;
  int i, tot = 0;
  cin >> p >> k;
  a[0] = -(p / k);
  for (i = 1;; i++) {
    if (a[i - 1] % k == 0)
      a[i] = -a[i - 1] / k;
    else {
      if (a[i - 1] < 0)
        a[i] = (-a[i - 1] + k - 1) / k;
      else
        a[i] = -(a[i - 1] / k);
    }
    if (a[i] == 0) break;
    tot = i;
    if (i > 90000) {
      cout << -1 << endl;
      return 0;
    }
  }
  b[0] = a[0] * k + p;
  for (i = 1; i <= tot; i++) b[i] = a[i] * k + a[i - 1];
  b[tot + 1] = a[tot];
  while (tot + 1 >= 0 && b[tot + 1] == 0) tot--;
  cout << tot + 2 << endl;
  for (i = 0; i <= tot + 1; i++) cout << b[i] << ' ';
  return 0;
}
