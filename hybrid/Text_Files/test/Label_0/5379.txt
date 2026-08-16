#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

const int INF = 1000000000;

typedef vector< vector<int> > graph;

graph g;
vector<int> match;
vector<bool> visit;

bool search(int u){
	if(u<0) return true;
	for(int i=0;i<g[u].size();i++){
		int next = g[u][i];
		if(visit[next]) continue;
		visit[next] = true;
		if(search(match[next])){
			match[u] = next, match[next] = u;
			return true;
		}
	}
	return false;
}

// L : ¶¤Ìm[hCR : E¤Ìm[h
int maximumMatch(int L, int R){
	int res = 0;
	match.assign(L+R, -1);
	for(int i=0;i<L;i++){
		visit.assign(L+R, false);
		res += search(i);
	}
	return res;
}

int main(){
	int N, M, L;
	static int dist[100][100];
	while(cin >> N >> M >> L, N){
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				dist[i][j] = (i==j ? 0 : INF);
		for(int i=0;i<M;i++){
			int a, b, c; cin >> a >> b >> c;
			dist[a][b] = dist[b][a] = min(dist[a][b], c);
		}
		for(int k=0;k<N;k++)
			for(int i=0;i<N;i++)
				for(int j=0;j<N;j++)
					dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]);
		g.assign(2*L, vector<int>());
		vector< pair<int, int> > vp(L);
		for(int i=0;i<L;i++)
			cin >> vp[i].second >> vp[i].first;
		sort(vp.begin(), vp.end());
		for(int i=0;i<L;i++){
			for(int j=i+1;j<L;j++){
				if(vp[i].first + dist[vp[i].second][vp[j].second] <= vp[j].first){
					g[i].push_back(L+j);
					g[L+j].push_back(i);
				}
			}
		}
		cout << L - maximumMatch(L, L) << endl;
	}
}