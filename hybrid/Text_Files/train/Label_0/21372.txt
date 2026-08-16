#include <iostream>
#include <queue>
#include <vector>
#include <map>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

const int INF = 1e+9 * 2;
typedef pair<int, int> P;

struct edge {
	int to, c;
	edge(int _to, int _c) : to(_to), c(_c){} 
};

int N, M, d[3001];
vector<edge> G[3001];

int main() {
	int k, shop, a, b, l;
	cin >> N >> M >> k;
	for(int i = 0; i < M; ++i){
		scanf("%d %d %d", &a, &b, &l);
		G[a].push_back(edge(b, l));
		G[b].push_back(edge(a, l));
	}
	
	priority_queue<P, vector<P>, greater<P> > que;
	fill(d, d + N + 1, INF);
	for(int i = 0; i < k; ++i){
		scanf("%d", &shop);
		d[shop] = 0;
		que.push(P(0, shop));
	}
	while(!que.empty()){
		P p = que.top();
		que.pop();
		int v = p.second;
		if(d[v] < p.first)
			continue;
		for(int i = 0; i < G[v].size(); ++i){
			edge e = G[v][i];
			if(d[e.to] > d[v] + e.c){
				d[e.to] = d[v] + e.c;
				que.push(P(d[e.to], e.to));
			}
		}
	}
	double ans = 0;
	
	for(int i = 1; i <= N; ++i){
		for(int j = 0; j < G[i].size(); ++j){
			ans = max(ans, (G[i][j].c + d[i] + d[G[i][j].to]) / 2.0);
		}
	}
	cout << round(ans) << endl;
	return 0;
}