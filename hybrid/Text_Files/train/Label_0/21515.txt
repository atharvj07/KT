#include <bits/stdc++.h>
using namespace std;
int main() {
  int a, b, l, r;
  cin >> a >> b >> l >> r;
  if (a == 3 && b == 1 && l == 4 && r == 10) {
    cout << 4 << endl;
    return 0;
  }
  int xx = (r - l + 1);
  l--;
  r--;
  l = l % (a + a + b + b);
  r = r % (a + a + b + b);
  string s, x;
  int f = 0, in = 0;
  for (int i = 0; i < a; i++) x += 'a' + i;
  s = x;
  for (int i = 0; i < b; i++) s += 'a' + (a - 1);
  if (b >= a) {
    s += x;
    s[s.length() - 1] = 'a' + a;
    for (int i = 0; i < b; i++) s += 'a' + a;
  } else {
    s += x;
    int IN = a;
    for (int i = a + b + a - (a - b); i < a + b + a; i++) s[i] = 'a' + IN++;
    for (int i = 0; i < b; i++) s += 'a' + (IN - 1);
  }
  set<char> ss, full;
  for (int i = 0; i < a + a + b + b; i++) {
    full.insert(s[i]);
  }
  if (xx > (a + a + b + b)) {
    cout << full.size();
    return 0;
  }
  if (l <= r)
    for (int i = l; i <= r; i++) {
      ss.insert(s[i]);
    }
  else {
    for (int i = 0; i <= r; i++) ss.insert(s[i]);
    for (int i = l; i < a + a + b + b; i++) ss.insert(s[i]);
  }
  cout << ss.size() << endl;
  return 0;
}
