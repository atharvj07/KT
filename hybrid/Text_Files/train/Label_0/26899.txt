#include <bits/stdc++.h>
using namespace std;

int64_t MOD;
void add(int64_t& a, int64_t b){
    a = (a+b) % MOD;
}
void mul(int64_t& a, int64_t b){
    a = a*b % MOD;
}

int main(){
    int N, K;
    cin >> N >> K >> MOD;

    int64_t pow[302][302] = {0};
    for(int i=1; i<=301; i++){
        pow[i][0] = 1;
        for(int j=1; j<=301; j++) pow[i][j] = pow[i][j-1] * i % MOD;
    }

    int64_t sub[302][302] = {0};
    sub[0][0] = 1;
    for(int i=1; i<=301; i++) for(int j=0; j<=301; j++) for(int k=0; j+k<=301; k++) add(sub[i][j+k], sub[i-1][j] * pow[i][k]);

    int64_t dp[301][301] = {0};
    dp[0][0] = 1;
    for(int i=1; i<=300; i++) for(int j=0; j<=300; j++) for(int k=0; j+k<=300; k++) add(dp[i][j+k], dp[i-1][j] * sub[j+1][k]);

    cout << dp[K][N] << endl;
    return 0;
}
