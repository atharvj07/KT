#include<bits/stdc++.h>
using namespace std;
struct E{long long t,c;};
vector<E>G[1<<17];
long long z[1<<17];
int n,a,b,c,q,i,j;
void d(int x,int p){
  for(auto &e:G[x])if(e.t-p)z[e.t]=z[x]+e.c,d(e.t,x);
}
int main(){
  for(cin>>n;++i<n;G[a].push_back({b,c}),G[b].push_back({a,c}))scanf("%d%d%d",&a,&b,&c);
  for(cin>>q>>n,d(n,0);j++<q;printf("%lld\n",z[a]+z[b]))scanf("%d%d",&a,&b);
}
