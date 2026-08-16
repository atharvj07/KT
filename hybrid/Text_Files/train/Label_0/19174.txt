#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
const int maxn=1e6+10;
const int mod=1000003;
ll sum[mod];
ll ni[mod];
ll pows(ll a,ll b)
{
    ll re=1;
    while(b)
    {
        if(b&1)
            re=a*re%mod;
         a=a*a%mod;
         b/=2;
    }
    return re;
}
int main()
{
      int q,x,d,n;
      scanf("%d",&q);
       sum[0]=ni[0]=1;
       for(ll  i=1;i<mod;i++)
       {
           sum[i]=sum[i-1]*i%mod;
           ni[i]=pows(sum[i],mod-2);
       }
       while(q--)
       {
       scanf("%d%d%d",&x,&d,&n);
        if(d==0)
            printf("%lld\n",pows(x,n)%mod);
        else
        {
                 ll xx=x*pows(d,mod-2)%mod;
                if(xx+n-1>=mod) printf("0\n");
                else
                printf("%lld\n",(sum[xx+n-1]*ni[xx-1]%mod*(pows(d,n))%mod)%mod);

        }

       }

    return 0;
}

