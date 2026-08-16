#include <bits/stdc++.h>
using namespace std;
const int N = 3e5 + 5;
const int M = 2e3 + 5;
const int mod = 2520;
const int INF = 2e9;
const double eps = 1e-7;
const double pi = acos(-1);
template <class T>
inline void read(T &x) {
  char c;
  x = 1;
  while ((c = getchar()) < '0' || c > '9')
    if (c == '-') x = -1;
  T res = c - '0';
  while ((c = getchar()) >= '0' && c <= '9') res = res * 10 + c - '0';
  x *= res;
}
int n, m;
char str[N];
int f[N];
void solve(int cas) {
  read(n);
  if (n == 2) {
    cout << 1 << endl;
    return;
  } else if (n == 4) {
    cout << 3 << endl;
    return;
  }
  long long ans = 1;
  for (int i = 1; i <= n - 1; i++) {
    ans *= i;
  }
  cout << ans / n * 2 << endl;
}
int main() {
  int t;
  t = 1;
  for (int i = 1; i <= t; i++) {
    solve(i);
  }
  return 0;
}
