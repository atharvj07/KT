#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <iomanip>

using namespace std;

const int N = 111;
const double eps = 1e-10;
int n, m, pos[N];
double v[N][N], val[N], dist[N][N];

double get_r(int i, int j)
{
    double up = 0.0;
    double down = 0.0;
    for (int k = 1; k <= n; ++k) {
        up += v[j][k] * v[i][k];
        down += v[j][k] * v[j][k];
    }
    if (fabs(down) < eps) return 0;
    return up / down;
}

bool cmp(const int &x, const int &y) {
    return y < x;
}

namespace Chuliu{
    int n, used[N], pass[N], eg[N], more, que[N];
    double g[N][N];
    void combine(int id, double &sum) {
        int tot = 0, from, i, j, k;
        for ( ; id != 0 && !pass[id]; id = eg[id])
            que[tot++] = id, pass[id] = 1;
        for (from = 0; from < tot && que[from] != id; from++);
        if (from == tot) return;
		
        more = 1;
        for (i = from; i < tot; i++) {
            sum += g[eg[que[i]]][que[i]];
            if (i == from) continue;
            for (j = used[que[i]] = 1; j <= n; j++)
                if (!used[j])
                    if (g[que[i]][j] < g[id][j])
                        g[id][j] = g[que[i]][j];
        }
        for (i = 1; i <= n; i++)
            if (!used[i] && i != id) {
                for (j = from; j < tot; j++) {
                    k = que[j];
                    if (g[i][id] > g[i][k] - g[eg[k]][k])
                        g[i][id] = g[i][k] - g[eg[k]][k];
                }
            }
    }
    void clear(int V) {
        n = V;
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
                g[i][j] = dist[i][j];
        for(int i = 1; i <= n; ++i)
            g[i][i] = 0x3f3f3f3f;
    }
    double solve(int root) {
        int i, j, k;
        double sum = 0.0;
        memset(used, 0, sizeof(int) * (n + 1));
        for (more = 1; more; ) {
            more = 0;
            memset(eg, 0, sizeof(int) * (n + 1));
            for (i = 1; i <= n; i++)
                if (!used[i] && i != root) {
                    for (j = 1, k = 0; j <= n; j++)
                        if (!used[j] && i != j)
                            if (k == 0 || g[j][i] < g[k][i]) k = j;
                    eg[i] = k;
                }
            memset(pass, 0, sizeof(int) * (n + 1));
            for (i = 1; i <= n; i++)
                if (!used[i] && !pass[i] && i != root)
                    combine(i, sum);
        }
        for (i = 1; i <= n; ++i)
            if (!used[i] && i != root)
                sum += g[eg[i]][i];
        return sum;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin >> n >> m;
    for (int i = 1; i <= m; ++i) {
        val[i] = 0.0;
        for (int j = 1; j <= n; ++j) {
            cin >> v[i][j];
            val[i] += v[i][j] * v[i][j];
        }
    }
	
    double INF = 0;
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= m; ++j) {
            dist[j][i] = 0.0;
            double r = get_r(i, j);
            for (int k = 1; k <= n; ++k)
                dist[j][i] += (v[i][k] - r * v[j][k]) * (v[i][k] - r * v[j][k]);
            INF += dist[j][i];
        }
    }
    INF += 100 * 200;
    for (int i = 1; i <= m; ++i)
        dist[i][m + 1] = dist[m + 1][i] = INF + val[i];
    Chuliu::clear(m + 1);
    double w = Chuliu::solve(m + 1);
    cout << setiosflags(ios::fixed) << setprecision(10) << w - INF << endl;
    return 0;
}