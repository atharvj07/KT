#include <bits/stdc++.h>
using namespace std;
ifstream in("date.in");
char s[200001], f;
int sol[200001];
int main() {
  int n, cnt = 0, ok, elem = 0, lngsir = 0, cop;
  cin >> n;
  cop = n;
  while (n--) {
    cin >> f;
    ok = 1;
    for (int i = 0; i < lngsir; ++i) {
      if (s[i] <= f) {
        s[i] = f;
        sol[cop - n] = i + 1;
        ok = 0;
        i = lngsir;
      }
    }
    if (ok == 1) {
      s[lngsir++] = f;
      sol[cop - n] = lngsir;
    }
  }
  cout << lngsir << '\n';
  for (int i = 1; i <= cop; i++) cout << sol[i] << ' ';
  return 0;
}
