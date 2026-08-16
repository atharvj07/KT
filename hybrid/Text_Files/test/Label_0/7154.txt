#include <bits/stdc++.h>

using namespace std;

#ifdef Adrian
#include "debug.h"
#else
#define debug(...) 9999
#endif

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef complex<int> point;
#define F first
#define S second
#define ii pair<int,int>



int main() {
#ifdef Adrian
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
#else
    ios_base::sync_with_stdio(0); cin.tie(0);
#endif


    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<vector<int>> g(n);
        for(int i=1; i<n; i++)
        {
            int x;
            cin>>x;
            --x;
            g[x].push_back(i);
            g[i].push_back(x);
        }
        vector<ll> a(n);
        for(int i=1; i<n; i++)
            cin>>a[i];

        vector<int> lvl(n, -1), par(n, -1);
        lvl[0] = 0;
        queue<int> q;
        q.push(0);
        while(!q.empty())
        {
            int c = q.front();
            q.pop();

            for(auto v:g[c])
                if(lvl[v] == -1)
                {
                    lvl[v] = lvl[c] + 1;
                    par[v] = c;
                    q.push(v);
                }
        }

        int d = *max_element(lvl.begin(), lvl.end()) + 1;

        vector<vector<int>> node(d);
        for(int i=0; i<n; i++)
            node[lvl[i]].push_back(i);

        auto cmp = [&](int i, int j) { return a[i] < a[j]; };
        for(auto &i:node) sort(i.begin(), i.end(), cmp);

        vector<vector<ll>> dp(2,
                vector<ll>(n));
        for(int i=d-1; i>=0; i--)
        {
            int sz = node[i].size();
            for(int j=0; j<sz; j++)
            {
                int c = node[i][j];
                dp[1][c] = 0;
                for(auto v:g[c])
                    if(v != par[c])
                        dp[1][c] = max(dp[1][c], dp[0][v]);
            }

            ll mx = -1e9;
            for(int j=0; j<sz; j++)
            {
                int c = node[i][j];
                if(j > 0)
                    dp[0][c] = max(dp[0][c], mx + a[c]);
                mx = max(mx, dp[1][c] - a[c]);
            }
            mx = -1e9;
            for(int j=sz - 1; j>=0; j--)
            {
                int c = node[i][j];
                if(j < n - 1)
                    dp[0][c] = max(dp[0][c], mx - a[c]);
                mx = max(mx, dp[1][c] + a[c]);
            }

            int l = node[i][0], r = node[i][sz - 1];
            for(int j=0; j<sz; j++)
            {
                int c = node[i][j];
                dp[0][c] = max(dp[0][c],
                        dp[1][c] + max(a[c] - a[l], a[r] - a[c]));
            }
        }

        cout<<dp[1][0]<<'\n';
    }

    return 0;
}
