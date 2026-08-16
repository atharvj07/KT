#include <bits/stdc++.h>
using namespace std;
long long c[200000], a1[200000], a2[200000], a3[200000];
long long k = 0;
int main() {
  long long k1, k2, k3, t1, t2, t3, n;
  cin >> k1 >> k2 >> k3 >> t1 >> t2 >> t3 >> n;
  for (long long i = 0; i < n; i++) cin >> c[i];
  k = 0;
  for (long long i = 0; i < n; i++) {
    while ((k < i - k1 || a1[k] <= c[i]) && k < i) k++;
    if (i - k < k1)
      a1[i] = c[i] + t1;
    else
      a1[i] = max(a1[k], c[i]) + t1;
  }
  k = 0;
  for (long long i = 0; i < n; i++) {
    while ((k < i - k2 || a2[k] <= a1[i]) && k < i) k++;
    if (i - k < k2)
      a2[i] = a1[i] + t2;
    else
      a2[i] = max(a2[k], a1[i]) + t2;
  }
  k = 0;
  for (long long i = 0; i < n; i++) {
    while ((k < i - k3 || a3[k] <= a2[i]) && k < i) k++;
    if (i - k < k3)
      a3[i] = a2[i] + t3;
    else
      a3[i] = max(a3[k], a2[i]) + t3;
  }
  long long max = 0;
  for (long long i = 0; i < n; i++)
    if (a3[i] - c[i] > max) max = a3[i] - c[i];
  cout << max;
  return 0;
}
