#include<bits/stdc++.h>
using namespace std;
#define MAX_V 105
#define INF 1000000001
typedef pair< double ,int> P;

struct edge {
  int to;
  int cap;
  int rev;
  double cost;
};

int V;
vector<edge> G[MAX_V];
double h[MAX_V];
double dist[MAX_V];
int prevv[MAX_V],preve[MAX_V];

void init_edge(){
  for(int i=0;i<MAX_V;i++)G[i].clear();
}

void add_edge(int from,int to,int cap,double cost){
  G[from].push_back((edge){to,cap,(int)G[to].size(),cost});
  G[to].push_back((edge){from,0,(int)G[from].size()-1,-cost});
}

double min_cost_flow(int s,int t,int f){
  double eps = 1e-5;
  double res = 0;
  fill(h,h+V,0.0);
  
  while(f>0){
    
    priority_queue< P, vector<P>, greater<P> >  que;
    fill( dist, dist+V , (double)INF );
    dist[s]=0;
    que.push(P(0,s));

    fill ( prevv , prevv + V , s );
    
    while(!que.empty()){
      P p = que.top(); que.pop();
      int v = p.second;
      if(dist[v]+eps < p.first)continue;
      for(int i=0;i<(int)G[v].size();i++){
        edge &e = G[v][i];
        if(e.cap>0&&dist[e.to] > eps+dist[v]+e.cost+h[v]-h[e.to]){
          dist[e.to]=dist[v]+e.cost+h[v]-h[e.to];
          prevv[e.to]=v;
          preve[e.to]=i;
          que.push(P(dist[e.to],e.to));
        }
      }
    }

        
    if(dist[t] == INF){
      return -1;
    }
    for(int v=0;v<V;v++)h[v]+=dist[v]; 

    int d=f;
    for(int v=t;v!=s;v=prevv[v]){
      d=min(d,G[prevv[v]][preve[v]].cap);
    }
    assert( d > 0 );
    f-=d;

    res+=d*h[t];

    for(int v=t;v!=s;v=prevv[v]){
      edge &e = G[prevv[v]][preve[v]];
      e.cap -= d;
      G[v][e.rev].cap += d;
    }

  }
  return res;
}

typedef vector< double > vec;
typedef vector<vec> mat;


vec gauss_jordan(const mat&A,const vec&b){
  int n=A.size();
  mat B(n,vec(n+1));
  for(int i=0;i<n;i++)
    for(int j=0;j<n;j++)B[i][j]=A[i][j];
  for(int i=0;i<n;i++)B[i][n]=b[i];
  for(int i=0;i<n;i++){
    int pivot=i;
    for(int j=i;j<n;j++)
      if(abs(B[j][i])>abs(B[pivot][i]))pivot=j;
    swap(B[i],B[pivot]);
    if(abs(B[i][i])< 0.0000001 )return vec();
    for(int j=i+1;j<=n;j++)B[i][j]/=B[i][i];
    for(int j=0;j<n;j++){
      if(i!=j)
        for(int k=i+1;k<=n;k++)B[j][k]-=B[j][i]*B[i][k];
    }
  }
  vec x(n);
  for(int i=0;i<n;i++)x[i]=B[i][n];
  return x;
}

int N,si,ti,F;
int M;

int main(){
  int T;
  cin>>T;
  while(T--){

    init_edge();
    cin>>N>>si>>ti>>F;
    
    mat A( N , vec(N) );
    vec B( N );
    
    for(int i=0;i<N;i++){
      for(int j=0;j<N;j++)scanf("%lf",&A[i][j]);
      scanf("%lf",&B[i]);
    }
    
    vec C=gauss_jordan(A,B);
    
    for(int i=0;i<N;i++){
      
      cin>>M;
      vector<int> d(M);
      vector<int> f(M);
      for(int j=0;j<M;j++)scanf("%d",&d[j]);
      for(int j=0;j<M;j++)scanf("%d",&f[j]);
      
      for(int j=0;j<M;j++){
        add_edge(i,d[j],f[j], abs(C[i]-C[d[j]]) );
        
      }
    }
    V=N;
    double ans=min_cost_flow(si,ti,F);
    if(ans<=-1.0){
      cout<<"impossible"<<endl;
    }else{
      printf("%.10f\n",ans);
    }
  }
  return 0;
}