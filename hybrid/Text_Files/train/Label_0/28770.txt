#include <bits/stdc++.h>

#define dbg(x) cerr<<#x": "<<x<<"\n"
#define dbg_p(x) cerr<<#x": "<<x.first<<","<<x.second<<"\n"
#define dbg_v(x, n) do{cerr<<#x"[]: ";for(long long _=0;_<n;++_)cerr<<x[_]<<" ";cerr<<'\n';}while(0)
#define dbg_ok cerr<<"OK!\n"

#define st first
#define nd second

#define DMAX 200100
#define MOD 998244353

using namespace std;

long long n, k, sum, dp[DMAX][5][5], dp2[DMAX], ans;

string s;

template<class T>
ostream& operator<<(ostream& out, vector<T> v) {
	out << v.size() << '\n';
	for(auto e : v) out << e << ' ';
	return out;
}

bool same() {
	for(long long i = 1; i < n; i++) 
		if(s[i] != s[i - 1])
			return 0;
	return 1;
}
bool dif() {
	for(long long i = 1; i < n; i++) 
		if(s[i] == s[i - 1])
			return 0;
	return 1;
}

int main() {
	ios_base::sync_with_stdio(false);

	cin >> s;
	n = s.size();
	if(same()) {
		cout << 1 << '\n';
		return 0;
	}
	if(s.size() == 2)	{
		cout << 2 << '\n';
		return 0;
	}
	if(s.size() == 3) {
		if(s[0] != s[1] && s[1] != s[2] && s[2] != s[0])
			cout << 3 << '\n';
		else if(s[0] == s[2]) cout << 7 << '\n';
		else cout << 6 << '\n';
		return 0;
	}

	for(long long i = 0; i < n; i++) sum += (s[i] - 'a');
	sum %= 3;

	dp[1][0][0] = 1;
	dp[1][1][1] = 1;
	dp[1][2][2] = 1;

	for(long long i = 2; i <= n; i++)
		for(long long j = 0; j < 3 ; j++)
			for(long long k = 0; k < 3; k++)
				for(long long kk = 0; kk < 3; kk++)
					if(kk != k)
						dp[i][j][k] += (dp[i - 1][(3 + j - k) % 3][kk]) % MOD;


	dp2[1] = 1;

	for(long long i = 2; i <= n; i++) {
		dp2[i] = (dp2[i - 1] * 3) % MOD;
	}

	ans = ((dp2[n] - dp[n][sum][0] - dp[n][sum][1] - dp[n][sum][2]) % MOD + MOD) % MOD;
	cout << ans + dif() << '\n';
	// cout << (dp2[n] - dp[n][sum][0] - dp[n][sum][1] - dp[n][sum][2]) << '\n';
}