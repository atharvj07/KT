#include <bits/stdc++.h>
using namespace std;
int main() {
  string a;
  int count = 0;
  cin >> a;
  for (auto i = 0; i < a.length() / 2; ++i) {
    if (a[i] != a[a.length() - (i + 1)]) count++;
  }
  if (count == 1)
    cout << "YES";
  else if (!count) {
    if (a.length() & 1)
      cout << "YES";
    else
      cout << "NO";
  } else
    cout << "NO";
}
