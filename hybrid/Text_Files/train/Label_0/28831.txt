#include <bits/stdc++.h>
using namespace std;
string pat;
int n;
int bal;
int main() {
  cin >> n;
  cin >> pat;
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    if (s[0] == pat[0] && s[1] == pat[1] && s[2] == pat[2]) bal++;
    if (s[5] == pat[0] && s[6] == pat[1] && s[7] == pat[2]) bal--;
  }
  if (bal)
    cout << "contest\n";
  else
    cout << "home\n";
  return 0;
}
