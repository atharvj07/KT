#include <bits/stdc++.h>
using namespace std;
const int N = 500005, mod = 1000000007;
long long int a, b, c, d, e, f, g, h[N], arr[N];
string s;
vector<long long int> v;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cin >> a >> s;
  long long int say = 0, ans = 0;
  for (long long int i = 0; i < a; i++) {
    if (s[i] == ')') {
      if (say > 0)
        say--;
      else {
        long long int bas = i;
        say--;
        while (i < a and say < 0) say += (s[++i] == '(' ? 1 : -1);
        if (say != 0) {
          cout << -1 << endl;
          return 0;
        }
        ans += i - bas + 1;
      }
    } else {
      say++;
    }
  }
  if (say != 0)
    cout << -1 << endl;
  else
    cout << ans << endl;
}
