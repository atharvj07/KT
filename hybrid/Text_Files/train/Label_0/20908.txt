#include <bits/stdc++.h>
using namespace std;
long long t, a, b;
int main() {
  cin >> t >> a >> b;
  if (t == 1) {
    if (a == 1 && b == 1) {
      cout << "inf" << endl;
      return 0;
    } else if (a == 1) {
      cout << 0 << endl;
      return 0;
    } else {
      int flag = 0;
      long long p = 1;
      while (p <= b / a) {
        p *= a;
        if (p == b) flag = 1;
      }
      if (flag) {
        cout << 1 << endl;
        return 0;
      }
    }
  }
  int cnt = 0;
  long long p = 0, q = 1, r = b;
  while (r && cnt < 100) {
    p += r % a * q;
    r /= a;
    q *= t;
    cnt++;
  }
  cout << (p == a) + (cnt > 1 && a == b) << endl;
  return 0;
}
