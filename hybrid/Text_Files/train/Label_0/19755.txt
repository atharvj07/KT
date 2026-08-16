#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, l, a, b, d[100010], dt[100010][20];

int main()
{
    scanf("%d", &n);
    for(int i = 0 ; i < n ; i++ ) scanf("%d", d+i);
    scanf("%d%d", &l, &m);
    for(int i = 0 ; i < n ; i++ )
        dt[i][0] = (int)(upper_bound(d+i, d+n, d[i]+l) - d) - 1;
    for(int k = 1 ; k < 20 ; k++ ) for(int i = 0 ; i < n ; i++ )
        dt[i][k] = dt[dt[i][k-1]][k-1];
    while( m-- )
    {
        int ans = 1;
        scanf("%d%d", &a, &b), a--, b--;
        if( a < b ) swap(a, b);
        for(int i = 19 ; i >= 0 ; i-- )
            if( dt[b][i] < a ) b = dt[b][i], ans+=(1<<i);
        printf("%d\n", ans);
    }
    return 0;
}
