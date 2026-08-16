#include<bits/stdc++.h>
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define rep(i,a,b) for (int i=(a); i<(b); i++)
#define per(i,a,b) for (int i=(b-1); i>=(a); i--)
#define debug(x) cout << #x << " => " << x << endl
using namespace std;

#define fi first
#define se second
#define mp make_pair
typedef pair<int,int> pii;

#define eb emplace_back
#define pb push_back
typedef vector<int> vi;

typedef long long ll;
typedef long double ld;

const int MAX_N = 7 + 100000;
///----------------------------------------------
map<int, vector<pii> > v1,v2;
map<int, set<pii> > s1,s2;
int x[MAX_N], y[MAX_N], n,D;
bool vis[MAX_N];
///----
int solve(vector<pii> &hv, int lo, int hi) {
	auto itl = lower_bound(all(hv), mp(lo,-1));
	auto itr = lower_bound(all(hv), mp(hi+1,-1));
	return itr-itl;
}
void check(set<pii> &hv, int lo, int hi, queue<int> &que) {
	auto it = hv.lower_bound(mp(lo, -1));
	while (it != hv.end() && it->fi <= hi) {
		if (!vis[it->se]) que.push(it->se);
		vis[it->se] = true;
		it = hv.erase(it);
	}
}
///----
void bfs(int st) {
	queue<int> que;
	que.push(st); vis[st]=true;
	for (; !que.empty(); ) {
		int at = que.front(); que.pop();
		auto it = s1.find(x[at]+y[at]-D); if (it != s1.end()) check(it->se, x[at]-D, x[at], que);
			 it = s1.find(x[at]+y[at]+D); if (it != s1.end()) check(it->se, x[at], x[at]+D, que);
			 it = s2.find(x[at]-y[at]-D); if (it != s2.end()) check(it->se, x[at]-D+1, x[at]-1, que);
			 it = s2.find(x[at]-y[at]+D); if (it != s2.end()) check(it->se, x[at]+1, x[at]+D-1, que);
	}
}
///----
int main() {
	
	///read
	int a,b; scanf("%d%d%d",&n,&a,&b); a--; b--;
	rep(i,0,n) {
		scanf("%d%d",x+i,y+i);
		v1[x[i]+y[i]].eb(x[i],i);
		v2[x[i]-y[i]].eb(x[i],i);
		s1[x[i]+y[i]].emplace(x[i], i);
		s2[x[i]-y[i]].emplace(x[i], i);
	}

	///prework
	for (auto it = v1.begin(); it != v1.end(); it++) sort(all(it->se));
	for (auto it = v2.begin(); it != v2.end(); it++) sort(all(it->se));
	D = abs(x[a]-x[b])+abs(y[a]-y[b]);

	///work
	memset(vis,false,sizeof(vis));
	bfs(a); bfs(b);
	ll ans=0;
	rep(i,0,n) if (vis[i]) {
		auto it = v1.find(x[i]+y[i]-D); if (it != v1.end()) ans += solve(it->se, x[i]-D, x[i]);
			 it = v1.find(x[i]+y[i]+D); if (it != v1.end()) ans += solve(it->se, x[i], x[i]+D);
			 it = v2.find(x[i]-y[i]-D); if (it != v2.end()) ans += solve(it->se, x[i]-D+1, x[i]-1);
			 it = v2.find(x[i]-y[i]+D); if (it != v2.end()) ans += solve(it->se, x[i]+1, x[i]+D-1);
	}
	printf("%lld\n",ans/2);
	
	return 0;



}
