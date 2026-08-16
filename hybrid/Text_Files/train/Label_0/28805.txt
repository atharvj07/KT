#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for(ll (i) = (0);(i) < (n);++i)
#define REV(i,n) for(ll (i) = (n) - 1;(i) >= 0;--i)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SHOW1d(v,n) {REP(W,n)cerr << v[W] << ' ';cerr << endl << endl;}
#define SHOW2d(v,i,j) {REP(aaa,i){REP(bbb,j)cerr << v[aaa][bbb] << ' ';cerr << endl;}cerr << endl;}
#define ALL(v) v.begin(),v.end()
#define Decimal fixed<<setprecision(20)
#define INF 1000000000
#define LLINF 1000000000000000000LL
#define MOD 1000000007

typedef long long ll;
typedef pair<ll,ll> P;

struct UF
{
	vector<int> par; // 親のインデックスを記憶する配列
	vector<int> sz; // サイズを記憶する。
	vector<int> rank;
	// 初期化
	UF(int n):par(n),sz(n),rank(n){
		for(int i = 0; i < n; i++){
			par[i] = i;sz[i] = 1;rank[i] = 0;
		}
	}
	// 親を求める
	int find(int x) {
		if (par[x] == x) return x;
		else return par[x] = find(par[x]);
	}
	// xとyの属する集合を併合
	void unite(int x, int y) {
		x = find(x); y = find(y);
		if (x == y) return;
		if(rank[x] < rank[y]){
			par[x] = y;
			sz[y] += sz[x];
		}
		else{
			par[y] = x;
			sz[x] += sz[y];
			if(rank[x] == rank[y])rank[x]++;
		}
	}
	// xとyが同じ集合ならtrue
	bool same(int x, int y) { return find(x) == find(y); }
	// 素の集合のサイズを求める
	int size(int n){return sz[find(n)];}
};


int mp[111][111];
int redev[111];
int sum[111];
set<pair<int,int>> ans;

pair<int,int> add_ans(int a, int b){
	return MP(min(a,b), max(a,b));
}

int main(){

	int n,m;cin >> n >> m;
	REP(i,m){
		int a,b;cin >> a >> b;
		a--;b--;
		mp[a][b] = 1;
		mp[b][a] = 1;
	}
	REP(i,n)mp[i][i] = 2;

	while(1){
		vector<pair<int,pair<int,int>>> v;
		REP(i,n){
			int tmp = 0;
			int su = 0;
			REP(j,n){
				if(mp[i][j] == 0)tmp++;
				if(mp[i][j] != 2)su++;
			}
			redev[i] = tmp;
			sum[i] = su;
			v.PB(MP(tmp,MP(i,su)));;
		}

		sort(ALL(v));

		int now = -1;
		REP(i,n){
			if(v[i].SE.SE % 2){
				now = v[i].SE.FI;
				break;
			}
		}
		if(now == -1)break;
		bool flag = false;

		REP(i,n){
			if(mp[now][v[i].SE.FI] == 0 && (v[i].SE.SE % 2 == 1)){
				mp[now][v[i].SE.FI] = 2;
				mp[v[i].SE.FI][now] = 2;
				flag = true;
				break;
			}
		}
		if(flag)continue;

		REV(i,n){
			if(mp[now][v[i].SE.FI] == 0){
				mp[now][v[i].SE.FI] = 2;
				mp[v[i].SE.FI][now] = 2;
				flag = true;
				break;
			}
		}

		if(!flag){
			cout << -1 << endl;
			return 0;
		}
	}

	UF uf(n);
	REP(i,n){
		REP(j,n){
			if(mp[i][j] != 2)uf.unite(i,j);
		}
	}
	set<int> s;
	REP(i,n)s.insert(uf.find(i));
	if(s.size() > 1){
		cout << -1 << endl;
		return 0;
	}

	REP(i,n){
		REP(j,n){
			if(mp[i][j] == 0)ans.insert(add_ans(i,j));
		}
	}

	cout << ans.size() << endl;
	for(auto it = ans.begin();it != ans.end();it++){
		cout << it->FI + 1 << " " << it->SE + 1 << endl;
	}

	return 0;
}

