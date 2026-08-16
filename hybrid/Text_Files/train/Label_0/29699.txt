#include <bits/stdc++.h>
#pragma warning(disable : 4996)
using namespace std;
template <class T>
inline void chkmin(T &a, T b) {
  if (a > b) a = b;
}
template <class T>
inline void chkmax(T &a, T b) {
  if (a < b) a = b;
}
const int MAXN = 2e5 + 7;
long long a[MAXN];
int x[MAXN];
long long b[MAXN];
int main() {
  ios_base::sync_with_stdio(false);
  int n;
  long long t;
  cin >> n >> t;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  for (int i = 0; i < n; ++i) {
    cin >> x[i];
    --x[i];
    if (x[i] < i) {
      cout << "No\n";
      return 0;
    }
    if (i) {
      if (x[i - 1] > x[i]) {
        cout << "No\n";
        return 0;
      }
      if (x[i - 1] != x[i]) {
        if (x[i - 1] != i - 1) {
          cout << "No\n";
          return 0;
        }
        b[i - 1] = a[i - 1] + t;
      } else {
        b[i - 1] = a[i] + t;
      }
    }
  }
  b[n - 1] = a[n - 1] + t;
  for (int i = 1; i < n - 1; ++i) {
    if (b[i] == b[i - 1] && a[i + 1] == a[i] + 1) {
      cout << "No\n";
      return 0;
    }
    chkmax(b[i], b[i - 1] + 1);
  }
  if (n >= 2) chkmax(b[n - 1], b[n - 2] + 1);
  cout << "Yes\n";
  for (int i = 0; i < n; ++i) {
    cout << b[i] << ' ';
  }
  cout << '\n';
}
