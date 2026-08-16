#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, max1, i, min1, premax, premin, count = 0, a[100000];
  cin >> n;
  cin >> a[1];
  premin = a[1];
  min1 = a[1];
  premax = a[1];
  max1 = a[1];
  for (i = 2; i <= n; i++) {
    cin >> a[i];
    min1 = min(a[i], min1);
    max1 = max(a[i], max1);
    if ((premax != max1) || (premin != min1)) {
      count++;
    }
    premax = max1;
    premin = min1;
  }
  cout << count;
  return 0;
}
