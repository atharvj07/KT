#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007;
int main() {
  ios_base::sync_with_stdio(0);
  long long n;
  cin >> n;
  for (long long i = 1; i <= n; i++) {
    long long start = (i == 1) ? 2 : 0;
    cout << (i + 1) * (i + 1) * i - i + 1 - start << endl;
  }
  return 0;
}
