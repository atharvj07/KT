#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#define N_ 101000
#define sz(x) ((int)x.size())
using namespace std;
int n, m;
struct point {
	long long x, y;
	point operator -(const point &p)const {
		return { x - p.x,y - p.y };
	}
	bool isPos() const{
		return (x > 0) || (x == 0 && y > 0);
	}
}w[N_], P[N_];
struct Order {
	point p;
	int num;
	bool operator<(const Order &q)const {
		if (p.isPos() != q.p.isPos())return p.isPos();
		return p.y*q.p.x < q.p.y*p.x;
	}
};
struct Edge {
	int b, e;
}Ed[2*N_];
vector<int>F[N_];
long long curX;
struct Frac {
	long long A, B; // A/B
	Frac() {}
	Frac(long long A_, long long B_) {
		A = A_, B = B_;
	}
	bool operator<(const Frac &p)const {
		if ((A < 0) != (p.A < 0))return A < 0;
		if (A < 0) return Frac(-p.A, p.B) < Frac(-A, B);
		if (A / B != p.A / p.B)return A / B < p.A / p.B;
		long long r1 = A%B, r2 = p.A%p.B;
		return r1 * p.B < r2 * B;
	}
};
struct Seg {
	point b, e;
	int num;
	Frac curY() const{
		return { b.y*(e.x - b.x) + (curX - b.x)*(e.y - b.y), e.x - b.x };
	}
	bool operator <(const Seg &p)const {
		Frac y1 = curY(), y2 = p.curY();
		if (y1 < y2) return true;
		if (y2 < y1)return false;
		bool ck = (e.y - b.y) * (p.e.x - p.b.x) >(p.e.y - p.b.y) * (e.x - b.x);
		if (b.x == curX) return !ck;
		return ck;
	}
};
set<Seg>Set;
int Num[2*N_], v[2*N_], cnt, XC, K, Outer[2*N_], AA[N_];
long long X[2*N_];
vector<int>In[2*N_], Out[2*N_], Put[2*N_];
void Go(int a) {
	if (v[a])return;
	v[a] = cnt;
	Go(F[Ed[a].e][(Num[a ^ 1] + 1) % sz(F[Ed[a].e])]);
}
int GetX(long long x) {
	return lower_bound(X + 1, X + XC + 1, x) - X;
}

int Get(point a) {
	if (Set.empty())return 0;
	point b = { a.x - 1,a.y };
	auto it = Set.lower_bound({ b, a, 0 });
	if (it == Set.end())return 0;
	return !Outer[v[it->num]];
}

int vv[N_], cc, vis[N_];
void Add(Seg tp) {
	int a = tp.num;
	int com = vv[Ed[a].b];
	if (vis[com] == 2)return;
	if (!vis[com]) {
		vis[com] = 1;
		auto it = Set.lower_bound(tp);
		if (it != Set.end() && !Outer[v[it->num]]) {
			vis[com] = 2;
			return;
		}
	}
	Set.insert(tp);
}
void Del(int a) {
	auto it = Set.find({ w[Ed[a].b],w[Ed[a].e],a });
	if (it == Set.end() || it->num != a)return;
	Set.erase(it);
}
vector<int>E[N_];
vector<int>TP;
void DFS(int a) {
	int i;
	TP.push_back(a);
	vv[a] = cc;
	for (i = 0; i < E[a].size(); i++)if (!vv[E[a][i]])DFS(E[a][i]);
}
int main() {
	int i, a, b, j;
	scanf("%d%d%d", &n, &m,&K);
	for (i = 1; i <= n; i++) {
		scanf("%lld%lld", &w[i].x, &w[i].y);
		X[++XC] = w[i].x;
	}
	for (i = 0; i < m; i++) {
		scanf("%d%d", &a, &b);
		E[a].push_back(b);
		E[b].push_back(a);
		Ed[i * 2] = { a,b };
		F[a].push_back(i * 2);
		Ed[i * 2 + 1] = { b,a };
		F[b].push_back(i * 2 + 1);
	}
	for (i = 1; i <= n; i++) {
		if (F[i].empty())continue;
		vector<Order>ord;
		for (j = 0; j < sz(F[i]); j++) {
			int num = F[i][j];
			ord.push_back({ w[Ed[num].e] - w[i], num });
		}
		sort(ord.begin(), ord.end());
		F[i].clear();
		for (j = 0; j < sz(ord); j++) {
			Num[ord[j].num] = sz(F[i]);
			F[i].push_back(ord[j].num);
		}
	}
	for (i = 0; i < 2 * m; i++) {
		if (!v[i]) {
			cnt++;
			Go(i);
		}
	}
	for (i = 1; i <= n; i++) {
		if (!vv[i]) {
			TP.clear();
			cc++;
			DFS(i);
			int Mn = TP[0];
			for (j = 1; j < TP.size(); j++) {
				if ((w[Mn] - w[TP[j]]).isPos())Mn = TP[j];
			}
			if (!F[Mn].empty())Outer[v[F[Mn][0]]] = 1;
		}
	}
	for (i = 1; i <= K; i++) {
		scanf("%lld%lld", &P[i].x, &P[i].y);
		X[++XC] = P[i].x;
	}
	sort(X + 1, X + XC + 1);
	for (i = 0; i < 2*m; i++) {
		point p1 = w[Ed[i].b], p2 = w[Ed[i].e];
		if (p1.x < p2.x) {
			In[GetX(p1.x)].push_back(i);
			Out[GetX(p2.x)].push_back(i);
		}
	}
	for (i = 1; i <= K; i++) Put[GetX(P[i].x)].push_back(i);

	for (i = 1; i <= XC; i++) {
		curX = X[i];
		for (j = 0; j < sz(Put[i]); j++) {
			AA[Put[i][j]] = Get(P[Put[i][j]]);
		}
		for (j = 0; j < sz(Out[i]); j++) Del(Out[i][j]);
		vector<Seg> V;
		for (auto &j : In[i])  V.push_back({ w[Ed[j].b], w[Ed[j].e], j });
		if (V.empty())continue;
		sort(V.begin(), V.end());
		for (j = V.size() - 1; j >= 0;j--) Add(V[j]);
	}
	for (i = 1; i <= K; i++) {
		printf(AA[i] ? "Yes\n" : "No\n");
	}
}
