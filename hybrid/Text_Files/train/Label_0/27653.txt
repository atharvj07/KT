#include <bits/stdc++.h>
#pragma GCC optimize(2)
#pragma G++ optimize(2)
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
long long rd() {
  long long x = 0, f = 1;
  char ch = getchar();
  while (ch < '0' || ch > '9') {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (ch >= '0' && ch <= '9') {
    x = x * 10 + ch - '0';
    ch = getchar();
  }
  return x * f;
}
const int maxn = 100010;
int t;
long long n;
int main() {
  cin >> t;
  while (t--) {
    cin >> n;
    long long y = 1;
    for (; y * (y - 1) / 2 <= n; y++)
      ;
    y--;
    n -= y * (y - 1) / 2;
    cout << "133";
    y -= 2;
    for (int i = 1; i <= n; ++i) {
      printf("7");
    }
    for (int i = 1; i <= y; ++i) {
      printf("3");
    }
    cout << "7" << endl;
  }
}
