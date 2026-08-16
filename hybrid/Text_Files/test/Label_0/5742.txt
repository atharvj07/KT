#include <bits/stdc++.h>
using namespace std;
const int INF = 0x3f3f3f3f;
const int MAXN = 1e6 + 10;
const int MOD = 1000000007;
int main() {
  long long n;
  cin >> n;
  long long s = 0;
  long long tmp;
  for (long long i = 1; i <= n; ++i) {
    cin >> tmp;
    s += tmp - 1;
    if (s & 1)
      cout << 1 << endl;
    else
      cout << 2 << endl;
  }
  return 0;
}
