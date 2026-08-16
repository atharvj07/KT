#include <bits/stdc++.h>
using namespace std;
const long long int Maxn3 = 1e3 + 10;
const long long int Maxn4 = 1e4 + 10;
const long long int Maxn5 = 1e5 + 10;
const long long int Maxn6 = 1e6 + 10;
const long long int Maxn7 = 1e7 + 10;
const long long int Maxn8 = 1e8 + 10;
const long long int Maxn9 = 1e9 + 10;
const long long int Maxn18 = 1e18 + 10;
const long long int Mod1 = 1e7 + 7;
const long long int Mod2 = 1e9 + 7;
const long long int LLMax = LLONG_MAX;
const long long int LLMin = LLONG_MIN;
const long long int INTMax = INT_MAX;
const long long int INTMin = INT_MIN;
long long int mn = LLMax, mx = LLMin;
int main() {
  ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
  long long int n, a, b, ans = 0;
  cin >> n >> a >> b;
  a--;
  b--;
  while (a != b) {
    a /= 2;
    b /= 2;
    ans++;
    n /= 2;
  }
  if (n == 1)
    cout << "Final!";
  else
    cout << ans;
}
