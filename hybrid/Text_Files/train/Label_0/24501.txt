#include <algorithm>
#include <cmath>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>
#define IOS ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef double db;
typedef __int128_t int128;
const int maxn = 1e2 + 10;
int n, m;
int x1[maxn], y11[maxn], x2[maxn], y2[maxn];
db width(int *x, int *y, int n, db x0)
{
    double lb = 1e8, ub = -1e8;
    for (int i = 0; i < n; i++)
    {
        double x1 = x[i], y1 = y[i], x2 = x[(i + 1) % n], y2 = y[(i + 1) % n];
        if ((x1 - x0) * (x2 - x0) <= 0 && x1 != x2)
        {
            double y0 = y1 + (y2 - y1) * (x0 - x1) / (x2 - x1);
            lb = min(lb, y0);
            ub = max(ub, y0);
        }
    }
    return max(0.0, ub - lb);
}
int main()
{
    IOS;
    while (cin >> m >> n)
    {
        if (m == 0 && n == 0)
            break;
        for (int i = 0; i < m; i++)
            cin >> x1[i] >> y11[i];
        for (int i = 0; i < n; i++)
            cin >> x2[i] >> y2[i];
        int min1 = *min_element(x1, x1 + m), max1 = *max_element(x1, x1 + m);
        int min2 = *min_element(x2, x2 + n), max2 = *max_element(x2, x2 + n);
        vector<int> v;
        for (int i = 0; i < m; i++)
            v.push_back(x1[i]);
        for (int i = 0; i < n; i++)
            v.push_back(x2[i]);
        sort(v.begin(), v.end());
        double ans = 0;
        for (int i = 0; i + 1 < v.size(); i++)
        {
            db a = v[i], b = v[i + 1], c = (a + b) / 2;
            if (min1 <= c && c <= max1 && min2 <= c && c <= max2)
            {
                double fa = width(x1, y11, m, a) * width(x2, y2, n, a);
                double fb = width(x1, y11, m, b) * width(x2, y2, n, b);
                double fc = width(x1, y11, m, c) * width(x2, y2, n, c);
                ans += (b - a) / 6 * (fa + 4 * fc + fb);
            }
        }
        cout << fixed << setprecision(12) << ans << endl;
    }

    return 0;
}

