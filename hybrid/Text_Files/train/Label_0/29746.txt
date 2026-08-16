#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  int flag = 1;
  string str;
  cin >> n;
  while (n--) {
    cin >> str;
    int len = str.length();
    for (int i = 0; i < len / 2; i++) {
      if (str[i] != str[len - 1 - i]) {
        flag = 0;
      }
    }
    if (flag) {
      sort(str.begin(), str.end());
      if (str[0] == str[len - 1]) {
        cout << -1 << endl;
        continue;
      }
    }
    cout << str << endl;
    flag = 1;
  }
  return 0;
}
