#include <bits/stdc++.h>
using namespace std;
template <class T>
inline T lcm(T a, T b) {
  if (a < 0) return lcm(-a, b);
  if (b < 0) return lcm(a, -b);
  return a * (b / (gcd(a, b)));
}
template <class T>
inline T gcd(T a, T b) {
  if (a < 0) return gcd(-a, b);
  if (b < 0) return gcd(a, -b);
  return (b == 0) ? a : gcd(b, a % b);
}
template <class T1>
void deb(T1 e) {
  cout << e << endl;
}
template <class T1, class T2>
void deb(T1 e1, T2 e2) {
  cout << e1 << " " << e2 << endl;
}
template <class T1, class T2, class T3>
void deb(T1 e1, T2 e2, T3 e3) {
  cout << e1 << " " << e2 << " " << e3 << endl;
}
template <class T1, class T2, class T3, class T4>
void deb(T1 e1, T2 e2, T3 e3, T4 e4) {
  cout << e1 << " " << e2 << " " << e3 << " " << e4 << endl;
}
template <class T1, class T2, class T3, class T4, class T5>
void deb(T1 e1, T2 e2, T3 e3, T4 e4, T5 e5) {
  cout << e1 << " " << e2 << " " << e3 << " " << e4 << " " << e5 << endl;
}
template <class T1, class T2, class T3, class T4, class T5, class T6>
void deb(T1 e1, T2 e2, T3 e3, T4 e4, T5 e5, T6 e6) {
  cout << e1 << " " << e2 << " " << e3 << " " << e4 << " " << e5 << " " << e6
       << endl;
}
int main() {
  int i, j, x, y, a, d, n, res = -1;
  int days[100010];
  n = ({
    int a;
    scanf("%d", &a);
    a;
  });
  x = ({
    int a;
    scanf("%d", &a);
    a;
  });
  y = ({
    int a;
    scanf("%d", &a);
    a;
  });
  for (i = 1; i <= n; i++) {
    a = ({
      int a;
      scanf("%d", &a);
      a;
    });
    days[i] = a;
  }
  for (i = 1; i <= n; i++) {
    bool success = true;
    for (j = i; j <= max(1, i - x); j++) {
      if (days[j] < days[i]) success = false;
    }
    if (!success) continue;
    for (j = i; j <= min(i + y, n); j++) {
      if (days[j] < days[i]) success = false;
    }
    if (!success)
      continue;
    else {
      res = i;
      break;
    }
  }
  cout << res << endl;
  return 0;
}
