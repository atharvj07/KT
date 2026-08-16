#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <queue>
using namespace std;
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
const int maxn = 30000 + 100;
const double eps = 1e-8;
typedef long long lint;

int sgn(double x) {
    return (x > eps) - (x < -eps);
}
struct P {
    double x, y;
    P() {}
    P(double _x, double _y): x(_x), y(_y) {}
    lint cross(const P &a, const P &b) const {
        return (a.x - x) * (b.y - y) - (a.y - y) * (b.x - x);
    }
    void input() {
        scanf("%lf%lf", &x, &y);
    }
};

int n, m, w, h, s;
int l[maxn], r[maxn];
double area[maxn];
int cnt[maxn];

int main() {
    while (scanf("%d%d%d%d%d", &n, &m, &w, &h, &s) == 5 && (n || m || w || h || s)) {
        for (int i = 1; i <= m; ++i) {
            scanf("%d%d", &l[i], &r[i]);
        }
        l[0] = r[0] = 0;
        l[m + 1] = r[m + 1] = h;
        
        for (int i = 0; i <= m; ++i) {
            area[i] = double(r[i + 1] - r[i] + l[i + 1] - l[i]) * w / 2;
            cnt[i] = 0;
        }
        for (int i = 0; i < n; ++i) {
            P pt;
            pt.input();
            int low = 0, high = m, res = -1;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (sgn(P(0, l[mid]).cross(P(w, r[mid]), pt)) > 0) {
                    res = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            if (res == -1) while (1);
            if (res != -1) ++cnt[res];
        }
        //for (int i = 0; i <= m; ++i) printf("%lf ", area[i]); printf("\n");
        //for (int i = 0; i <= m; ++i) {
            //if (i == 0) sum[i] = cnt[i];
            //else sum[i] = sum[i - 1] + cnt[i];
        //}
        int ba = 0;
        double now = 0;
        int ct = 0;
        int ans = 0;
        for (int i = 0; i <= m; ++i) {
            now += area[i];
            ct += cnt[i];
            while (ba <= i && sgn(now - w * h + s) > 0) {
                now -= area[ba];
                ct -= cnt[ba];
                ++ba;
            }
            ans = max(ans, ct);
        }
        printf("%d\n", n - ans);
    }
    return 0;
}