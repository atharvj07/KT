#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, y, x, sum = 0;
  string str;
  cin >> n >> x >> y >> str;
  int len = str.size() - 1;
  for (int i = len; i > len - x; i--) {
    if (str[i] == '1') sum++;
  }
  if (str[len - y] == '0')
    sum++;
  else
    sum--;
  cout << sum << endl;
  return 0;
}
