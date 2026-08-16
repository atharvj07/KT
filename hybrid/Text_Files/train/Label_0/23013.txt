#include <bits/stdc++.h>
using namespace std;
const int m = 1e6 + 3;
int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a % b);
}
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  while (T--) {
    int n;
    cin >> n;
    vector<int> a(n), c;
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    vector<bool> b(n);
    c.push_back(n - 1);
    b[n - 1] = 1;
    int m = a.back();
    for (int i = 1; i < n; i++) {
      int p = -1, q = -1;
      for (int j = 0; j < n; j++) {
        if (!b[j] && gcd(a[j], m) > p) {
          p = gcd(a[j], m);
          q = j;
        }
      }
      c.push_back(q);
      b[q] = 1;
      m = p;
    }
    for (auto i : c) cout << a[i] << ' ';
    cout << endl;
  }
}
