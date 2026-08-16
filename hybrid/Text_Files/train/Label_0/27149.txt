#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  string str;
  cin >> str;
  bool ok = false;
  int l = -1, r = -1;
  for (int i = 1; i < str.length(); i++) {
    if (str[i] < str[i - 1]) {
      l = i, r = i + 1;
      char ch = str[i];
      str[i] = str[i - 1];
      str[i - 1] = ch;
      ok = true;
      break;
    }
  }
  if (ok) {
    cout << "YES\n";
    cout << l << " " << r << "\n";
  } else
    cout << "NO\n";
  return 0;
}
