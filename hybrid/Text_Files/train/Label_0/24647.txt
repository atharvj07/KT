#include <bits/stdc++.h>
using namespace std;
int x[1234567], n, a, s, d, f, c, t;
int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> x[i];
    if (x[i] == 1)
      a++;
    else if (x[i] == 2)
      s++;
    else if (x[i] == 3)
      d++;
    else if (x[i] == 4)
      f++;
  }
  c = f;
  while (d != 0 && a != 0 && t != d) {
    if (a - 1 < 0) break;
    a--;
    t++;
  }
  c += d;
  t = 0;
  while (s != 0 && a != 0 && (t / 2) != s) {
    if (a - 2 < 0) {
      if (a - 1 < 0)
        break;
      else {
        a--;
        t++;
        break;
      }
    }
    a -= 2;
    t += 2;
  }
  c += (t / 2) + (t % 2);
  s -= ((t / 2) + (t % 2));
  if (s != 0) {
    s *= 2;
    c += (s / 4) + ((s % 4) / 2);
  }
  if (a != 0) {
    c += (a / 4);
  }
  if (a % 4 != 0) c++;
  cout << c;
}
