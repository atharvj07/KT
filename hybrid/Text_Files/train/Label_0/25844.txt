#include <bits/stdc++.h>
using namespace std;
string s;
int xin;
bool cek(int x) {
  if ((int)sqrt(x) * (int)sqrt(x) == x)
    return true;
  else
    return false;
}
int main() {
  cin >> s;
  xin = s.size() + 1;
  for (int i = 1; i < (1 << s.size()); i++) {
    int cur = 0;
    int now = i;
    int satu = 0;
    int res = 0;
    bool flag = false;
    while (now) {
      if (now % 2 == 1 and !(s[cur] == '0' and res == 0)) {
        flag = true;
        res *= 10;
        res += (s[cur] - '0');
        satu++;
      }
      now /= 2;
      cur++;
    }
    if (flag and cek(res)) {
      xin = min(xin, (int)s.size() - satu);
    }
  }
  if (xin == s.size() + 1)
    printf("-1\n");
  else
    printf("%d\n", xin);
}
