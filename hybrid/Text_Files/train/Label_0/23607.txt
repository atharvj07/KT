#include <bits/stdc++.h>
using namespace std;
long long v[100002], a[100002];
void interclasare(int st, int dr, int m) {
  int i, j, k = st - 1;
  i = st;
  j = m + 1;
  while (i <= m && j <= dr)
    if (v[i] <= v[j]) {
      k++;
      a[k] = v[i];
      i++;
    } else {
      k++;
      a[k] = v[j];
      j++;
    }
  if (i <= m)
    for (j = i; j <= m; j++) {
      k++;
      a[k] = v[j];
    }
  else
    for (i = j; i <= dr; i++) {
      k++;
      a[k] = v[i];
    }
  for (i = st; i <= dr; i++) v[i] = a[i];
}
void mergesort(int st, int dr) {
  if (st < dr) {
    int m = (dr + st) / 2;
    mergesort(st, m);
    mergesort(m + 1, dr);
    interclasare(st, dr, m);
  }
}
int main() {
  int n, i, m = 0, nr, x;
  cin >> n;
  for (i = 1; i <= n; i++) {
    cin >> x;
    v[i] = v[i - 1] + x;
  }
  mergesort(1, n);
  for (i = 1; i <= n; i++) {
    nr = 1;
    while (v[i] == v[i + 1] && i < n) {
      nr++;
      i++;
    }
    if (nr > m) m = nr;
  }
  cout << n - m;
}
