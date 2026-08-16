#include <bits/stdc++.h>
using namespace std;
long long n, a[100007], d, t;
int main() {
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> a[i];
  sort(a + 1, a + (n + 1));
  for (int i = 1; i <= n; i++) {
    if (t <= a[i]) {
      d++;
      t += a[i];
    }
  }
  cout << d;
  return 0;
}
