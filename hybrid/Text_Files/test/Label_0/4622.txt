#include <bits/stdc++.h>
using namespace std;
string drawline(int i, int n) {
  string str(2 * (n - i), ' ');
  for (int c = 0; c <= i; c++) {
    if (c) {
      str.push_back(' ');
    }
    str.push_back(c + '0');
  }
  for (int c = i - 1; c >= 0; c--) {
    str.push_back(' ');
    str.push_back(c + '0');
  }
  return str;
}
int main() {
  int n;
  cin >> n;
  for (int i = 0; i <= n; i++) {
    cout << drawline(i, n) << endl;
  }
  for (int i = n - 1; i >= 0; i--) {
    cout << drawline(i, n) << endl;
  }
  return 0;
}
