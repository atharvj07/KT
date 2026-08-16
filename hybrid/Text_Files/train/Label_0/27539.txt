#include <bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[]) {
  int n, k;
  char str[51];
  string s;
  cin >> n >> k >> str;
  s = str;
  int l = 0;
  for (int i = 1; i < n; i++) {
    if (s.substr(0, i) == s.substr(n - i, i)) {
      l = i;
    }
  }
  if (k) {
    cout << str;
  }
  for (int i = 1; i < k; i++) cout << (str + l);
  cout << endl;
  return 0;
}
