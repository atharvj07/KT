#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main()
{
    string S;
    cin >> S;
    const int N = S.size();
    vector<int> s(N + 1, 0);
    vector<ll> p(N + 1, 1LL);
    for (int i = N - 1; i >= 0; i--) { s[i] = s[i + 1] + S[i] - '0', p[i] = p[i + 1] * (S[i] - '0' + 1); }
    const int Sum = s[0];
    const ll Prod = p[0];
    vector<map<ll, ll>> dp(9 * N + 1);
    dp[0][1] = 1;
    ll prev = 0;
    for (int i = N - 1; i >= 0; i--) {
        const int d = S[i] - '0';
        for (int j = 0; j < d; j++) {
            if (p[i] % (j + 1) != 0) { continue; }
            const int S = s[i] - j;
            const ll P = p[i] / (j + 1);
            prev += (dp[S].find(P) == dp[S].end() ? 0LL : dp[S][P]);
        }
        vector<map<ll, ll>> tmp(9 * N + 1);
        for (int j = 0; j <= 9 * N; j++) {
            for (const auto& e : dp[j]) {
                for (int k = 0; k < 10; k++) { tmp[j + k][e.first * (k + 1)] += e.second; }
            }
        }
        dp = tmp;
    }
    ll ans = 0;
    for (int i = 0; i < Sum; i++) {
        for (const auto& e : dp[i]) { ans += e.second; }
    }
    for (const auto& e : dp[Sum]) { ans += (e.first < Prod ? e.second : 0LL); }
    cout << ans + prev << endl;
    return 0;
}

