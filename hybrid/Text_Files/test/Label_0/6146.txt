#include "iostream"
#include "climits"
#include "list"
#include "queue"
#include "stack"
#include "set"
#include "functional"
#include "algorithm"
#include "string"
#include "map"
#include "unordered_map"
#include "unordered_set"
#include "iomanip"
#include "cmath"
#include "random"
#include "bitset"
#include "cstdio"
#include "numeric"
#include "cassert"

using namespace std;

//const long long int MOD = 1000000007;
const int MOD = 1000000007;
//const int MOD = 998244353;
//const long long int MOD = 998244353;

//long long int N, M, K, H, W, L, R;
int N, M, K, H, W, L, R;

void Calculate_Depth(vector<vector<int>>&edge, vector<int>&depth, int stnode) {
	depth[stnode] = 0;
	queue<int>Q;
	Q.push(stnode);
	while (!Q.empty()) {
		int cn = Q.front();
		Q.pop();
		for (auto i : edge[cn]) {
			if (depth[i] > depth[cn] + 1) {
				depth[i] = depth[cn] + 1;
				Q.push(i);
			}
		}
	}
	return;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> N >> M >> L >> R;
	L--;
	R--;
	vector<vector<int>>edge(N);
	for (int i = 0; i < M; i++) {
		cin >> H >> W;
		H--;
		W--;
		edge[H].push_back(W);
		edge[W].push_back(H);
	}
	vector<int>depthL(N, MOD);
	vector<int>depthR(N, MOD);
	Calculate_Depth(edge, depthL, L);
	Calculate_Depth(edge, depthR, R);
	//cout << depthL[R] << endl;
	if (depthL[R] == 1) {
		cout << 0 << endl;
		return 0;
	}
	long long int ans = 0;
	vector<int>Lnum(N);
	vector<int>Rnum(N);
	for (auto i : depthL)if (i != MOD)Lnum[i]++;
	for (auto i : depthR)if (i != MOD)Rnum[i]++;
	for (int i = 0; i < depthL[R] - 1; i++) {
		ans += 1LL * Lnum[i] * Rnum[depthL[R] - i - 2];
		//cout << Lnum[i] << " " << Rnum[depthL[R] - i - 2] << endl;
		//cout << ans << endl;
	}
	cout << ans << endl;
}

