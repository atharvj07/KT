#include <bits/stdc++.h>
using namespace std;
template <typename T>
inline T abs(const T &a) {
  return a < 0 ? -a : a;
}
template <typename T>
inline T min(const T &b, const T &a) {
  return a < b ? a : b;
}
template <typename T>
inline T max(const T &a, const T &b) {
  return a < b ? b : a;
}
int read() {
  int x = 0;
  bool f = 0;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    f = (ch == '-');
    ch = getchar();
  }
  while (ch <= '9' && ch >= '0') {
    x = (x << 1) + (x << 3) + (ch - '0');
    ch = getchar();
  }
  return f ? -x : x;
}
void write(int x) {
  if (x < 0) {
    x = abs(x);
    putchar('-');
  }
  if (x < 10) {
    putchar(x + 48);
    return;
  }
  write(x / 10);
  putchar(x % 10 + 48);
}
const int Maxn = 1e5 + 11;
int t, n, a[Maxn];
int main() {
  ios::sync_with_stdio(false);
  cin >> t;
  while (t--) {
    int cnt = 1;
    cin >> n;
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    sort(a, a + n);
    for (int i = 1; i < n; ++i)
      if (a[i] != a[i - 1]) cnt++;
    cout << cnt << endl;
  }
}
