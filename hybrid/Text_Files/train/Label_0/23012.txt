#include <bits/stdc++.h>
using namespace std;
long long fastPow(long long a, long long p) {
  long long res = 1;
  while (p) {
    if (p & 1) res = (res * a) % 1000000007;
    p >>= 1;
    a = (a * a) % 1000000007;
  }
  return res;
}
long long gcd(long long a, long long b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}
void solve(int num) {
  int n;
  cin >> n;
  int a[n];
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  sort(a, a + n);
  vector<int> ans, used(n, 0);
  used[n - 1] = 1;
  ans.push_back(a[n - 1]);
  int last = a[n - 1];
  for (int i = 1; i < n; ++i) {
    int take, maks = -1, cek;
    for (int j = n - 1; j >= 0; --j) {
      if (used[j] == 0) {
        cek = gcd(last, a[j]);
        if (maks < cek) {
          maks = cek;
          take = j;
        }
      }
    }
    last = maks;
    ans.push_back(a[take]);
    used[take] = 1;
  }
  for (auto i : ans) {
    cout << i << " ";
  }
  cout << "\n";
}
int main() {
  int tc = 1, num = 0;
  cin >> tc;
  while (tc--) {
    ++num;
    solve(num);
  }
  return 0;
}
