#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    ll t;
    cin >> t;
    for (ll i = 0; i < t; i++)
    {
        ll n, moves = 0;
        cin >> n;
        ll c0=0,c1=0,c2=0;
        ll inp;
        for (int j = 0; j < n; j++)
        {
            cin >> inp;
            if (inp % 3 == 0)
            {
                c0++;
            }
            if (inp % 3 == 1)
            {
                c1++;
            }
            if (inp % 3 == 2)
            {
                c2++;
            }
        }
        ll temp=n/3;
        while(c0!=temp||c1!=temp||c2!=temp)
        {
            if(c0>(n/3))
            {
                if(c1>c2)
                {
                    c0=c0-1;
                    c2=c2+1;
                    moves+=2;
                }
                else if(c2>=c1)
                {
                    c0=c0-1;
                    c1=c1+1;
                    moves++;
                }
            }
            if(c1>(n/3))
            {
                if(c0>=c2)
                {
                    c1=c1-1;
                    c2=c2+1;
                    moves+=1;
                }
                else if(c2>c0)
                {
                    c1=c1-1;
                    c0=c0+1;
                    moves+=2;
                }
            }
            if(c2>(n/3))
            {
                if(c1>=c0)
                {
                    c2=c2-1;
                    c0=c0+1;
                    moves++;
                }
                else if(c0>c1)
                {
                    c2=c2-1;
                    c1=c1+1;
                    moves+=2;
                }
            }
        }
        cout<<moves<<endl;
    }
    return 0;
}