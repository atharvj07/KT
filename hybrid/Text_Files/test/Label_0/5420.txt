#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  long long t, v;
  cin >> t >> v;
  long long a[t];
  for (int i = 0; i < t; i++) cin >> a[i];
  long long minx = 0;
  sort(a, a + t);
  for (int z = 0; z < t - 1; z++) {
    minx = max(a[z + 1] - a[z], minx);
  }
  long long diff = max(a[0] - 0, v - a[t - 1]);
  double re;
  re = max(double(diff), double(minx) / 2.0);
  cout << setprecision(10) << fixed << re;
}
