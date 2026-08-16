#include "bits/stdc++.h"
#include<unordered_map>
#include<unordered_set>
#pragma warning(disable:4996)
using namespace std;
using ld = long double;
const ld eps = 1e-9;


////フォード - ファルカーソン法 O(Flow|E|)

typedef int Weight;

const Weight INF = 1e9;
const Weight ZERO = 0;
struct Edge {
	int src, dst;
	Weight weight;
	int rev;
	int id;
	Edge(int src_, int dst_, Weight weight_, const int rev_, const int id_) :
		src(src_), dst(dst_), weight(weight_), rev(rev_), id(id_) { }
	Edge(int src_, int dst_, Weight weight_, const int rev_) :
		src(src_), dst(dst_), weight(weight_), rev(rev_) { }
	Edge() :src(0), dst(0), weight(0) {
	}
};
bool operator < (const Edge &e, const Edge &f) {
	return e.weight != f.weight ? e.weight > f.weight : // !!INVERSE!!
	e.src != f.src ? e.src < f.src : e.dst < f.dst;
}
typedef vector<Edge> Edges;
typedef vector<Edges> Graph;

typedef vector<Weight> Array;
typedef vector<Array> Matrix;
void add_edge(Graph&g, int from, int to, int cap)
{
	g[from].push_back(Edge(from, to, cap, (int)g[to].size()));
	g[to].push_back(Edge(to, from, 0, (int)g[from].size() - 1));
}
//二つを繋ぐ線を完全に消す
void erase_edge(Graph&g, const  int from, const int to) {
	g[from].erase(remove_if(g[from].begin(), g[from].end(), [=](const Edge&e) {return e.dst == to; }), g[from].end());
	g[to].erase(remove_if(g[to].begin(), g[to].end(), [=](const Edge&e) {return e.dst == from; }), g[to].end());
}
int dfs(vector<int>&used, Graph&g, int now, int t, int f)
{
	if (now == t) {
		return f;
	}
	used[now] = true;
	for (int i = 0; i<g[now].size(); ++i) {
		Edge &e = g[now][i];
		if (!used[e.dst] && e.weight>0) {
			int d = dfs(used, g, e.dst, t, min(f, e.weight));
			if (d > 0) {
				e.weight -= d;
				g[e.dst][e.rev].weight += d;
				return d;
			}
		}
	}
	return 0;
}
Weight fold_falc(Graph g, const int start, const int goal) {
	Weight ans = 0;
	while (1) {
		vector<int>used(g.size());
		int flow = dfs(used, g, start, goal, INF);
		if (!flow)return ans;
		else ans += flow;
	}
}

int main() {
	int N,A,B;cin>>N>>A>>B;
	vector<vector<int>>sas(2);
	int ans=0;
	for (int i = 0; i < N; ++i) {
		int a, b;cin>>a>>b;
		int num=a-b;
		if ( abs(num)<=A || (B <= abs(num) && abs(num) <= 2 * A)) {
			ans++;
		}
		else {
			if(num>0)sas[0].push_back(num);
			else sas[1].push_back(-num);
		}
	}
	const int start=0;
	const int zero=1;
	const int one=zero+sas[0].size();
	const int goal=one+sas[1].size();
	Graph g(goal+1);

	for (int i = 0; i < sas[0].size(); ++i) {
		add_edge(g,start,zero+i,1);
	}
	for (int i = 0; i < sas[0].size(); ++i) {
		for (int j = 0; j < sas[1].size(); ++j) {
			int x=zero+i;
			int y=one+j;
			int num=sas[0][i]-sas[1][j];

			if ( abs(num)<=A || (B <= (abs(num)) && (abs(num)) <= 2 * A)) {
				add_edge(g,x,y,1);
			}
		}
	}
	for (int i = 0; i < sas[1].size(); ++i) {
		add_edge(g, one+i, goal, 1);
	}

	ans+=fold_falc(g,start,goal);
	cout<<ans<<endl;
	return 0;
}
