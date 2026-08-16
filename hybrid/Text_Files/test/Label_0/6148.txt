#include <bits/stdc++.h>
using namespace std;
long long int solve(long long int x, long long int y, long long int k) {
  if (x == y && x % k == 0) return 1;
  if (x == y && x % k != 0) return 0;
  if (y - ((x / k) * k + k) >= 0) {
    if (x % k != 0) return ((y - ((x / k) * k + k)) / k) + 1;
    return ((y - ((x / k) * k + k)) / k) + 2;
  } else {
    if (x % k == 0)
      return 1;
    else
      return 0;
  }
}
int main() {
  long long int a, b, p, res = 0;
  cin >> p >> a >> b;
  if (a >= 0 && b >= 0)
    res = solve(a, b, p);
  else if (a < 0 && b >= 0)
    res = solve(1, -a, p) + solve(0, b, p);
  else
    res = solve(-b, -a, p);
  cout << res << endl;
  return 0;
}
