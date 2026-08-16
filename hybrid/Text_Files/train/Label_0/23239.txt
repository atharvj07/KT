#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

int const N = 200000, md = 1e9 + 7;
vector<int> tr[N + 1];
pair<int, int> dp[N + 1];
int n, an[N + 1][2], pw2[N + 1], mxdp[N + 1], es[N + 1][3];

inline void ad(int &x, int y) { if ((x += y) >= md)x -= md; }

int pl(int v = 0, int l = 0, int r = 0){
	if (v && (int)tr[v].size() == 1)return pl(tr[v][0], l, r + 1);
	dp[v] = make_pair(l, r);
	mxdp[v] = r;
	f(i, 0, tr[v].size())tr[v][i] = pl(tr[v][i], r + 1, r + 1), mxdp[v] = max(mxdp[v], mxdp[tr[v][i]]);
	return v;
}

inline pair<int, int> rm(vector<pair<int, int> > &v){
	es[0][0] = 1;
	f(i, 0, v.size()){
		es[i + 1][0] = (ll)es[i][0] * v[i].first % md;
		es[i + 1][1] = (ll)es[i][0] * v[i].second % md;
		ad(es[i + 1][1], (ll)es[i][1] * v[i].first % md);
		es[i + 1][2] = (ll)es[i][1] * v[i].second % md;
		ad(es[i + 1][2], (ll)es[i][2] * (v[i].first + v[i].second) % md);
	}
	ad(es[v.size()][0], es[v.size()][2]);
	return make_pair(es[v.size()][0], es[v.size()][1]);
}

int D, sz;
void go(int v = 0){
	if (D >= dp[v].first && D <= dp[v].second) { an[v][0] = an[v][1] = 1; ++sz; return; }
	vector<pair<int, int> > x;
	f(i, 0, tr[v].size()){
		int u = tr[v][i];
		if (mxdp[u] < D)continue;
		go(u);
		x.push_back(make_pair(an[u][0], an[u][1]));
	}
	pair<int, int> t = rm(x);
	an[v][0] = t.first;
	an[v][1] = t.second;
}

int main(){
	scanf("%d", &n);
	pw2[0] = 1;
	f(i, 1, n + 1)if ((pw2[i] = pw2[i - 1] << 1) >= md)pw2[i] -= md;
	f(i, 1, n + 1){
		int t;
		scanf("%d", &t);
		tr[t].push_back(i);
	}
	pl();
	int a = 0;
	f(i, 0, mxdp[0] + 1){
		D = i;
		sz = 0;
		go();
		ad(a, (ll)an[0][1] * pw2[n + 1 - sz] % md);
	}
	printf("%d\n", a);
}