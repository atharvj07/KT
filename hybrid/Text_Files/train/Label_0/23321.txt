#include <cmath>
#include <queue>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

typedef pair<int, int> pii;

const int maxn = 105;
const int inf = 1e9;
const double eps = 1e-12;

int n, s, t, flag[maxn];

vector<pii> mp[maxn];
void add_edge(int u, int v, int d){
	mp[u].push_back(make_pair(v, d));
	mp[v].push_back(make_pair(u, d));
}

double eq[maxn][maxn];
double gauss(){
	
	for(int i = 1; i <= n; ++i){
		int tmp = i;
		for(int j = i; j <= n; ++j) if(fabs(eq[j][i]) > fabs(eq[tmp][i])) tmp = j;
		for(int j = i; j <= n; ++j) swap(eq[i][j], eq[tmp][j]); swap(eq[i][0], eq[tmp][0]);
		
		for(int j = i + 1; j <= n; ++j){
			double tt = eq[j][i] / eq[i][i];
			for(int k = i; k <= n; ++k) eq[j][k] -= eq[i][k] * tt;
			eq[j][0] -= eq[i][0] * tt;
		}
	}
	for(int i = n; i >= 1; --i){
		for(int j = i + 1; j <= n; ++j) eq[i][0] -= eq[i][j] * eq[j][0];
		eq[i][0] /= eq[i][i];
	}
	return eq[s][0];
}

queue<int> que;
int dist[maxn];
bool inq[maxn];
void spfa(){
	
	for(int i = 1; i <= n; ++i) dist[i] = inf;
	dist[t] = 0;
	que.push(t);
	while(!que.empty()){
		int u = que.front();
		inq[u] = false;
		que.pop();
		for(int l = 0; l < mp[u].size(); ++l){
			int v = mp[u][l].first;
			if(dist[v] <= dist[u] + mp[u][l].second) continue;
			dist[v] = dist[u] + mp[u][l].second;
			if(!inq[v]){
				inq[v] = true;
				que.push(v);
			}
		}
	}
}

void work(){
	
	for(int i = 1; i <= n; ++i) mp[i].clear();
	for(int i = 1; i <= n; ++i) for(int j = 0; j <= n; ++j) eq[i][j] = 0.00;
	for(int i = 1; i <= n; ++i) scanf("%d", &flag[i]);
	for(int i = 1; i <= n; ++i) for(int j = 1; j <= n; ++j){
		int d; scanf("%d", &d);
		if(i < j || d == 0) continue;
		add_edge(i, j, d);
	}
	spfa();
	if(dist[s] == inf){
		puts("impossible");
		return;
	}
	for(int u = 1; u <= n; ++u){
		if(u == t){
			eq[u][u] = 1.00;
			continue;
		}
		for(int l = 0; l < mp[u].size(); ++l){
			int v = mp[u][l].first;
			if(flag[u] && dist[u] != dist[v] + mp[u][l].second) continue;
			eq[u][v] += 1.00;
			eq[u][0] -= 1.00 * mp[u][l].second;
			eq[u][u] -= 1.00;
		}
	}
	printf("%.10f\n", gauss() + eps);
}

int main(){

	while(true){
		scanf("%d%d%d", &n, &s, &t);
		if(n + s + t == 0) break;
		work();
	}
	return 0;
}