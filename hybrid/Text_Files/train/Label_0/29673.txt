#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{

    int n;
    scanf("%d",&n);

    vector<ll> a(n+1);
    for (int i = 0; i < n+1; i++)
    {
        scanf("%lld",&a[i]);
    }
    ll sum = 0;
    for (int i = 0; i <= n; i++)
    {
        sum += a[i];
    }
    ll ans = 0, space = 1;
    for (ll i = 0; i <= n; i++, space *= 2, space = min(space, sum))
    {
        ans += min(sum, space);
        sum -= a[i];
        space -= a[i];
        if (space < 0)
        {
            printf("-1");
            return 0;
        }
    }

    printf("%lld\n",ans);
    return 0;
}

