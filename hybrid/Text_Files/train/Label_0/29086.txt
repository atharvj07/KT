#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int MAX_N  = 3009;
int N, T;
int A[MAX_N], B[MAX_N];

void solve()
{
	vector<pair<int,int>> v;
	for(int i=0;i<N;++i) v.emplace_back(A[i],B[i]);
	sort(v.begin(),v.end());
    vector< int > dp(T + 1);
    for(const auto &p : v) {
        for(int k = T - 1; k >= 0; k--) {
            dp[min(T, k + p.first)] = max(dp[min(T, k + p.first)],  dp[k] + p.second);
        }
    }
    cout << dp.back() << endl;
}

int main()
{
	cin >> N >> T;
	for(int i=0;i<N;++i) cin >> A[i] >> B[i];
	solve();
	return 0;
}