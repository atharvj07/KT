#include<iostream>
#include<cmath>
#include<string>
#include<map>
#include<queue>
using namespace std;

#define N  3
#define N2 9

static const int dx[4]   = {-1,0,1,0};
static const int dy[4]   = {0,-1,0,1};
static const char dir[4] = {'u','l','d','r'};

struct Puzzle{
  int f[N2];
  int space;
  string path;

  bool operator<(const Puzzle &p)const {
    for(int i=0;i<N2;i++){
      if(f[i]==p.f[i])continue;
      return f[i]>p.f[i];
    }
    return false;
  }
};



bool isTarget(Puzzle x){
  for(int i=0;i<N2;i++)
    if(x.f[i]!=(i+1))   return false;
    return true;
}

string bfs(Puzzle start){
  queue<Puzzle> Q;
  map<Puzzle, bool> V;
  Puzzle u, v;
  start.path = "";
  Q.push(start);
  V[start] = true;

  while(!Q.empty()){
    u = Q.front(); Q.pop();
    if(isTarget(u))return u.path;
    int xStart = u.space / N;
    int yStart = u.space % N;

    for(int k=0;k<4;k++){
	    int xTarget = xStart + dx[k];
	    int yTarget = yStart + dy[k];
	    if(xTarget<0 || yTarget<0 || xTarget >=N || yTarget>=N) continue;
	    v = u;
	    swap(v.f[u.space],v.f[xTarget*N+yTarget]);
	    v.space = xTarget*N+yTarget;
	    if(!V[v]){
	      V[v] = true;
	      v.path += dir[k];
	      Q.push(v);
	    }
    }
  }
  return NULL;
}
  

int main(){
  Puzzle in;
  for(int i=0;i<N2;i++){
    cin>>in.f[i];
    if(in.f[i]==0){
      in.f[i]  = N2;
      in.space = i;
    }
  }
  string ans = bfs(in);
  cout<<ans.size()<<endl;
  
  return 0;
}

