#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
const int mod = 1e9+7;

int main() {
  int N; cin >> N;
  vector<ll> A(N);
  ll ans = 0LL;

  for(int i = 0; i < N; i++) cin >> A[i];
  for(int i = 0; i < 60; i++) {
    ll t = 0;
    for(int j = 0; j < N; j++) {
      if(A[j] & (1LL << i)) t++;
    }
    ans = (ans+(((t*(N-t))%mod)*((1LL<<i)%mod))) % mod;
  }
  cout << ans << endl;
  return 0;
}
