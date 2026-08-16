#define _CRT_SECURE_NO_WARNINGS
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef vector<long long> vl; typedef pair<long long,long long> pll; typedef vector<pair<long long,long long> > vpll;
typedef vector<string> vs; typedef long double ld;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

struct GetStrID {
	static const int MaxLen = 21;	//書き換えること！
	static const int Alphas = 26;	//書き換えること！
	typedef char Alpha;
	static const int EndAlpha = -1;

private:
	template<typename T>
	struct Trie {
		bool terminate;
		T val;
		Trie<T> *next[Alphas];

		Trie(): terminate(false) { memset(next, 0, sizeof(next)); }
		~Trie() { for(Alpha a = 0; a < Alphas; ++ a) delete next[a]; }

		void insert(Alpha *s, const T &v) {
			if(*s == EndAlpha) {
				terminate = true;
				val = v;
				return;
			}else {
				if(!next[*s])
					next[*s] = new Trie;
				return next[*s]->insert(s+1, v);
			}
		}
		bool find(Alpha *s, T &out_v) const {
			if(*s == EndAlpha) {
				if(terminate) {
					out_v = val;
					return true;
				}else return false;
			}
			return next[*s] && next[*s]->find(s+1, out_v);
		}
	};

public:
	GetStrID(const char *alphas): cnt(0) {
		assert(strlen(alphas) <= Alphas);
		memset(idx, -1, sizeof(idx));
		for(const char *p = alphas; *p; ++ p)
			idx[*p] = p - alphas;
	}
	char idx[128];
	Trie<int> trie;
	int cnt;

	void clear() { trie = Trie<int>(); cnt = 0; }
	int get(const char *x) {
		static char tmp[MaxLen+1];
		{	int i;
			for(i = 0; x[i]; i ++) tmp[i] = idx[x[i]];
			tmp[i] = EndAlpha;
		}
		int ret = -1;
		if(!trie.find(tmp, ret)) {
			ret = cnt ++;
			trie.insert(tmp, ret);
		}
		return ret;
	}
};

pair<int,int> detectCycle2(const vector<int> &f) {
	int n = f.size();
	vector<bool> ved(n);
	int power, lambda, tortoise, hare;
	outer:
	for(int s = 0;s < n;s++){
		if(!ved[s]){
			power = 1, lambda = 1;
			if(f[s] < 0)continue;
			tortoise = s;
			ved[s] = true;
			hare = f[s];
			while(tortoise != hare) {
				if(hare < 0)goto outer;
				ved[hare] = true;
				if(power == lambda) {
					tortoise = hare;
					power <<= 1;
					lambda = 0;
				}
				if(hare < 0)goto outer;
				hare = f[hare];
				lambda++;
			}
			if(lambda > 0){
				return mp(hare, lambda);
			}
		}
	}
	return mp(-1,-1);
}

typedef int Weight;
vector<int> buildMSA(const vector<vector<Weight> > &w, int root)
{
int n = w.size();
		
// critical graphをつくる
// root以外の全頂点に対し、そこに入る最小コスト辺を選ぶ
vi par(n, -1);
for(int i = 0;i < n;i++){
	if(i != root){
		Weight min = INF;
		int pi = -1;
		for(int j = 0;j < n;j++){
			if(j != i){
				if(min > w[j][i]){
					min = w[j][i];
					pi = j;
				}
			}
		}
		par[i] = pi;
	}
}
		
pii res = detectCycle2(par);
if(res.first != -1){
	// cycleが存在したら縮約
	vi map(n, -1);
	int shed = n-res.second;
	map[res.first] = shed;
			
	// cycleの要素を列挙
	Weight minc = w[par[res.first]][res.first];
	for(int k = par[res.first];k != res.first;k = par[k]){
		map[k] = shed;
		minc = min(minc, w[par[k]][k]);
	}
			
	// 縮約後のグラフとの対応
	vector<int> imap(n-res.second);
	int p = 0;
	for(int i = 0;i < n;i++){
		if(map[i] != shed){
			map[i] = p;
			imap[p] = i;
			p++;
		}
	}
			
	// 縮約後のグラフ
	vector<vector<Weight> > sw(shed+1, vector<Weight>(shed+1, INF));
			
	vi to(n); // cycle内の要素xで、辺i->xの最小weightを実現するもの
	vi from(n); // cycle内の要素xで、辺x->iの最小weightを実現するもの
	for(int i = 0;i < n;i++){
		if(map[i] != shed){
			for(int j = 0;j < n;j++){
				if(map[j] == shed){
					// 非cycle->cycle
					// weightを修正
					Weight V = w[i][j] - w[par[j]][j] + minc;
					if(sw[map[i]][shed] > V){
						sw[map[i]][shed] = V;
						to[i] = j;
					}
				}else{
					// 非cycle->非cycle
					sw[map[i]][map[j]] = w[i][j];
				}
			}
		}else{
			for(int j = 0;j < n;j++){
				if(map[j] != shed){
					// cycle->非cycle
					Weight V = w[i][j];
					if(sw[shed][map[j]] > V){
						sw[shed][map[j]] = V;
						from[j] = i;
					}
				}
			}
		}
	}
			
	vi smsa = buildMSA(sw, map[root]); // 再帰してMSAを求める。
	// cycle以外の頂点について、imap,fromに従って対応を戻す。
	for(int i = 0;i < shed;i++){
		if(smsa[i] == shed){
			par[imap[i]] = from[imap[i]]; // cycle->非cycle
		}else if(smsa[i] != -1){
			par[imap[i]] = imap[smsa[i]]; // 非cycle->非cycle
		}
	}
			
	// cycle内の頂点について、toに従って対応を戻す。
	int u = imap[smsa[shed]];
	par[to[u]] = u;
}
return par;
}

