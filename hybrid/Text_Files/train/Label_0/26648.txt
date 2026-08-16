#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  long long ans = 0;
  for (int i = (0); i < (n); ++i) {
    long long t, T, x, cost;
    cin >> t >> T >> x >> cost;
    if (t >= T) {
      ans += cost + m * x;
      continue;
    }
    long long aux1 = cost;
    if (m > (T - t)) aux1 += m * x;
    long long aux2 = (long long)ceil((double)(m - (T - t)) / (T - t)) + 1;
    aux2 *= cost;
    ans += min(aux1, aux2);
  }
  cout << ans << endl;
  return 0;
}
