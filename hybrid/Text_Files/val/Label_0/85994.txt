#include <bits/stdc++.h>
using namespace std;
int main() {
  long long hh, mm, x, ans = 0;
  cin >> x >> hh >> mm;
  while (hh % 10 != 7 && mm % 10 != 7) {
    mm -= x;
    if (mm < 0) {
      mm = mm + 60;
      hh = hh - 1;
    }
    if (hh < 0) {
      hh = 23;
    }
    ans++;
  }
  cout << ans;
  return 0;
}
