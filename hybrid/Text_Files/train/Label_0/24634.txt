#include <bits/stdc++.h>
using namespace std;
long long n, i, j, a[10001], b[10001], v, h[10001], k;
int main() {
  cin >> n;
  for (i = 1; i <= n; i++) cin >> a[i];
  for (i = 1; i <= n; i++) {
    for (j = 1; j <= n; j++) b[j] = 0;
    k = 0;
    for (j = i; j <= n; j++) {
      v = a[j];
      b[v]++;
      if (b[v] > b[k] or (b[v] == b[k] and v < k)) k = v;
      h[k]++;
    }
  }
  for (i = 1; i <= n; i++) cout << h[i] << " ";
  return 0;
}
