#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, i;
  cin >> n;
  string s;
  cin >> s;
  long long int a[n], f[9];
  for (i = 0; i < n; i++) {
    a[i] = (int)(s[i] - '0');
  }
  for (i = 0; i < 9; i++) {
    cin >> f[i];
  }
  int j = 0, k = 0, flag = 0;
  for (i = 0; i < n; i++) {
    if (f[a[i] - 1] >= a[i]) {
      if (f[a[i] - 1] > a[i]) flag = 1;
      a[i] = f[a[i] - 1];
    } else if (flag == 1) {
      break;
    }
  }
  string str = "";
  for (i = 0; i < n; i++) {
    str += (char)('0' + a[i]);
  }
  cout << str << endl;
}
