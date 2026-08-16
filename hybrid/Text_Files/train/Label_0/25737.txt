#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <cassert>
using namespace std;


struct BipartiteMatching {
	int V;
	vector<vector<bool> > G;
	vector<int> match;
	vector<bool> used;

	BipartiteMatching(int v) {
		V = v;
		G = vector<vector<bool> >(v, vector<bool>(v));
		match = vector<int>(v);
		used = vector<bool>(v);
	}

	void add_edge(int v, int u) {
		G[v][u] = G[u][v] = true;
	}

	bool dfs(int v) {
		used[v] = true;
		for(int i = 0; i < V; i++) {
			if(!G[v][i]) continue;
			int u = i, w = match[u];
			if(w < 0 || (!used[w] && dfs(w))) {
				match[v] = u;
				match[u] = v;
				return true;
			}
		}
		return false;
	}

	int calc() {
		int res = 0;
		fill(match.begin(), match.end(), -1);
		for(int v = 0; v < V; v++) {
			if(match[v] < 0) {
				fill(used.begin(), used.end(), false);
				if(dfs(v)) {
					res++;
				}
			}
		}
		return res;
	}
};

typedef pair<int, int> Pii;

int h, w;
string C[100];
int dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 };

bool exist(int i, int j) {
	if(0 <= i && i < h && 0 <= j && j < w) return C[i][j] == '#';
	return false;
}

struct line {
	int x1, y1, x2, y2;
};

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	while(cin >> h >> w, h) {
		for(int i = 0; i < h; i++) {
			cin >> C[i];
		}

		bool G[101][101][4] = { { 0 } };
		bool E[101][101] = { { 0 } };
		vector<Pii> p;
		for(int i = 0; i < h + 1; i++) {
			for(int j = 0; j < w + 1; j++) {
				G[i][j][0] = exist(i - 1, j) && exist(i, j);
				G[i][j][1] = exist(i, j - 1) && exist(i, j);
				G[i][j][2] = exist(i - 1, j - 1) && exist(i, j - 1);
				G[i][j][3] = exist(i - 1, j - 1) && exist(i - 1, j);
				if(exist(i, j) + exist(i - 1, j) + exist(i, j - 1) + exist(i - 1, j - 1) == 3) {
					E[i][j] = true;
					p.emplace_back(j, i);
				}
			}
		}


		vector<line> tate, yoko;
		for(int y = 0; y < h + 1; y++) {
			for(int x = 0; x < w + 1; x++) {
				if(!E[y][x]) continue;
				for(int k = 0; k < 2; k++) {
					int ny = y, nx = x;
					if(!G[ny][nx][k]) continue;
					do {
						ny += dy[k];
						nx += dx[k];
					} while(!E[ny][nx] && G[ny][nx][k]);
					if(E[ny][nx]) {
						if(k % 2 == 1) tate.push_back(line{ x, y, nx, ny });
						else yoko.push_back(line{ x, y, nx, ny });
					}
				}
			}
		}

		int N = tate.size(), M = yoko.size();
		BipartiteMatching bp(N + M);
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				line t = tate[i], y = yoko[j];
				if(t.y1 <= y.y1 && y.y1 <= t.y2 && y.x1 <= t.x1 && t.x1 <= y.x2) {
					bp.add_edge(i, N + j);
				}
			}
		}

		int match = bp.calc();
		cout << p.size() - (N + M - match) + 1 << endl;
	}
}