#include <bits/stdc++.h>
using namespace std;
const int INF = 1000000000;
const double PI = 3.1415926535897932384626433832795028841971;
long long sum[10000010], s[10000010];
int main() {
  long long n, m, a, b, l, t, r, j, i;
  cin >> a >> b >> n;
  for (i = 1; i <= 10000000; i++) {
    s[i] = a + (i - 1) * b;
    sum[i] = sum[i - 1] + s[i];
  }
  for (i = 0; i < n; i++) {
    cin >> l >> t >> m;
    int left = l, right = 10000000, middle;
    while (left + 1 != right) {
      middle = (left + right) / 2;
      if (middle < l) {
        left = middle;
        break;
      }
      if (s[middle] <= t && sum[middle] - sum[l - 1] <= t * m)
        left = middle;
      else
        right = middle;
    }
    if (!(s[left] <= t && sum[left] - sum[l - 1] <= t * m)) left = -1;
    if (left < l) left = -1;
    cout << left << endl;
  }
}
