#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int MAXN = 2100;

int N;
string S;
vector <int> edge[MAXN];
int nnode[MAXN];
int ddep[MAXN];
int dmin[MAXN];
int ans;

void flood (int cloc, int last)
{
    int ntot = 0;
    int nbest = 0;
    int nmin = 0;
    nnode[cloc] = S[cloc] - '0';
    ddep[cloc] = 0;
    for (int neigh : edge[cloc])
    {
        if (neigh == last) continue;
        flood (neigh, cloc);

        nnode[cloc] += nnode[neigh];
        int nb = ddep[neigh] + nnode[neigh];
        ddep[cloc] += nb;
        ntot += nb;
        if (nb > nbest)
        {
            nbest = nb;
            nmin = dmin[neigh] + nnode[neigh];
        }
    }

    dmin[cloc] = max (0, nbest + nmin - ntot);
}

void solve_root (int x)
{
    flood (x, -1);
    if (dmin[x] == 0 && ddep[x] % 2 == 0)
    {
        //cout << x << " " << ddep[x] << "\n";
        ans = min (ans, ddep[x]);
    }
}

int main()
{
    ios_base::sync_with_stdio(0);

    cin >> N >> S;
    for (int i = 0; i < N - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        a--, b--;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }

    ans = 1e9;
    for (int i = 0; i < N; i++)
    {
        solve_root (i);
    }
    if (ans > 1e8)
        cout << "-1\n";
    else
        cout << ans / 2 << "\n";
}