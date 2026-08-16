#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
long long Mod, F[1010], InvF[1010];
long long Pow(long long a, long long b){
    long long r=1;
    while(b){
        if(b&1)r=r*a%Mod;
        a=a*a%Mod;b>>=1;
    }
    return r;
}
long long Comb(int a, int b){
    if(a<b||b<0)return 0ll;
    return F[a]*InvF[b]%Mod*InvF[a-b]%Mod;
}
int D[210][210][410], S[210][210][410];
int DD[210][210][410];
long long CC[210];
void Do(int d){
    int i, j, k;
    for(i=0;i<=101;i++){
        for(k=0;k<=i+i;k++){
            for(j=i;j<=i+d&&k<=200;j++){
                D[i][k][j]=S[i][j][k]=0;
            }
        }
    }
    D[0][0][0]=1;
    for(i=0;i<=100;i++){
        for(j=0;j<=i+i;j++){
            for(k=i;k<=i+d&&k<=200;k++){
                S[i][j][k]=D[i][j][k];
                if(k){
                    S[i][j][k]+=S[i][j][k-1];
                    if(S[i][j][k]>=Mod)S[i][j][k]-=Mod;
                }
            }
            for(k=i+1;k<=i+d&&k<=200;k++){
                int tj=j;
                if(k==i+1)tj++;
                if(k==i+d)tj++;
                D[i+1][tj][k]=(D[i+1][tj][k]+S[i][j][k])%Mod;
            }
        }
    }
    for(i=0;i<=101;i++){
        for(j=0;j<=i+i;j++){
            long long s=0;
            for(k=i;k<i+d;k++){
                s+=D[i][j][k];
            }
            DD[d][i][j]=s%Mod;
        }
    }
    
}
long long Calc(int n, int K){
    if(K*2<n-1)return 0ll;
    int d = 2*K-n+2, i, j, k;
    for(i=0;i<=n;i++)CC[i]=0;
    for(j=0;j<=n;j++){
        CC[j+1]=(CC[j+1] + DD[d][n-K-1][j])%Mod;
    }
    long long s=0;
    for(i=1;i<=n;i++){
        s=(s+CC[i]*Pow(i,Mod-2))%Mod;
    }
    s=s*F[n]%Mod;
    return s;
}
long long Get(int n, int K){
    if(K==n-1)return F[n];
    long long res=0;
    int i;
    for(i=0;i<=K;i++){
        res=(res+Calc(n-i,K-i)*Comb(n,i)%Mod*F[i])%Mod;
    }
    return res;
}
int main(){
    int i;
    int n, K;
    scanf("%d%d%lld",&n,&K,&Mod);
    F[0]=InvF[0]=1;
    for(i=1;i<=n;i++){
        F[i]=F[i-1]*i%Mod;
        InvF[i]=Pow(F[i],Mod-2);
    }
    long long res=0;
/*    for(i=K;i>=1;i--){
        res=(res+Get(n,i))%Mod;
    }*/
    for(i=1;i<=2*K-n+2;i++)Do(i);
    for(i=K;i>=1;i--){
        res=(res+Get(n,i))%Mod;
    }
    printf("%lld\n",res);
}
