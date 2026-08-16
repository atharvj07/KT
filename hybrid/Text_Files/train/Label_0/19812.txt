#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[]) {
  int a1, a2, a3, a4;
  cin >> a1 >> a2 >> a3 >> a4;
  string s = "";
  if (abs(a3 - a4) > 1 || min(a1, a2) < max(a3, a4) ||
      (a3 == a4 && max(a1, a2) <= a3)) {
    cout << -1;
    return 0;
  } else {
    if (a3 > a4) {
      while (a3--) {
        s += '4';
        s += '7';
        a1--;
        a2--;
      }
    } else if (a3 < a4) {
      while (a4--) {
        s += '7';
        s += '4';
        a1--;
        a2--;
      }
    } else {
      if (a1 == a3) {
        s += '7';
        a2--;
        while (a3--) {
          s += '4';
          s += '7';
          a1--;
          a2--;
        }
      } else {
        s += '4';
        a1--;
        while (a3--) {
          s += '7';
          s += '4';
          a1--;
          a2--;
        }
      }
    }
  }
  if (s[s.length() - 1] == '4') {
    for (int i = 0; i < s.length() - 1; i++) {
      if (s[i] == '4' && a1) {
        while (a1 > 0) {
          cout << '4';
          a1--;
        }
      }
      cout << s[i];
    }
    while (a2 > 0) {
      cout << '7';
      a2--;
    }
    cout << 4;
  } else {
    while (a2 > 0) {
      s += '7';
      a2--;
    }
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == '4') {
        while (a1 > 0) {
          cout << '4';
          a1--;
        }
      }
      cout << s[i];
    }
  }
  return 0;
}
