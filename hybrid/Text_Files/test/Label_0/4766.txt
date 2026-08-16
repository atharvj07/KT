#define _USE_MATH_DEFINES
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <cfloat>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <vector>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> i_i;
typedef pair<ll, int> ll_i;
typedef pair<double, int> d_i;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> d_d;
struct edge { int u, v; ll w; };

ll MOD = 1000000007;
ll _MOD = 1000000009;
int INF = INT_MAX / 2;
double EPS = 1e-10;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

void add_edge(vector<vector<edge> >& G, int R, int C, int y, int x, int _y, int _x, int t) {
	edge e = {C * y + x, C * _y + _x, t};
	G[C * y + x].push_back(e);
}

vector<ll> dijkstra(int n, vector<vector<edge> >& G, int s) {
	vector<ll> d(n, LLONG_MAX); d[s] = 0;
	priority_queue<ll_i, vector<ll_i>, greater<ll_i> > q;
	q.push(ll_i(0, s));
	while (!q.empty()) {
		ll_i p = q.top(); q.pop();
		int u = p.second;
		if (p.first > d[u]) continue;
		for (int i = 0; i < G[u].size(); i++) {
			edge e = G[u][i];
			if (d[e.v] > d[u] + e.w) {
				d[e.v] = d[u] + e.w;
				q.push(ll_i(d[e.v], e.v));
			}
		}
	}
	return d;
}

int main() {
	int R, C; cin >> R >> C;
	vector<string> a(R);
	int s, t;
	for (int y = 0; y < R; y++) {
		cin >> a[y];
		for (int x = 0; x < C; x++) {
			if (a[y][x] == 'S') {
				a[y][x] = '.';
				s = C * y + x;
			}
			if (a[y][x] == 'G') {
				a[y][x] = '.';
				t = C * y + x;
			}
		}
	}
	vector<vector<edge> > G(R * C);
	for (int y = 0; y < R; y++)
		for (int x = 0; x < C; x++) {
			if (a[y][x] == '#') continue;
			for (int k = 0; k < 4; k++) {
				int _y = y + dy[k], _x = x + dx[k];
				if (_y >= 0 && _y < R && _x >= 0 && _x < C);
				else continue;
				char c = a[_y][_x];
				if (c == 'o') add_edge(G, R, C, y, x, _y, _x, 1);
				if (c == '.') add_edge(G, R, C, y, x, _y, _x, 2);
			}
			for (int k = 0; k < 4; k++) {
				int _y = y, _x = x;
				for (int i = 1; i <= 3; i++) {
					_y += dy[k]; _x += dx[k];
					if (_y >= 0 && _y < R && _x >= 0 && _x < C);
					else break;
					char c = a[_y][_x];
					if (c == '#') break;
					add_edge(G, R, C, y, x, _y, _x, 2 + i);
				}
			}
		}
	cout << dijkstra(R * C, G, s)[t] << endl;
}