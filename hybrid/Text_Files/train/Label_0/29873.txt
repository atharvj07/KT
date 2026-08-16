#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>	// require sort next_permutation count __gcd reverse etc.
#include <cstdlib>	// require abs exit atof atoi 
#include <cstdio>		// require scanf printf
#include <functional>
#include <numeric>	// require accumulate
#include <cmath>		// require fabs
#include <climits>
#include <limits>
#include <cfloat>
#include <iomanip>	// require setw
#include <sstream>	// require stringstream 
#include <cstring>	// require memset
#include <cctype>		// require tolower, toupper
#include <fstream>	// require freopen
#include <ctime>		// require srand
#define rep(i,n) for(int i=0;i<(n);i++)
#define ALL(A) A.begin(), A.end()

using namespace std;

typedef long long ll;
typedef pair<int, int> P;


const int INF = 100000000;
const int MAX_N = 100;
const int MAX_M = 100;
const int dy[4] = {-1, 0, 1, 0 };
const int dx[4] = { 0, 1, 0,-1 };

char maze[MAX_N][MAX_M+1];
int N, M;
int sy, sx;
int cost[MAX_N][MAX_M];

int bfs (void ){
	rep (i, N ) rep (j, M ) cost[i][j] = INF;
	queue<P> que;
	que.push (P (sy, sx ) );
	cost[sy][sx] = 0;
	while (!que.empty() ){
		P cur = que.front(); que.pop();
		int cy = cur.first;
		int cx = cur.second;
		int cc = cost[cy][cx];
		rep (k, 4 ){
			int ny = cy + dy[k];
			int nx = cx + dx[k];
			if (ny < 0 || ny >= N || nx < 0 || nx >= M ) continue;
			int next_cost = cost[cy][cx] + ((maze[ny][nx] == '#' && maze[cy][cx] != '#') ? 1 : 0 );
			if (next_cost >= cost[ny][nx] ) continue;
			cost[ny][nx] = next_cost;
			que.push (P (ny, nx ) );
		} // end rep
	} // end rep

	int res = INF;
	rep (i, N ) res = min (res, cost[i][0] );
	rep (i, N ) res = min (res, cost[i][M-1] );
	rep (j, M ) res = min (res, cost[0][j] );
	rep (j, M ) res = min (res, cost[N-1][j] );

	return res;	
}

int main()
{
	ios_base::sync_with_stdio(0);
	while (cin >> M >> N, M ){
		memset (maze, 0, sizeof (maze ) );
		memset (cost, 0, sizeof (cost ) );
		rep (i, N ) rep (j, M ) cin >> maze[i][j];
		rep (i, N ) rep (j, M ) if (maze[i][j] == '&' ){ sy = i, sx = j; }
		int res = bfs ();
		cout << res << endl;
	} // end while
	
	return 0;
}