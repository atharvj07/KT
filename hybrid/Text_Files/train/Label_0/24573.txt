#include <iostream>
#include <algorithm>
using namespace std;
#define INF 1e8

int main(){
    int V,E;
    cin>>V>>E;
    int G[V][V];
    fill(G[0],G[V],INF);
    int ans=0;
    int deg[V];
    fill(deg,deg+V,0);//?¬???°
    for(int i=0;i<E;i++){
        int s,t,d;
        cin>>s>>t>>d;
        G[s][t]=G[t][s]=min(G[s][t],d);
        ans+=d;
        deg[s]++;deg[t]++;
    }
    unsigned int M=0;
    for(int i=0;i<V;i++){
        if(deg[i]%2) M|=(1<<i); 
    }
    for(int i=0;i<V;i++)G[i][i]=0;
    for(int k=0;k<V;k++){
        for(int i=0;i<V;i++){
            for(int j=0;j<V;j++){
                G[i][j]=min(G[i][j],G[i][k]+G[k][j]);
            }
        }
    }
    int dp[1<<V];
    fill(dp,dp+(1<<V),INF);
    dp[0]=0;
    for(unsigned int S=0;S<(1<<V);S++){
        if(__builtin_popcount(S)%2)continue;
        for(int i=0;i<V;i++){
                if(!((1<<i)&S))continue;
            for(int j=i+1;j<V;j++){
                if(!((1<<j)&S))continue;
                unsigned int s = ((1<<i)|(1<<j))^S;
                dp[S]=min(dp[S],dp[s]+G[i][j]);
            }
        }
    }
    ans+=dp[M];
    cout<<ans<<endl;
}