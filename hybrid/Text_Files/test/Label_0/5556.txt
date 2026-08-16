#include <bits/stdc++.h>
using namespace std;
int main() {
  string s, l;
  cin >> s;
  int a = 0;
  l = "heidi";
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == l[a]) a++;
  }
  if (a >= 5)
    cout << "YES";
  else
    cout << "NO";
  return 0;
}
