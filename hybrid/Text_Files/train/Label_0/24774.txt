#include<bits/stdc++.h>
using namespace std;
double eps=1e-9;
double inf=1e9;

int N,M,Q;
double w[12],h[12];
double x[10],y[10];
double p[10],t[10],ans[10];
double s[11][10];
int L[11],R[11],par[11],flg[11];


int find(int id){
  if(par[id]==id)return id;
  return par[id]=find(par[id]);
}

void init(){
  for(int i=0;i<Q;i++)ans[i]=-1;
  for(int i=0;i<=N;i++){
    L[i]=w[i];
    R[i]=w[i+1];
    par[i]=i;
    flg[i]=0;
    for(int j=0;j<M;j++)s[i][j]=inf;
  }
}

void func(int id,int &left,int &right){
  id=find(id);
  left=N+1,right=0;
  for(int i=0;i<=N;i++){
    if(find(i)!=id)continue;
    left=min(left,i);
    right=max(right,i+1);
  }
}

double calc(int id){
  id=find(id);
  double lh,lw=inf,rh,rw=-inf;
  for(int i=0;i<=N;i++){
    if(find(i)!=id)continue;
    if(w[i]<lw)lw=w[i],lh=h[i];
    rw=w[i+1],rh=h[i+1];
    for(int j=0;j<M;j++)s[id][j]=min(s[id][j],s[i][j]);
  }
  double V=min(lh,rh)*(rw-lw)*30.0,sum=0;
  for(int j=0;j<M;j++){
    if(s[id][j]==inf)continue;
    V+=s[id][j]*y[j];
    sum+=y[j];
  }
  return V/sum;
}

double compute(int id,double t){
  id=find(id);
  double lw=inf,rw=-inf;
  for(int i=0;i<=N;i++){
    if(find(i)!=id)continue;
    if(w[i]<lw)lw=w[i];
    rw=w[i+1];
    for(int j=0;j<M;j++)s[id][j]=min(s[id][j],s[i][j]);
  }
  double V=0;
  for(int j=0;j<M;j++){
    if(t<s[id][j])continue;
    V+=(t-s[id][j])*y[j];
  }
  double res=V/( (rw-lw)*30.0 );
  int left,right;
  func(id,left,right);
  if(flg[id])res=min(res,min(h[left],h[right]));
  return res;
}

bool check(double now,double next){
  bool res=true;
  for(int i=0;i<Q;i++){
    if(ans[i]==-1)res=false;
    if(t[i]<now-eps||next+eps<t[i])continue;
    int id;
    for(id=0;w[id+1]<p[i];id++);
    ans[i]=compute(id,t[i]);
  }
  return res;
}

bool visited[11];
void update(int id,int yi,double t){
  if(visited[id])return;
  visited[id]=true;
  s[id][yi]=min(s[id][yi],t);
  if(id-1>=0&&compute(id,t)>h[id]-eps)update(id-1,yi,t);
  if(id+1<=N&&compute(id,t)>h[id+1]-eps)update(id+1,yi,t);
}


void solve(){
  for(int i=0;i<M;i++){
    int id;
    for(id=0;w[id+1]<x[i];id++);
    s[id][i]=0;
  }
  
  double now=0,next=0;
  while(1){
    now=next;
    next=inf;

    for(int i=0;i<=N;i++){
      if(find(i)!=i||flg[i])continue;
      next=min(next,calc(i));
    }
    
    check(now,next);
    if(find(0)==find(N))break;
    
    for(int i=0;i<=N;i++){
      if(find(i)!=i||flg[i])continue;
      double tv=calc(i);
      if(next<tv-eps||tv+eps<next)continue;
      
      int left,right;
      func(i,left,right);
      if(h[left]==h[right])return;
      
      int target=(h[left]<h[right]?left-1:right);
      target=find(target);

      for(int j=0;j<M;j++){
        if(s[i][j]==inf)continue;
        if(s[target][j]==inf){
          flg[i]=1;
          memset(visited,0,sizeof(visited));
          update(target,j,next);
        }else{
          par[find(max(target,i))]=find(min(target,i));
          for(int k=0;k<=N;k++)
            if(find(i)==find(k))flg[k]=0;
        }
      }
    }

  }//while
}

int main(){
  int Tc;
  cin>>Tc;
  while(Tc--){
    cin>>N;
    w[0]=0,w[N+1]=100;
    h[0]=h[N+1]=inf;
    for(int i=1;i<=N;i++)cin>>w[i]>>h[i];
    cin>>M;
    for(int i=0;i<M;i++)cin>>x[i]>>y[i];
    cin>>Q;
    for(int i=0;i<Q;i++)cin>>p[i]>>t[i];
    init();
    solve();
    for(int i=0;i<Q;i++)printf("%.10f\n",min(50.0,ans[i]));
  }
  return 0;
}