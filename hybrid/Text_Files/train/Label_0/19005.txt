#include <bits/stdc++.h>
using namespace std;
long long int solve(long long int a, long long int b) {
  if (a >= 2 * b) {
    return b;
  }
  if (b >= 2 * a) {
    return a;
  }
  return (a + b) / 3;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    long long int a, b;
    cin >> a >> b;
    cout << solve(a, b) << endl;
  }
  return 0;
}
