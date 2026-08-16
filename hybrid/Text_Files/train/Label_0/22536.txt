#include <bits/stdc++.h>
using namespace std;
string s = "";
int n;
int main() {
  cin >> n;
  while (n >= 4) {
    s += "abcd";
    n -= 4;
  }
  if (n == 1) s += "a";
  if (n == 2) s += "ab";
  if (n == 3) s += "abc";
  cout << s << "\n";
}
