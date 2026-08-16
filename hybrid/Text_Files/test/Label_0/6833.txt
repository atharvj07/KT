#include <iostream>
#include <vector>
#include <iostream>
using namespace std;
using int64 = long long int;
const int64 MOD = 1000000007;

int64 mod_pow(int64 A, int64 k) {
  int64 res = 1;
  for(; k>0; k>>=1) {
    if(k & 1) (res *= A) %= MOD;
    (A *= A) %= MOD;
  }
  return res;
}

int64 dp[100010];
int main() {
  int N, M; cin >> N >> M;

  dp[0] = 1;
  for(int i=0; i<N; i++) {
    dp[i+1] = dp[i] - (i-M < 0 ? 0 : dp[i-M]);
    (dp[i+1] += MOD) %= MOD;
    // fprintf(stderr, "dp[%d] = %lld\n", i+1, dp[i+1]);
    (dp[i+1] += dp[i]) %= MOD;
  }

  int64 ans = mod_pow(2, N);
  int64 sub = (dp[N] - dp[N-M] + MOD) % MOD;
  (ans += MOD - sub) %= MOD;
  cout << ans << endl;
  return 0;
}

