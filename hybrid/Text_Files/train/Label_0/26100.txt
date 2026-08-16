#include <bits/stdc++.h>
using namespace std;
const int MAXN = 305;

int N, M, ps[3*MAXN][3*MAXN], ps2[3*MAXN][3*MAXN];
char arr[MAXN][MAXN];
vector<pair<int, int>> utama[2*MAXN], lain[2*MAXN];

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == '#') {
				utama[i+j].push_back({i, j});
				lain[i-j+MAXN].push_back({i, j});
			}
		}
	}
	
	for (int i = -N; i < 2*N; i++) {
		for (int j = -M; j < 2*M; j++) {
			ps[i+MAXN][j+MAXN] = ps[i-1+MAXN][j+1+MAXN];
			ps2[i+MAXN][j+MAXN] = ps2[i-1+MAXN][j-1+MAXN];
			if (0 <= i && i < N && 0 <= j && j < M && arr[i][j] == '#') {
				ps[i+MAXN][j+MAXN]++;
				ps2[i+MAXN][j+MAXN]++;
			}
			//~ cerr << ps[i+MAXN][j+MAXN] << " ";
		}
		//~ cerr << "\n";
	}
	
	int ans = 0;
	for (int miring = 0; miring < N+M; miring++) {
		for (int i = 0; i < (int)utama[miring].size(); i++) {
			for (int j = i+1; j < (int)utama[miring].size(); j++) {
				auto p = utama[miring][i], q = utama[miring][j];
				int x = p.second-q.second + q.first-p.first;
				assert(x > 0);
				//~ cerr << ps[miring+x-p.second+MAXN][p.second+MAXN] << " " << ps[q.first-1+MAXN][miring+x-(q.first-1)+MAXN] << "ex\n";
				ans += ps[p.first+MAXN][miring-x-p.first+MAXN] - ps[miring-x-(q.second+1)+MAXN][q.second+1+MAXN];
				ans += ps[miring+x-p.second+MAXN][p.second+MAXN] - ps[q.first-1+MAXN][miring+x-(q.first-1)+MAXN];
			}
		}
	}
	
	for (int miring = -M; miring < N; miring++) {
		for (int i = 0; i < (int)lain[miring+MAXN].size(); i++) {
			for (int j = i+1; j < (int)lain[miring+MAXN].size(); j++) {
				auto p = lain[miring+MAXN][i], q = lain[miring+MAXN][j];
				int x = q.first-p.first + q.second-p.second;
				//~ if (x <= 0) cerr << x << " ex\n";
				assert(x > 0);
				//~ cout << ps2[p.first-1+MAXN][-miring+x-(p.first-1)+MAXN] << "\n";
				ans += ps2[miring+x+p.second-1+MAXN][p.second-1+MAXN] - ps2[q.first+MAXN][-miring-x+q.first+MAXN];
				//~ cerr << ans << " ans\n";
				ans += ps2[p.first-1+MAXN][-miring+x+(p.first-1)+MAXN] - ps2[miring-x+q.second+MAXN][q.second+MAXN];
			}
		}
	}
	
	//~ int ans2 = 0;
	//~ for (int i = 0; i < N*M; i++) {
		//~ for (int j = i+1; j < N*M; j++) {
			//~ for (int k = j+1; k < N*M; k++) {
				//~ if (arr[i/M][i%M] == '#' && arr[j/M][j%M] == '#' && arr[k/M][k%M] == '#'
					//~ && abs(i/M-j/M) + abs(i%M - j%M) == abs(i/M-k/M) + abs(i%M - k%M)
					//~ && abs(i/M-k/M) + abs(i%M - k%M) == abs(j/M - k/M) + abs(j%M - k%M)) ans2++;
			//~ }
		//~ }
	//~ }
	//~ cout << ans2 << "\n";
	//~ assert(ans2 == ans);
	
	cout << ans << "\n";
	
	return 0;
}
