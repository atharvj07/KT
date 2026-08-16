#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll N, M;
vector<ll> A;
map<ll, ll, greater<ll>> CB;
ll R;

int main() {
  cin >> N >> M;
  A.resize(N);
  for (ll i = 0; i < N; ++i) cin >> A[i];
  sort(A.begin(), A.end());
  for (ll i = 0; i < M; ++i) {
    ll b, c;
    cin >> b >> c;
    CB[c] += b;
  }
  for (ll i = 0; i < N && !CB.empty(); ++i) {
    auto it = CB.begin();
    if (it->first <= A[i]) break;
    A[i] = it->first;
    --it->second;
    if (it->second == 0) CB.erase(it);
  }
  for (ll a : A) R += a;
  cout << R << endl;
  return 0;
}
