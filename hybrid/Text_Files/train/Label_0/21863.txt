#include <bits/stdc++.h>
using namespace std;
long long To_Int(long long p, long long z) {
  long long ans = 0;
  for (long long i = 0; i <= p; i++) ans += (i != z) * (1LL << i);
  return ans;
}
int main() {
  long long l, r;
  cin >> l >> r;
  bitset<64> L(l), R(r);
  long long posL, posR;
  for (int i = 0; i < 64; i++) {
    if (L[i]) posL = i + 1;
    if (R[i]) posR = i + 1;
  }
  long long ans = 0;
  for (long long i = posL - 1LL; i <= posR - 1LL; i++) {
    for (long long j = 0; j < i; j++) {
      long long xx = To_Int(i, j);
      if (xx >= l and xx <= r) ans++;
    }
  }
  cout << ans;
}
