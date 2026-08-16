#include <bits/stdc++.h>
using namespace std;
const int N = 1e3 + 2,M = 1e9 + 7;
int dp[N][N],n,a,b,c,d,fact[N] = {1},inv[N];
void add(int &a,int b){
    a+=b;
    if(a >= M)a-=M;
}
int power(int base,int to){
    int ret = 1;
    while(to){
        if(to&1)ret = ret*1LL*base%M;
        to>>=1;
        base = base*1LL*base%M;
    }
    return ret;
}
int main(){
    //freopen("readin.txt","r",stdin);
    for(int i = 1;i < N;i++)fact[i] = fact[i - 1]*1LL*i%M;
    for(int i = 0;i < N;i++)inv[i] = power(fact[i],M - 2);
    scanf("%d%d%d%d%d",&n,&a,&b,&c,&d);
    dp[a][0] = 1;
    for(int i = a;i <= b;i++)
        for(int j = 0;j <= n;j++){
            add(dp[i + 1][j],dp[i][j]);
            for(int k = c;k <= d;k++){
                if(j + i*k > n)break;
                int x = fact[n - j]*1LL*inv[n - j - i*k]%M;
                x = x*1LL*power(inv[i],k)%M;
                x = x*1LL*inv[k]%M;
                add(dp[i + 1][j + k*i],dp[i][j]*1LL*x%M);   
            }
        }
    printf("%d\n",dp[b + 1][n]);
}