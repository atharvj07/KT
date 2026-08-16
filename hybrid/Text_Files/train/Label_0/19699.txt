#include <bits/stdc++.h>
using namespace std;
void quicken() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
}
int main() {
  quicken();
  int q;
  cin >> q;
  long long l1, r1, l2, r2;
  while (q--) {
    cin >> l1 >> r1 >> l2 >> r2;
    if (l1 != l2)
      cout << l1 << " " << l2 << '\n';
    else if (r1 != r2)
      cout << r1 << " " << r2 << '\n';
    else
      cout << l1 << " " << l1 + 1 << '\n';
  }
  return 0;
}
