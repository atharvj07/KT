#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int dp[505][505];
/*
00300
02220
11111
*/
int main()
{
    int t;
    scanf("%d", &t);
    while(t--)
    {
        memset(dp, 0, sizeof(dp));
        int n, m;
        scanf("%d%d", &n, &m);
        for(int i = 0;i < n;i++)
        {
            for(int j = 0;j < m;j++)
            {
                char c;
                scanf(" %c", &c);
                if(c == '*') dp[i][j] = 1;
            }
        }

        for(int k = 1;k <= 500;k++)
        {
            for(int i = 0;i < n;i++)
            {
                for(int j = 0;j < m;j++)
                {
                    if(j == 0 || j == m - 1) continue;
                    if(dp[i][j] == 0) continue;
                    if(dp[i + 1][j - 1] == k && dp[i + 1][j] == k && dp[i + 1][j + 1] == k)
                    {
                        dp[i][j]++;
                    }
                }
            }
        }

        ll ans = 0;
        for(int i = 0;i < n;i++)
        {
            for(int j = 0;j < m;j++)
            {
                ans += dp[i][j];
                // printf("%d ", dp[i][j]);
            }
            // printf("\n");
        }

        printf("%lld\n", ans);
    }

    return 0;
}
