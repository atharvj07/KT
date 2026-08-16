#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  long long n, k;
  cin >> n >> k;
  auto count = [&](long long x) {
    if (x % 2 == 1) {
      long long left = x, right = x;
      long long ans = 0;
      while (left <= n) {
        ans += min(right, n) - left + 1;
        left = left * 2;
        right = right * 2 + 1;
      }
      return ans;
    } else {
      long long left = x, right = x + 1;
      long long ans = 0;
      while (left <= n) {
        ans += min(right, n) - left + 1;
        left = left * 2;
        right = right * 2 + 1;
      }
      return ans;
    }
  };
  cerr << count(2) << endl;
  cerr << count(3) << endl;
  long long ans = 1;
  {
    long long low = 1, high = n % 2 == 0 ? n - 1 : n;
    while (low <= high) {
      long long mid = (low + high) / 2;
      if (mid % 2 == 0) {
        if (low < mid) {
          mid--;
        } else {
          mid++;
        }
      }
      long long c = count(mid);
      if (c >= k) {
        ans = max(ans, mid);
        low = mid + 2;
      } else {
        high = mid - 2;
      }
    }
  }
  {
    long long low = 2, high = n % 2 == 0 ? n : n - 1;
    while (low <= high) {
      long long mid = (low + high) / 2;
      if (mid % 2 == 1) {
        if (low < mid) {
          mid--;
        } else {
          mid++;
        }
      }
      long long c = count(mid);
      if (c >= k) {
        ans = max(ans, mid);
        low = mid + 2;
      } else {
        high = mid - 2;
      }
    }
  }
  cout << ans << '\n';
}
