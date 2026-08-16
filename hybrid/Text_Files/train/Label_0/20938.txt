#include <bits/stdc++.h>
using namespace std;
template <class T>
inline bool chmax(T &a, T b)
{
    if (a < b)
    {
        a = b;
        return 1;
    }
    return 0;
}
template <class T>
inline bool chmin(T &a, T b)
{
    if (a > b)
    {
        a = b;
        return 1;
    }
    return 0;
}
typedef long long int ll;

#define EPS (1e-7)
#define INF (1e9)
#define LLINF (1e18)
#define PI (acos(-1))
#define MOD (1000000007)
#define ALL(v) (v).begin(), (v).end()
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

//-------------------------------------

using P = pair<int, int>;

int dist(P a, P b)
{
    return abs(a.first - b.first) + abs(a.second - b.second);
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    int h, w;
    cin >> h >> w;
    vector<string> grid(h);
    for (int i = 0; i < h; i++)
    {
        cin >> grid[i];
    }
    vector<P> rec;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (grid[i][j] == 'B')
            {
                rec.push_back(P(j, i));
            }
        }
    }
    int n = rec.size();
    int ans = 0;
    int x_mn = INF;
    int x_mx = -INF;
    int y_mn = INF;
    int y_mx = -INF;
    for (int i = 0; i < n; i++)
    {
        chmin(x_mn, rec[i].first);
        chmin(y_mn, rec[i].second);
        chmax(x_mx, rec[i].first);
        chmax(y_mx, rec[i].second);
    }
    vector<P> kouho;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (grid[i][j] == 'B')
            {
                if (i == y_mn || i == y_mx || j == x_mn || j == x_mx)
                {
                    kouho.push_back(P(j, i));
                }
            }
        }
    }
    int sz = kouho.size();
    for (int i = 0; i < sz; i++)
    {
        for (int j = i + 1; j < sz; j++)
        {
            chmax(ans, dist(kouho[i], kouho[j]));
        }
    }
    cout << ans << endl;
}
