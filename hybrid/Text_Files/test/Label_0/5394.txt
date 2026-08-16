#include<iostream>
#include<cstdlib>
#include<cmath>
#include<complex>
#include<vector>
#include<algorithm>
#include<cassert>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)
#define pb         push_back

typedef complex<int> P;
const double eps= 1e-10;
const int N =200;
int cross(P a,P b){//ll?
  return a.real()*b.imag()-a.imag()*b.real();
}

//ê¼üÌf[^ðÈ­Í<0,È«½­È¢Í<=0É·éÆ¢¢B
int ccw(P a,P b){
  if ( cross(a,b) <0)return 1;
  else return -1;
}

bool cmp(const P&a,const P&b){
  if ( a.real() != b.real())return a.real()<b.real();
  else return a.imag() < b.imag();
}

void ConvexHull(int n,P *inp,P *out,int &p){
  sort(inp,inp+n,cmp);
  bool used[n];
  int num[n];
  fill(used,used+n,false);
  p=0;
  out[p++]=inp[0];out[p++]=inp[1];
  used[1]=true;
  num[0]=0;num[1]=1;
  for(int i=2;i<n;i++){
    while(p>=2){
      if ( ccw(out[p-1]-out[p-2],inp[i]-out[p-2]) ==1)break;
      else {
	used[num[p-1]]=false;
	p--;
      }
    }
    num[p]=i;
    used[i]=true;
    out[p++]=inp[i];
  }
  for(int i=n-2,t=p+1;i>=0;i--){
    if ( used[i] == true)continue;
    while(p>=t){//·ÅÉÊïÉÈÁ½_ðÁ³È¢æ¤É·éB
      if ( ccw(out[p-1]-out[p-2],inp[i]-out[p-2]) ==1)break;
      else p--;
    }
    out[p++]=inp[i];
  }
  return;
}

int polygon_area(const P *a,int n){
  int sum = 0;
  for(int i=0;i<n;i++){
    sum += (a[i%n].real()-a[(i+1)%n].real())*(a[i%n].imag()+a[(i+1)%n].imag());
  }
  
  //if (sum < 0)sum=-sum;
  return sum;
}

double dist(P a){
  complex<double> ho((double)a.real(),(double)a.imag());
  return abs(ho);
  return sqrt((double)a.real()*a.real()+(double)a.imag()*a.imag());
}

bool isp(P a,P b,P c){
  return dist(a-c)+dist(b-c) < dist(a-b)+eps;
}

bool is_intersected_ls(P a1,P a2,P b1,P b2){
  if ((cross(a2-a1,b1-a1)*cross(a2-a1,b2-a1)<0 ) && 
      (cross(b2-b1,a1-b1)*cross(b2-b1,a2-b1)<0))return true;
  else return false;
}

class Edge{
public:
  int num;
  double dist;
  int val;
};
vector<Edge>edge[N];

const int M = 20010;
double dp[N][M];

int solve(int n,P *in,double r,int lim){
  if (r==0)return 0;

  rep(i,n){
    REP(j,i+2,n+1){
      bool isok=true;
      if (!isok)continue;
      rep(k,n+1){
	if (k%n==i||(k+1)%n==i||
	    k%n==j||(k+1)%n==j)continue;
      	if (is_intersected_ls(in[i],in[j],in[k],in[k+1])){isok=false;break;}
      }
      if (!isok)continue;
      int tmp = polygon_area(in+i,j-i+1);
      if( tmp > 0)continue;
      tmp=-tmp;
      if (i == 0  && j == n)continue;
      edge[i].pb((Edge){j,dist(in[i]-in[j]),tmp});
    }
  }
  
  rep(i,n+1){
    rep(j,M)dp[i][j]=1e20;
    dp[i][0]=0;
  }

  rep(i,n){
    rep(j,M){
      if (i)dp[i][j]=min(dp[i][j],dp[i-1][j]);
      rep(k,edge[i].size()){
	int nexi=edge[i][k].num;
	int nexj=j+edge[i][k].val;
	double nev=dp[i][j]+edge[i][k].dist;
	if (nexj >= M)continue;
	dp[nexi][nexj]=min(dp[nexi][nexj],nev);
      }
    }
  }
  
  int ans = 0;
  for(int j=M-1;j>0;j--){
    rep(i,n+1){
      if (dp[i][j] <= r+eps){return j;}
    }
  }
  return 0;
}

int main(){
  int n,r;
  int tc=1;
  P tmp[N],hoge[N],in[N],out[N];
  while(cin>>n>>r && n){
    int p=0;
    int ans=0;
    rep(i,N)edge[i].clear();
    
    rep(i,n){
      int x,y;
      cin>>x>>y;
      tmp[i]=P(x,y);
      hoge[i]=tmp[i];
    }
    ans = polygon_area(hoge,n);
    ConvexHull(n,hoge,out,p);
    int lim=polygon_area(out,p);
    
    int move=-1;
    rep(i,n){
      if (out[0] == tmp[i]){
	move=i;
	break;
      }
    }
    rep(i,n){
      in[i]=tmp[(i+move)%n];
    }
    tmp[n]=tmp[0];
    in[n]=in[0];
    rep(i,n)in[n+i]=in[i];
    rep(i,n)tmp[n+i]=tmp[i];
    
    ans+=solve(n,in,(double)r,lim-ans);
    printf("case %d: %.1lf\n",tc++,ans/2.);
  }
}