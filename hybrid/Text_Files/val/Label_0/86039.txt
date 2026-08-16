#include <bits/stdc++.h>
using namespace std;
long long freq[63];
int main(){
    cin.sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n; cin >> n;
    long long a, MOD = 1000000007LL, tot = 0;
    for(int i = 0; i < n; ++i){
        cin >> a; for(long long j = 0; j < 63; ++j) if((a >> j) & 1) ++freq[j];
    }
    for(long long i = 0; i < 62; ++i) tot = (tot + (1LL << i) % MOD * freq[i] % MOD * (n - freq[i]) % MOD) % MOD;
    cout << tot << "\n";
}