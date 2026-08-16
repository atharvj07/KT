#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int maxn = 1e5 + 5, mod = 1e9 + 7;
const double inf = 1e18;
struct e{
    int x, y;
    double nx, ny;
    char p;
}a[maxn];
int n;
double F(double mid)
{
    double maxx = -inf, minx = inf, maxy = -inf, miny = inf;
    for (int i = 0; i < n; ++i){
        a[i].nx = a[i].x, a[i].ny = a[i].y;
        if(a[i].p == 'L') a[i].nx = (double)a[i].x - mid;
        else if(a[i].p == 'R') a[i].nx = (double)a[i].x + mid;
        else if(a[i].p == 'U') a[i].ny = (double)a[i].y + mid;
        else a[i].ny = (double)a[i].y - mid;
        minx = min(minx, a[i].nx);
        maxx = max(maxx, a[i].nx);
        miny = min(miny, a[i].ny);
        maxy = max(maxy, a[i].ny);
    }
    return (maxx - minx) * (maxy - miny);
}
int main()
{
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; ++i){
        cin >> a[i].x >> a[i].y >> a[i].p;
    }
    double l = 0, r = 1e8;
    for (int i = 0; i < 100; ++i){
        double len = (r - l) / 3;
        double lmid = l + len, rmid = l + 2 * len;
        if (F(lmid) < F(rmid)) r = rmid;
        else l = lmid;
    }
    cout << fixed << F((l + r) / 2) << endl;
    return 0;
}
