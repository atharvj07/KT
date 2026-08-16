#include "iostream"
#include "random"
#include "string"
#include "bitset"
#include "algorithm"
#include "map"
#include "queue"
#include "list"
#include "set"
#include "climits"
#include "iomanip"
#include "stack"
#include "functional"

using namespace std;
using ll = long long int;
using PII = pair<ll, ll>;

struct Edge {
	int to, cost;
	Edge(int a, int b) {
		to = a;
		cost = b;
		return;
	}
};

struct Node {
	int num, cost, day;
	bool operator<(const Node&n)const {
		return make_pair(cost, day) < make_pair(n.cost, n.day);
	}
	bool operator>(const Node&n)const {
		return make_pair(cost, day)>make_pair(n.cost, n.day);
	}
	Node(int a, int b, int c) {
		num = a, cost = b, day = c;
		return;
	}
};

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int N, M;
	cin >> N >> M;
	vector<long long int>num(N);
	for (auto &i : num)cin >> i;
	vector<vector<Edge>>edge(N);
	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		a--;
		b--;
		edge[a].push_back(Edge(b, c));
		edge[b].push_back(Edge(a, c));
	}
	vector<pair<int, int>>dist(N, { 1000000000,1000000000 });
	dist[0] = make_pair( 0,0 );
	priority_queue<Node, vector<Node>, greater<Node>>PQ;
	PQ.push(Node(0, 0, 0));
	while (!PQ.empty()) {
		int cn = PQ.top().num;
		int c = PQ.top().cost;
		int cd = PQ.top().day;
		PQ.pop();
		for (auto i : edge[cn]) {
			if (dist[i.to] > make_pair(c + i.cost, cd + 1)) {
				dist[i.to] = make_pair(c + i.cost, cd + 1);
				PQ.push(Node(i.to, dist[i.to].first, dist[i.to].second));
			}
		}
	}
	int K;
	cin >> K;
	vector<vector<int>>tapi(N, vector<int>(20, -1));
	for (int i = 1; i < N; i++) {
		int nx = -1;
		for (auto j : edge[i]) {
			if (dist[j.to].first + j.cost == dist[i].first&&dist[j.to].second + 1 == dist[i].second) {
				if (nx == -1)nx = j.to;
				else if (num[nx] > num[j.to])nx = j.to;
			}
		}
		if (nx != -1) {
			tapi[i][0] = nx;
		}
	}
	for (int j = 1; j < 20; j++) {
		for (int i = 0; i < N; i++) {
			if (tapi[i][j - 1] == -1)continue;
			tapi[i][j] = tapi[tapi[i][j - 1]][j - 1];
		}
	}
	while (K--) {
		int a, b, c;
		cin >> a >> b >> c;
		a--;
		int step = max(0, dist[a].second - b);
		int ans = dist[a].first;
		int node = a;
		for (int i = 0; i < 20; i++) {
			if ((step >> i) & 1) {
				node = tapi[node][i];
			}
		}
		ans -= dist[node].first;
		ans += max(0, dist[node].first - c);
		cout << ans << endl;
	}
}
