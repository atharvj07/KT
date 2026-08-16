#include<bits/stdc++.h>
#define rep(i,n) for (int i=0;i<n;i++)
#define ll long long
#define ALL(x) x.begin(),x.end()
using namespace std;
typedef pair<int,int> PII;

int dp[(1<<16)+10];
bool calc[(1<< 16) +10];
vector<vector<int>> edge;
const int INF = 1e9;
   int n,m,k;
map<int,int> idx_to_node;
map<int,int> node_to_idx;
map<int,bool> memD;

void dijkstra(){
  int dist[1<<m];
  rep(i,1<<m) dist[i] = INF;
  dist[(1<<m) - 1 ] = 0;
  priority_queue< PII, vector<PII>, greater<PII>> que;
  que.push({0,(1<<m)-1});
  while(que.empty() == false){
    PII p = que.top(); que.pop();
    int cdist = p.first;
    int cbit = p.second;
    if(dist[cbit] < cdist) continue;
    rep(i,k){
        int newBit = 0;
        rep(j,m){
            if((cbit >> j & 1) && memD[ edge[ idx_to_node[j] ][ i ] ] ) newBit |= 1<< node_to_idx[edge[idx_to_node[j]][i]];
        }
        if(dist[newBit] > cdist + 1){
          dist[newBit] = cdist + 1;
          que.push({cdist+1,newBit});
        }
    }

  }
  cout << dist[0] << endl;

}


int main(){
    cin >> n >> m >> k;

    rep(i,m){
        int x;
        cin >> x;
        x--;
        idx_to_node[i] = x;
        node_to_idx[x] = i;
        memD[x] = true;
    }
    edge.resize(n);
    rep(i,n){
      rep(j,k){
          int v;
          cin >> v;
          v--;
          edge[i].push_back(v);
      }
    }
    dijkstra();

    return 0;
}

