#include <bits/stdc++.h>
using namespace std;
long long a3, b, t, ans[15], i, j = 1, n, k = 0, l, r, z = 0, sum1, sum2, m, p,
                                a;
string s, s1, s2, v, s3, s4, a1, b1, a2, b2, t1, t2;
stringstream ss, ss1, ss2;
char ch;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  char x1, x2, x3, x4;
  cin >> n;
  a = 1;
  b = 2;
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      if (i + j < (n - 1) / 2 or abs(i - j) > (n - 1) / 2 or
          i + j > 3 * (n - 1) / 2) {
        cout << b << " ";
        b += 2;
      } else {
        cout << a << " ", a += 2;
      }
    }
    cout << "\n";
  }
  return 0;
}
