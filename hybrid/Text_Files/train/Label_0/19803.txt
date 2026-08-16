#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

struct node{
  vector<int> con;
  vector<int> cost;
  vector<int> e_id;
};

typedef vector<node> Graph;

struct State{
  int now;
  int dist;
  int used;
  State(int n, int d, int u):now(n),dist(d),used(u){}
  bool visited(int i){return (bool)(used&(1LL<<i));}
  void setUse(int i){used|=(1LL<<i);}
  vector<int> hist;
  bool operator>(const State &t)const{
    return dist > t.dist;
  }
};

pair<int,vector<int> > solve(int st, Graph &G){
  priority_queue<State,vector<State>,greater<State> > Q;
  State init(st,0,0);
  init.hist.push_back(st+1);
  Q.push(init);
  pair<int, vector<int> > ret;
  while(!Q.empty()){
    State nst = Q.top();
    Q.pop();
    int nowid = nst.now;

    if(ret.first<nst.dist){
      ret=make_pair(nst.dist,nst.hist);
    }else if(ret.first==nst.dist){
      if(nst.hist<ret.second){
	ret.second = nst.hist;
      }
    }

    for(int i = 0; i < (int)G[nowid].con.size(); ++i){
      State next(G[nowid].con[i], nst.dist + G[nowid].cost[i], nst.used);
      if(!nst.visited(G[nowid].e_id[i])){
	next.setUse(G[nowid].e_id[i]);
	next.hist=nst.hist;
	next.hist.push_back(G[nowid].con[i]+1);
	Q.push(next);
      }
    }
  }
  return ret;
}

int main()
{
  while(true){
    int ns,nl;
    cin >> ns >> nl;
    if(ns==0&&nl==0)break;
    Graph G(ns);
    for(int i = 0; i < nl; ++i){
      int src,dst,w;
      cin >> src >> dst >> w;
      G[src-1].con.push_back(dst-1);
      G[src-1].cost.push_back(w);
      G[src-1].e_id.push_back(i);
      G[dst-1].con.push_back(src-1);
      G[dst-1].cost.push_back(w);
      G[dst-1].e_id.push_back(i);
    }
    pair<int, vector<int> > res;
    for(int i = 0; i < ns; ++i){
      pair<int, vector<int> > tmp = solve(i,G);
      if(res.first < tmp.first){
	res = tmp;
      }else if( res.first == tmp.first ){
	if( tmp.second < res.second )
	  res.second = tmp.second;
      }
    }
    cout << res.first << endl;
    for(int i = 0; i < (int)res.second.size(); ++i){
      if(i>0)cout << ' ';
      cout << res.second[i];
    }
    cout << endl;
  }
  return 0;
}