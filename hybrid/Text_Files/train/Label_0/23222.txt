#include <bits/stdc++.h>
using namespace std;
ofstream fo("test.out");
ifstream fi("test.inp");
const long long MOD = 1e9 + 7;
const long long base = 269;
const int N = 1e5 + 5;
long long n, m, q, K, pos, t, rs, r;
long long cnt10, cnt11;
string s, a, b;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> n;
  cin >> a >> b;
  for (long long(i) = 0; (i) < (n); (i)++) {
    if (a[i] == '1' && b[i] == '0') cnt10++;
    if (a[i] == '1' && b[i] == '1') cnt11++;
  }
  for (long long(i) = 0; (i) < (n); (i)++) {
    if (a[i] == '0' && b[i] == '0') {
      rs += cnt11;
      rs += cnt10;
    }
    if (a[i] == '0' && b[i] == '1') rs += cnt10;
  }
  cout << rs;
}
