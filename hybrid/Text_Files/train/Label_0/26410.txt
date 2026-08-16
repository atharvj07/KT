#include <bits/stdc++.h>
using namespace std;
int toInt(string s) {
  int re = 0;
  istringstream is(s);
  is >> re;
  return re;
}
int main() {
  string s;
  int HH, MM;
  cin >> s;
  HH = toInt(s.substr(0, 2)) % 12;
  MM = toInt(s.substr(3, 2));
  if ((HH == 12 || HH == 0) && MM == 0) {
    cout << 0 << " ";
  } else {
    printf("%.11f ", (HH + (double)MM / 60) * 30);
  }
  if (MM == 0) {
    cout << 0;
  } else {
    cout << MM * 6;
  }
}
