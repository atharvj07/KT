#include <bits/stdc++.h>
using namespace std;
int n;
int read() {
  int x = 0, f = 1;
  char ch;
  while ((ch = getchar()) < '0' || ch > '9') {
    if (ch == '-') {
      x = -1;
    }
  }
  while (ch >= '0' && ch <= '9') {
    x = x * 10 + ch - 48;
    ch = getchar();
  }
  return x * f;
}
int main() {
  n = read();
  if (n == 1) {
    cout << -1 << endl;
  } else {
    cout << n << ' ' << n + 1 << ' ' << n * (n + 1);
  }
  return 0;
}
