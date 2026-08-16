#include <bits/stdc++.h>
const int MAX = 1e3 + 10;
const int MAXN = 1e3;
const long long MOD = 1e9 + 7;
using namespace std;
int n, k;
int a[MAX];
int Q[MAXN];
int l, r;
int main() {
  ios::sync_with_stdio(0);
  cin >> n >> k;
  for (int i = 1; i <= n; i++) cin >> a[i];
  l = 205, r = 204;
  Q[++r] = a[1];
  for (int i = 2; i <= n; i++) {
    if (r >= l) {
      bool f = 0;
      for (int j = l; j <= r; j++) {
        if (Q[j] == a[i]) {
          f = true;
          break;
        }
      }
      if (f) continue;
    }
    if (r - l + 1 == k) {
      Q[--l] = a[i];
      r--;
    } else {
      Q[--l] = a[i];
    }
  }
  cout << r - l + 1 << endl;
  for (int i = l; i <= r; i++) {
    cout << Q[i] << " ";
  }
  cout << endl;
  return 0;
}
