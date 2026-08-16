#include<bits/stdc++.h>

#define ll long long
#define fornum(A,B,C) for(A=B;A<C;A++)
#define mp make_pair
#define pii pair<int,int>
#define pll pair<ll,ll>

using namespace std;

/////////////////////////////////////////////////////
#define nxtr (1ll<<53)
ll n;
char bs[255];
ll mk[11][11],kt[11];
ll ans,a,b;
ll i, j, k;



int main(){
    
    scanf("%lld", &n);
    //printf("a%lld", n);
    while(n){
        scanf("%s", bs);
        a = 1;
        b = 0;
        ans = 1;
        //printf("a");
        fornum(i,0,52){
            ans *= 2;
            a *= 2;
            ans += bs[i] == '1' ? 1 : 0;
            a += bs[i] == '1' ? 1 : 0;
        }
        i = 0;
        //printf("a");
        while(true){
            ll aa = nxtr - ans;
            //printf("%lld\n", aa);
            ll ai = (aa / a + (aa%a?1:0));
            if(ai+i<=n){
                ans += ai * a;
            }else{
                ans += (n-i) * a;
                break;
            }
            i += ai;
            b++;
            ans /= 2;
            a /= 2;
            if(a==0){
                break;
            }
        }
        //printf("%lld\n", b);
        fornum(i,0,12){
            printf("%lld", ((b >> (11ll - i)) & 1ll) ? 1ll : 0ll);
        }
        fornum(i,0,52){
            printf("%lld",((ans >> (51ll - i)) & 1ll) ? 1ll : 0ll);
        }

        printf("\n");
        scanf("%lld", &n);
    }
    return 0;
}
