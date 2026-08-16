#include <bits/stdc++.h>
using namespace std;
long long l1, r1;
long long l2, r2;
int q;
int main() {
  cin >> q;
  for (int i = 0; i < q; i++) {
    cin >> l1 >> r1 >> l2 >> r2;
    cout << l1 << " ";
    if (l1 == l2) {
      cout << r2;
    } else
      cout << l2;
    cout << endl;
  }
  return 0;
}
