#include <bits/stdc++.h>
using namespace std;
int n;
string s;
int main() {
  cin >> n >> s >> s,
      cout << (s == "week" ? (n == 6 || n == 5 ? 53 : 52)
                           : (n == 31 ? 7 : (n == 30 ? 11 : 12)));
  return 0;
}
