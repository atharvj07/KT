#include<iostream>
#include<string>
#include<queue>
#include<map>
#include<vector>
#include<algorithm>
#include<set>
#include<functional>

#define MAX_ITEM 256
using namespace std;

const int infty = 1<<27;

class Node{
public:
  vector<int> con;
  vector<int> cost;
  int item_num;
  pair<int,int> shop[MAX_ITEM];
};

typedef vector<Node> Graph;

inline bool lesscost(const pair<int,int> &p1, const pair<int,int> &p2){
  if( p1.first < p2.first )
    return true;
  if( p1.first == p2.first && p1.second < p2.second )
    return true;
  return false;
}
inline bool greatercost(const pair<int,int> &p1, const pair<int,int> &p2){
  if( p1.first > p2.first )
    return true;
  if( p1.first == p2.first && p1.second > p2.second )
    return true;
  return false;
}

class State{
public:
  int now;
  int have;
  pair<int,int> cost;
  bool operator>(const State &t)const{
    return greatercost(cost,t.cost);
  }
};

pair<int,int> dijkstra(int n, Graph &G, int q, State init){
  priority_queue< State,vector<State>,greater<State> > qs;
  pair<int,int> cost[1<<q][n];
  bool vis[1<<q][n];
  
  for(int i = 0; i < (1<<q); ++i){
    for(int j = 0; j < n; ++j){
      cost[i][j] = make_pair(infty,infty);
      vis[i][j] = false;
    }
  }
  
  qs.push(init);
  cost[0][0]=make_pair(0,0);
  
  while(!qs.empty()){
    State now = qs.top();
    qs.pop();
    
    if( vis[now.have][now.now] )
      continue;
    vis[now.have][now.now] = true;

    int id = now.now;

    /*
      cout << now.now << ' ' << " HAVING : " << now.have << ' ' ;
      for(int i=0;i<q;++i){
      if(now.have&(1<<i))cout << '1';
      else cout <<'0';
      }
      cout << " COST = " << now.cost.first << ',' << now.cost.second << endl;
    */

    for(int j = 0; j < G[id].item_num; ++j){
      State next=now;
      int jbit = (1<<G[id].shop[j].first);
      int jval = G[id].shop[j].second;
      
      if( now.have & jbit ){
	continue;
      }
      
      next.have |= jbit;
      next.cost.first += jval;
      
      if( lesscost( next.cost, cost[next.have][next.now] ) ){
	cost[next.have][next.now] = next.cost;
	if( !vis[next.have][next.now] ){
	  qs.push( next );
	}
      }
    }
    
    for(int i = 0; i < G[id].con.size(); ++i){
      State next = now;
      next.now = G[id].con[i];
      next.cost = make_pair( now.cost.first, now.cost.second + G[id].cost[i] );
      
      if( lesscost( next.cost, cost[next.have][next.now] ) ){
	cost[next.have][next.now] = next.cost;
	if( !vis[next.have][next.now] ){
	  qs.push( next );
	}
      }
    }
  }
  return cost[(1<<q)-1][0];
}

int main()
{

  while(true){
    int n;
    bool impossible=false;
    cin >> n;
    Graph G(n+1);
    map<string,int> shop[n+1];
    map<string,int> item_bit;
    if( n == 0 ) break;

    for(int i = 1; i < n+1; ++i){
      int k;
      cin >> k;
      for(int j = 0; j < k; ++j){
	string item;
	int val;
	cin >> item >> val;
	shop[i][item]=val;
      }
    }

    int q;
    cin >> q;
    for(int i = 0; i < q; ++i){
      string s;
      cin >> s;
      item_bit[s]=i;
    }

    for(int i = 0; i < n+1; ++i){
      G[i].item_num = 0;
      for(int j = 0; j < MAX_ITEM; ++j){
	G[i].shop[j] = make_pair(-1,infty);
      }
      for(map<string,int>::iterator itm = item_bit.begin(); itm != item_bit.end(); ++itm){
	if( shop[i].find( itm->first ) != shop[i].end() ){
	  G[i].shop[ G[i].item_num ] = make_pair(item_bit[itm->first],shop[i][itm->first]);
	  G[i].item_num++;
	}
      }
    }

    int m;
    cin >> m;
    for(int i = 0; i < m; ++i){
      int s,t,d;
      cin >> s >> t >> d;
      G[s].con.push_back(t);
      G[s].cost.push_back(d);
      G[t].con.push_back(s);
      G[t].cost.push_back(d);
    }

    State init;
    init.now = 0;
    init.have = 0;
    init.cost = make_pair(0,0);
    pair<int,int> ans;

    ans = dijkstra( n+1, G, q, init );
    if( ans.first >= infty ){
      cout << "impossible" << endl;
    }else{
      cout << ans.first << ' ' << ans.second << endl;
    }
  }
  return 0;
}