int n;
char name1[21], name2[21];
char names[26][21];
int ms[26];
int g[26][100][100];
int ginter[26][100][100];
int h[26][26];
int hg[26][26];
bool vis[26];
vector<pair<pii,pii> > anss;

int dfs(int c) {
	if(vis[c]) return 0;
	vis[c] = true;
	int r = 1;
	rep(d, n) if(h[c][d] < INF)
		r += dfs(d);
	return r;
}

void buildPath_g(int c, int s, int t) {
	int u = ginter[c][s][t];
	if(u == -1) {
		if(s != t) anss.push_back(mp(mp(c, c), mp(s, t)));
	}else buildPath_g(c, s, u), buildPath_g(c, u, t);
}

int main() {
	GetStrID country("abcdefghijklmnopqrstuvwxyz");
	scanf("%d", &n);
	rep(i, n) {
		scanf("%s%d", names[i], &ms[i]);
		country.get(names[i]);
	}
	int e;
	scanf("%d", &e);
	mset(g, INF);
	rep(c, n) rep(i, ms[c]) g[c][i][i] = 0;
	vector<pair<pii,pii> > edges;
	rep(i, e) {
		int v1, v2, cost;
		scanf("%s%d%s%d%d", name1, &v1, name2, &v2, &cost);
		int c1 = country.get(name1), c2 = country.get(name2);
		if(c1 == c2) {
			amin(g[c1][v1][v2], cost);
		}else {
			edges.pb(mp(mp(c1,c2),mp(v2,cost)));
		}
	}
	mset(ginter, -1);
	rep(c, n) {
		int m = ms[c];
		rep(k, m) rep(i, m) rep(j, m) {
			if(g[c][i][j] > g[c][i][k] + g[c][k][j]) {
				g[c][i][j] = g[c][i][k] + g[c][k][j];
				ginter[c][i][j] = k;
			}
		}
	}
	mset(h, INF);
	rep(c, n) h[c][c] = 0;
	each(i, edges) {
		int c1 = i->first.first, c2 = i->first.second;
		int v2 = i->second.first, cost = i->second.second;
		if(h[c1][c2] > cost + g[c2][v2][0]) {
			h[c1][c2] = cost + g[c2][v2][0];
			hg[c1][c2] = v2;
		}
	}
	vector<vi> hv(n, vi(n));
	rep(i, n) rep(j, n) hv[i][j] = h[i][j];
	int q;
	scanf("%d", &q);
	rep(ii, q) {
		int v;
		scanf("%s%d", name1, &v);
		int c = country.get(name1);
		bool ok = true;
		ok &= g[c][v][0] < INF;
		mset(vis, 0);
		ok &= dfs(c) == n;
		if(!ok) {
			puts("Impossible");
		}else {
			anss.clear();
			int cost = g[c][v][0];
			buildPath_g(c, v, 0);
			vi tree = buildMSA(hv, c);
			rep(i, n) if(i != c) {
				cost += hv[tree[i]][i];
				int v2 = hg[tree[i]][i];
				anss.push_back(mp(mp(tree[i], i), mp(0, v2)));
				buildPath_g(i, v2, 0);
			}
			printf("%d\n", cost);
//			sort(all(anss));
//			anss.erase(unique(all(anss)), anss.end());
			each(i, anss) {
				pii p = i->first, q = i->second;
				printf("%s %d %s %d\n",
					names[p.first], q.first,
					names[p.second], q.second);
			}
		}
		puts("-----");
	}
	return 0;
}
