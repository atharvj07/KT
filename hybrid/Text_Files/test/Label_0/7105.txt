#include <bits/stdc++.h>
using namespace std;
int main() {
  string x, c, v, k;
  getline(cin, x);
  int sz = x.size();
  for (int i = 0; i < sz; i++) {
    c += x[i];
    if (x[i] == '!' || x[i] == '?' || x[i] == '.' || x[i] == ',') c += ' ';
  }
  sz = c.size();
  for (int i = 0; i < sz; i++) {
    if (c[i] == ' ' && c[i - 1] == ' ')
      continue;
    else
      v += c[i];
  }
  sz = v.size();
  for (int i = 0; i < sz; i++) {
    if (v[i] == ' ' && (v[i + 1] == '!' | v[i + 1] == '?' || v[i + 1] == '.' ||
                        v[i + 1] == ','))
      continue;
    else
      k += v[i];
  }
  cout << k << endl;
  return 0;
}
