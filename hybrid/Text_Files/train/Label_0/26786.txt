#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

const int N=1000010,P=924844033;

int n,cnt,G[N],a[N],A[N],B[N];
struct edge{
  int t,nx;
}E[N<<1];

inline void addedge(int x,int y){
  E[++cnt].t=y; E[cnt].nx=G[x]; G[x]=cnt;
  E[++cnt].t=x; E[cnt].nx=G[y]; G[y]=cnt;
}

int dfs(int x,int f){
  int ret=1;
  for(int i=G[x];i;i=E[i].nx){
    if(E[i].t==f) continue;
    int cur=dfs(E[i].t,x);
    a[cur]++; ret+=cur;
  }
  a[n-ret]++;
  return ret;
}

int w[2][N],rev[N],L,m,fac[N],inv[N];

inline int Pow(int x,int y){
  int ret=1;
  for(;y;y>>=1,x=1LL*x*x%P) if(y&1) ret=1LL*ret*x%P;
  return ret;
}

inline void Pre(){
  int g=Pow(5,(P-1)/m);
  w[0][0]=w[1][0]=1;
  for(int i=1;i<m;i++) w[1][i]=1LL*w[1][i-1]*g%P;
  for(int i=1;i<m;i++) w[0][i]=w[1][m-i];

  fac[0]=1; for(int i=1;i<m;i++) fac[i]=1LL*fac[i-1]*i%P;
  inv[1]=1; for(int i=2;i<m;i++) inv[i]=1LL*(P-P/i)*inv[P%i]%P;
  inv[0]=1; for(int i=1;i<m;i++) inv[i]=1LL*inv[i]*inv[i-1]%P;
}

inline void NTT(int *a,int m,int r){
  for(int i=1;i<m;i++) if(rev[i]>i) swap(a[i],a[rev[i]]);
  for(int i=1;i<m;i<<=1)
    for(int j=0;j<m;j+=i<<1)
      for(int k=0;k<i;k++){
	int x=a[j+k],y=1LL*w[r][m/(i<<1)*k]*a[j+k+i]%P;
	a[j+k]=(x+y)%P; a[j+k+i]=(x+P-y)%P;
      }
  if(!r) for(int i=0,inv=Pow(m,P-2);i<m;i++) a[i]=1LL*a[i]*inv%P;
}

inline int C(int x,int y){
  return 1LL*fac[x]*inv[y]%P*inv[x-y]%P;
}

int main(){
  scanf("%d",&n);
  for(int i=1,x,y;i<n;i++)
    scanf("%d%d",&x,&y),addedge(x,y);
  dfs(1,0);
  for(m=1;m<=n;m<<=1,L++); m<<=1; Pre();
  for(int i=1;i<m;i++) rev[i]=(rev[i>>1]>>1)|((i&1)<<L);
  for(int i=1;i<=n;i++) A[i]=1LL*a[i]*fac[i]%P,B[m-i]=inv[i]; B[0]=1;
  NTT(A,m,1); NTT(B,m,1);
  for(int i=0;i<m;i++) A[i]=1LL*A[i]*B[i]%P;
  NTT(A,m,0);
  for(int i=1;i<=n;i++){
    int cur=1LL*n*C(n,i)%P;
    cur=(cur-1LL*inv[i]*A[i])%P;
    printf("%d\n",(cur+P)%P);
  }
  return 0;
}
