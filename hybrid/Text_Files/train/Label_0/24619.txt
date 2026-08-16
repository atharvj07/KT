#include <bits/stdc++.h>
using namespace std;
#define FOR(i,k,n) for(int i = (k); i < (n); i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(), a.end()
#define MS(m,v) memset(m,v,sizeof(m))
#define D10 fixed<<setprecision(10)
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
const int MOD = 1000000007;
const int INF = MOD + 1;
const ld EPS = 0.0000001;
template<class T> T &chmin(T &a, const T &b) { return a = min(a, b); }
template<class T> T &chmax(T &a, const T &b) { return a = max(a, b); }

/*--------------------template--------------------*/

int main()
{
	int t;
	cin >> t;
	ld mx = 0;
	REP(i, t)
	{
		int n, m;
		cin >> n >> m;
		ld sum = 0;
		ld ex = 0;
		REP(j, m)
		{
			int v; ld r;
			cin >> v >> r;
			ex += v*r;
			sum += r;
		}
		chmax(mx, ex*(1 / sum));
	}
	int p, q;
	cin >> p >> q;
	ld sum = 0;
	ld ex = 0;
	REP(j, q)
	{
		int v; ld r;
		cin >> v >> r;
		ex += v*r;
		sum += r;
	}
	if (mx - ex*(1/sum) > EPS) puts("YES");
	else puts("NO");
	return 0;
}