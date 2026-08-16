#include <bits/stdc++.h>
using namespace std;
string a, b;
int main() {
  string a, b;
  cin >> a >> b;
  for (int i = 0; i < a.size(); i++) {
    if (char(tolower(a[i])) == char(tolower(b[i]))) {
      continue;
    } else if (char(tolower(a[i])) > char(tolower(b[i]))) {
      cout << 1 << endl;
      return 0;
    } else if (char(tolower(a[i])) < char(tolower(b[i]))) {
      cout << -1 << endl;
      return 0;
    }
  }
  cout << 0 << endl;
}
