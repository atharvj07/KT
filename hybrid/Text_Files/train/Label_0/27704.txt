#include <bits/stdc++.h>
using namespace std;
int main() {
  std::ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
  int n;
  long long a, b;
  cin >> n;
  while (n--) {
    cin >> a >> b;
    long long c = a * b;
    bool ok = false;
    long long left = 1, right = 1000001;
    long long ans;
    while (left <= right) {
      long long mid = (left + right) / 2;
      long long now = mid * mid * mid;
      if (now == c) {
        ans = mid;
        ok = 1;
        break;
      }
      if (now > c) right = mid - 1;
      if (now < c) left = mid + 1;
    }
    if (!ok) {
      cout << "No" << '\n';
    } else {
      if (a % ans == 0 && b % ans == 0) {
        cout << "Yes" << '\n';
      } else
        cout << "No" << '\n';
    }
  }
  return 0;
}
