#include <bits/stdc++.h>
using namespace std;
long long n, m, ans1, ans2, ass = -9999999999;
long long a[200100];
long long b[200100];
long long ab[400100];
int main() {
  ios::sync_with_stdio(false);
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    ab[i] = a[i];
  }
  cin >> m;
  for (int i = 0; i < m; i++) {
    cin >> b[i];
    ab[i + n] = b[i];
  }
  sort(a, a + n);
  sort(b, b + m);
  sort(ab, ab + n + m);
  for (int i = 0; i < n + m; i++) {
    long long k = ab[i] - 1;
    long long st1 = 0, en1 = n;
    while (st1 + 1 < en1) {
      long long mid1 = (st1 + en1) / 2;
      if (a[mid1] <= k)
        st1 = mid1;
      else
        en1 = mid1;
    }
    long long st2 = 0, en2 = m;
    while (st2 + 1 < en2) {
      long long mid2 = (st2 + en2) / 2;
      if (b[mid2] <= k)
        st2 = mid2;
      else
        en2 = mid2;
    }
    long long x, y;
    if (a[st1] > k) {
      x = 3 * n;
    } else {
      x = 2 * (st1 + 1) + 3 * (n - st1 - 1);
    }
    if (b[st2] > k) {
      y = 3 * m;
    } else {
      y = 2 * (st2 + 1) + 3 * (m - st2 - 1);
    }
    if (x - y > ass) {
      ass = x - y;
      ans1 = x;
      ans2 = y;
    } else {
      if (x - y == ass && x > ans1) {
        ass = x - y;
        ans1 = x;
        ans2 = y;
      }
    }
  }
  long long x = 2 * n, y = 2 * m;
  if (x - y > ass) {
    ass = x - y;
    ans1 = x;
    ans2 = y;
  } else {
    if (x - y == ass && x > ans1) {
      ass = x - y;
      ans1 = x;
      ans2 = y;
    }
  }
  cout << ans1 << ":" << ans2 << endl;
  return 0;
}
