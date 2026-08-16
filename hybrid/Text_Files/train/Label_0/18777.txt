#include <bits/stdc++.h>
using namespace std;
int main() {
  string a, b;
  cin >> a;
  int i, st, last, jump;
  b.push_back('A');
  for (i = 0; a[i]; i++) {
    b.push_back(a[i]);
  }
  b.push_back('A');
  int mn = 0;
  for (i = 0; i < b.size(); i++) {
    if (b[i] == 'A' || b[i] == 'E' || b[i] == 'I' || b[i] == 'O' ||
        b[i] == 'U' || b[i] == 'Y') {
      st = i;
      i++;
      if (i == b.size()) break;
      while (b[i] != 'A' && b[i] != 'E' && b[i] != 'I' && b[i] != 'O' &&
             b[i] != 'U' && b[i] != 'Y') {
        i++;
        if (i == b.size()) break;
      }
      last = i;
      jump = last - st;
      mn = max(mn, jump);
      i--;
    }
  }
  cout << mn;
}
