#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<cmath>
#include<algorithm>
#include<functional>
#include<iomanip>
#include<queue>
#include<ciso646>
#include<random>
#include<map>
#include<set>
#include<complex>
#include<bitset>
#include<stack>
#include<unordered_map>
#include<utility>
using namespace std;
typedef long long ll;
typedef unsigned long long ul;
typedef unsigned int ui;
const ll mod = 1000000007;
typedef long double ld;
typedef complex<ld> Point;
const ll INF = mod * mod;
typedef pair<int, int> P;
#define stop char nyaa;cin>>nyaa;
#define rep(i,n) for(int i=0;i<n;i++)
#define per(i,n) for(int i=n-1;i>=0;i--)
#define Rep(i,sta,n) for(int i=sta;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define per1(i,n) for(int i=n;i>=1;i--)
#define Rep1(i,sta,n) for(int i=sta;i<=n;i++)
const ld eps = 1e-6;
const ld pi = acos(-1.0);
typedef pair<ld, ld> LDP;
typedef pair<ll, ll> LP;

int dx[8] = { 1,1,1,0,-1,-1,-1,0 };
int dy[8] = { 1,0,-1,-1,-1,0,1,1 };

char mp[4][4];
bool used[4][4];

vector<string> v;
string cur;


void dfs(int x,int y) {
	v.push_back(cur);
	if (cur.length() == 8)return;
	rep(k, 8) {
		int nx = x + dx[k], ny = y + dy[k];
		if (nx < 0 || ny < 0 || nx >= 4 || ny >= 4)continue;
		if (used[nx][ny])continue;
		cur.push_back(mp[nx][ny]);
		used[nx][ny] = true;
		dfs(nx, ny);
		used[nx][ny] = false;
		cur.pop_back();
	}
}

int dp[10001];

void solve() {
	sort(v.begin(), v.end());
	int n; cin >> n;
	vector<string> s(n); vector<int> c(n);
	rep(i, n) {
		cin >> s[i] >> c[i];
	}
	rep(i, 4) {
		rep(j, 4)cin >> mp[i][j];
	}
	rep(i, 4) {
		rep(j, 4) {
			cur.push_back(mp[i][j]);
			used[i][j] = true;
			dfs(i, j);
			used[i][j] = false;
			cur.pop_back();
		}
	}
	sort(v.begin(), v.end());
	int t; cin >> t;
	rep(i, n) {
		int num = upper_bound(v.begin(), v.end(), s[i]) - lower_bound(v.begin(), v.end(), s[i]);
		int len = s[i].length();
		per(k, t + 1) {
			
			rep1(j, num) {
				int ni = k + j * len;
				if (ni > t)break;
				dp[ni] = max(dp[ni], dp[k] + j * c[i]);
			}
		}
	}
	int ans = 0;
	rep(i, t + 1)ans = max(ans, dp[i]);
	cout << ans << endl;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	solve();
	//stop
	return 0;
}
