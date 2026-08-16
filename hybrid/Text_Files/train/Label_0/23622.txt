#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define reps(i,f,n) for(int i=f; i<int(n); ++i)
#define rep(i,n) reps(i,0,n)

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

const int INF = 1001001001;
const double EPS = 1e-10;

struct Edge {
	int dst, cost;
	Edge(int d, int c) : dst(d), cost(c) {}
};

struct Data {
	int pos, stat, cost;
	Data(int p, int s, int c) : pos(p), stat(s), cost(c) {}
	bool operator< (const Data& d)const {
		return cost > d.cost;
	}
};

int main()
{
	int n, m;
	while(scanf("%d%d", &n, &m), n){
		vector<Edge> G[100];
		rep(i, m){
			int a, b, c;
			scanf("%d%d%d", &a, &b, &c);
			--a;
			--b;
			G[a].push_back(Edge(b, c));
			G[b].push_back(Edge(a, c));
		}
		
		priority_queue<Data> Q;
		Q.push(Data(0, 0, 0));
		bool visited[100][3] = {{false}};
		int ans;
		
		while(!Q.empty()){
			Data d = Q.top();
			Q.pop();
			if(visited[d.pos][d.stat])
				continue;
			visited[d.pos][d.stat] = true;
			if(d.pos == n-1 && d.stat != 1){
				ans = d.cost;
				break;
			}
			
			rep(i, G[d.pos].size()){
				Edge e = G[d.pos][i];
				if(d.stat != 1)
					Q.push(Data(e.dst, d.stat, d.cost+e.cost));
				if(d.stat < 2)
					Q.push(Data(e.dst, d.stat+1, d.cost));
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}