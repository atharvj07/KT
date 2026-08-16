#include <bits/stdc++.h>
using namespace std;
string pre[4] = {"", "0", "00", "000"};
int T[4] = {1, 10, 100, 1000};
int k, m;
bool v[10000];
int ndgt(int x) {
  for (int i = 0; i < 3; ++i) {
    if (x >= T[3 - i]) return i;
  }
  return 3;
}
bool print(int x, int s) {
  int y = k < s ? s - k : k - s;
  if (y < 10000 && !v[y]) {
    cout << pre[ndgt(y)] << y << pre[ndgt(x)] << x << endl;
    v[y] = true;
    return true;
  }
  return false;
}
int calc(int t, int x) {
  int p = 1;
  int b = 0, a = 0, op_ = 0, z = x;
  for (int i = 0; i < 4; ++i) {
    int op = t % 4;
    t /= 4;
    b += (z % 10) * p;
    if (op == 3) {
      p *= 10;
    } else {
      switch (op_) {
        case 0:
          a = a + b;
          break;
        case 1:
          a = a - b;
          break;
        case 2:
          a = a * b;
          break;
      }
      op_ = op, b = 0, p = 1;
    }
    z /= 10;
  }
  return a;
}
int rep[64];
int main1() {
  int _1, _2;
  while (cin >> _1 >> _2) cout << calc(_1, _2) << endl;
  return 0;
}
int main() {
  while (cin >> k >> m) {
    for (int x = 0; x <= 9999 && m; ++x) {
      memset(v, false, sizeof(v));
      for (int cb = 0; cb < 64; ++cb) {
        int s = calc(cb, x);
        rep[cb] = s;
      }
      sort(rep, rep + 64);
      if (print(x, rep[0])) m--;
      for (int i = 1; i < 64 && m; ++i) {
        if (rep[i] > rep[i - 1]) {
          if (print(x, rep[i])) m--;
        }
      }
    }
  }
  return 0;
}
int main2() {
  string s;
  int cnt = 0;
  while (getline(cin, s)) {
    cnt++;
    if (s.size() != 8) {
      cout << s << endl;
    }
  }
  cout << "cnt=" << cnt << endl;
  return 0;
}
