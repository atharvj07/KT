#include <bits/stdc++.h>
using namespace std;
const int inf = 0x3f3f3f3f;
const int N = 1e5 + 10;
int n;
void work() {
  cin >> n;
  int lst = 2;
  int lstans = 2;
  cout << (2) << endl;
  for (int k = 1; k <= n - 1; k++) {
    long long kk = k + 1;
    cout << ((kk + 2) * (kk * kk) + 1) << endl;
  }
}
int main() { work(); }
