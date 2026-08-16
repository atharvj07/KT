#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<ll> vi;
#define INF (1e9)

int main() {
  ll N, ans = 0;
  cin >> N;
  vi A(N + 1), B(N + 2);
  for (ll i = 0; i < N + 1; i++) {
    cin >> A[i];
  }
  for (ll i = N; i >= 0; i--) {
    B[i] = B[i + 1] + A[i];
  }

  ll x = 1;
  for (ll i = 0; i < N + 1; i++) {
    // cout << x << endl;
    if (x < A[i]) {
      ans = -1;
      break;
    }

    ans += A[i];
    x -= A[i];
    ans += min(B[i] - A[i], x);
    if (B[i] - A[i] >= x) x *= 2;
  }
  cout << ans << endl;
}

