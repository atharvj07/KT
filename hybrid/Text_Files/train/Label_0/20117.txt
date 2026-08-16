#include <bits/stdc++.h>
#define INF 1000000007
#define MP make_pair
#define FI first
#define SE second
#define PB push_back
#define VI vector<int>
const double EPS = 1e-9, PI = acos(-1.0);
using namespace std;
typedef long long LL;
typedef pair <int, int> P;
const int NUM = 100010;
int n, m, goal;
bool g[10][10];
double ans, num[10];
double dp[2][1 << 10][10];
void solve(double now[1 << 10][10], double nxt[1 << 10][10], int len)
{
    for(int i = 1; i <= goal; ++i)
		for(int j = 0; j < n; ++j)
			nxt[i][j] = 0.0;
    for(int i = 1; i < goal; ++i)
        for(int j = 0; j < n; ++j) if(i & (1 << j))
                for(int k = 0; k < n; ++k)
                    if(g[j][k])
                        nxt[i | (1 << k)][k] += num[j] * now[i][j];
	for(int i = 0; i < n; ++i) ans += nxt[goal][i] * len;
}
int main()
{
#ifdef ACM_TEST
    freopen("in.txt", "r", stdin);
#endif
    scanf("%d%d", &n, &m);
    for(int i = 0, u, v; i < m; ++i)
    {
        scanf("%d%d", &u, &v);
        --u, --v;
        g[u][v] = g[v][u] = true;
        num[u] += 1.0;
        num[v] += 1.0;
    }
    for(int i = 0; i < n; ++i) if(num[i]) num[i] = 1.0 / num[i];
    goal = (1 << n) - 1;
    dp[0][1][0] = 1.0;
    for(int i = 1, j = 0; i < 10000; ++i, j = !j) solve(dp[j], dp[!j], i);
    printf("%.6f", ans);
    return 0;
}