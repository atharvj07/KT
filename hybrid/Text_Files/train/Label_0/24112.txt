#include <iostream>
using namespace std;

int main() {
    int N,A;
    int x[50];
    cin >> N >> A;
    for(int i=0; i<N; ++i) {
        int tmp; cin >> tmp;
        x[i] = tmp - A;
    }
    long long dp[50][4901] = {0};
    dp[0][2450] = 1;
    dp[0][x[0] + 2450] += 1;
    for(int i=1; i<N; ++i) {
        for(int j=0; j<=4900; ++j) {
            dp[i][j] = dp[i-1][j];
            if(j-x[i] >= 0 && j-x[i] <= 4900) dp[i][j] += dp[i-1][j - x[i]];
        }
    }
    cout << dp[N-1][2450] - 1 << endl;
}