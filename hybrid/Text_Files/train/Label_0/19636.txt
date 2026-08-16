#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#define min(a,b)    (((a) < (b)) ? (a) : (b))
#define max(a,b)    (((a) > (b)) ? (a) : (b))
#define abs(x)    ((x) < 0 ? -(x) : (x))
#define INF 0x3f3f3f3f
#define delta 0.85
#define eps 1e-3
#define PI 3.14159265358979323846
#define MAX_N 1005
using namespace std;
typedef pair<int, int> P;
const int dx[4] = {0, 0, -1, 1};
const int dy[4] = {-1, 1, 0, 0};
int W, H, N;
int X1[MAX_N], X2[MAX_N], Y1[MAX_N], Y2[MAX_N];
bool fld[MAX_N * 4][MAX_N * 4];
//坐标压缩
int compress(int *x1, int *x2, int w){
	vector<int> xs(N * 4 + 2);
	xs.push_back(0);
	xs.push_back(w);
	for(int i = 0; i < N; i++){
		for(int j = 0; j <= 1; j++){
			int tx1 = x1[i] - j, tx2 = x2[i] + j;
			if(tx1 >= 0 && tx1 <= w) xs.push_back(tx1);
			if(tx2 >= 0 && tx2 <= w) xs.push_back(tx2);
		}
	}
	sort(xs.begin(), xs.end());
	xs.erase(unique(xs.begin(), xs.end()), xs.end());
	for(int i = 0; i < N; i++){
		x1[i] = distance(xs.begin(), lower_bound(xs.begin(), xs.end(), x1[i]));
		x2[i] = distance(xs.begin(), lower_bound(xs.begin(), xs.end(), x2[i]));
	}
	return xs.size();
}

int main(){
	while(~scanf("%d%d", &W, &H) && W){
		scanf("%d", &N);
		for(int i = 0; i < N; i++) scanf("%d%d%d%d", X1 + i, Y1 + i, X2 + i, Y2 + i);
		W = compress(X1, X2, W);
		H = compress(Y1, Y2, H);
		memset(fld, 0, sizeof(fld));
		// 因为 x, y 是坐标值，而 fld 数组是离散的，填充时为了对应原图矩形，右上边界不填充
		--W, --H;
		for(int i = 0; i < N; i++){
			for(int x = X1[i]; x < X2[i]; x++){
				for(int y = Y1[i]; y < Y2[i]; y++){
					fld[x][y] = 1;
				}
			}
		}
		int res = 0;	
		for(int x = 0; x < W; x++){
			for(int y = 0; y < H; y++){
				if(fld[x][y]) continue;
				++res;
				fld[x][y] = 1;
				// Bfs
				queue<P> que;
				que.push(P(x, y));
				while(!que.empty()){
					P p = que.front(); que.pop();
					int x = p.first, y = p.second;
					for(int i = 0; i < 4; i++){
						int nx = x + dx[i], ny = y + dy[i];
						if(nx >= 0 && nx < W && ny >= 0 && ny < H && !fld[nx][ny]){
							fld[nx][ny] = 1;
							que.push(P(nx, ny));
						}
					}
				}
			}
		}
		printf("%d\n", res);
	}
	return 0;
}
