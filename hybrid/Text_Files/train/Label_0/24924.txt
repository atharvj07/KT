#include <bits/stdc++.h>
using namespace std;
bool check(char s) {
  if (s == 'A' || s == 'H' || s == 'I' || s == 'M' || s == 'O' || s == 'T' ||
      s == 'U' || s == 'V' || s == 'W' || s == 'X' || s == 'Y')
    return true;
  else
    return false;
}
int main() {
  int n, i, x, p;
  bool ans = true;
  string st;
  cin >> st;
  n = st.size();
  if (n == 1 && check(st[0]) == true) {
    cout << "YES\n";
    ;
  } else if (n == 2 && st[0] == st[1] && check(st[0]) == true) {
    cout << "YES\n";
    ;
  } else if (n >= 3) {
    ans = true;
    x = 0, p = n - 1;
    while (x <= p) {
      if (st[x] == st[p] && check(st[x]) == true) {
        x += 1, p -= 1;
      } else {
        ans = false;
        break;
      }
    }
    if (ans == false) {
      cout << "NO\n";
      ;
    } else {
      cout << "YES\n";
      ;
    }
  } else {
    cout << "NO\n";
    ;
  }
}
