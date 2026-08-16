#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i,a) for(int i=0;i<(a);i++)
const ll MOD=1000000007;

const int MAX_N=1010;
ll inv[MAX_N+1], fact[MAX_N+1], ifact[MAX_N+1];

ll comb(int n, int k){
  if(n<k) return 0;
  return fact[n]*ifact[k]%MOD*ifact[n-k]%MOD;
}

void prepare(){
  inv[1]=fact[0]=fact[1]=ifact[0]=ifact[1]=1LL;
  for(int i=2;i<=MAX_N;i++){
    inv[i]=inv[MOD%i]*(MOD-MOD/i)%MOD;
    fact[i]=fact[i-1]*i%MOD;
    ifact[i]=ifact[i-1]*inv[i]%MOD;
  }
}

// dp[k][n]:n人に対して，k人以下のグループを作った場合のグループ分けの個数
ll dp[1010][1010];

int main(){
  prepare();
  int N,A,B,C,D; cin>>N>>A>>B>>C>>D;
  dp[A][0]=1;
  for(int i=A;i<=B;i++) for(int j=0;j<=N;j++) if(dp[i][j]!=0){
    (dp[i+1][j]+=dp[i][j])%=MOD;
    ll tmp=1LL;
    int num=N-j;
    for(int k=1;j+k*i<=N&&k<=D;k++){
      (tmp*=comb(num,i))%=MOD;
      num-=i;
      if(k>=C) (dp[i+1][j+k*i]+=tmp*dp[i][j]%MOD*ifact[k]%MOD)%=MOD;
    }
  }
  cout<<dp[B+1][N]<<endl;
  return 0;
}
