#include <bits/stdc++.h>
     
#define all(A) begin(A), end(A)
#define rall(A) rbegin(A), rend(A)
#define sz(A) int(A.size())
#define pb push_back
#define mp make_pair
     
using namespace std;
     
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef vector <int> vi;
typedef vector <ll> vll;
typedef vector <pii> vpii;
typedef vector <pll> vpll;

int main () {
  ios::sync_with_stdio(false); cin.tie(0);
  int tt;
  cin >> tt;
  while (tt--) {
    int n;
    cin >> n;
    vll x(n);
    vll y(n);
    int z1 = 0;
    int z2 = 0;
    for (int i = 0; i < 2 * n; i++) {
      ll a, b;
      cin >> a >> b;
      if (a == 0) y[z2++] = b * b;
      if (b == 0) x[z1++] = a * a;
    }
    assert(z1 == n);
    assert(z2 == n);
    sort(all(x));
    sort(all(y));
    long double ans = 0;
    for (int i = 0; i < n; i++) {
      ans += sqrtl(x[i] + y[i]);
    }
    cout << fixed << setprecision(15) << ans << '\n';
  }
  return (0);
}
