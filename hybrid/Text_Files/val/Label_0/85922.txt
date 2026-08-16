#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
#include<map>
#include<set>
using namespace std;
typedef pair<int,int> P;
typedef pair<int,P> PP;
#define F first
#define S second
#define INF (10000000)
int N;
int X[100001];
int Y[100001];
int mp[]={1,-1,1,-1};
int mm[]={1,1,-1,-1};
int Used[100001];
priority_queue<P> Q[3][4];
inline int ab(int a){ return a>0?a:-a; }
int getk(int id1,int id2){
  return ab(X[id1] - X[id2]) + ab(Y[id1] - Y[id2]);
}
PP max_point(int id1,int id2){
  if(Q[id1][0].empty()) return PP(-1,P(-1,-1));
  if(Q[id2][0].empty()) return PP(-1,P(-1,-1));
  PP ret = PP(getk( Q[id1][0].top().S, Q[id2][3].top().S), 
	      P(Q[id1][0].top().S, Q[id2][3].top().S));
  ret = max( ret, PP(getk( Q[id1][1].top().S, Q[id2][2].top().S),
		     P(Q[id1][1].top().S, Q[id2][2].top().S)) );
  ret = max( ret, PP(getk( Q[id1][2].top().S, Q[id2][1].top().S),
		     P(Q[id1][2].top().S, Q[id2][1].top().S)) );
  ret = max( ret, PP(getk( Q[id1][3].top().S, Q[id2][0].top().S),
		     P(Q[id1][3].top().S, Q[id2][0].top().S)) );
  return ret;
}
int max_point_s(int id,int A){
  if(Q[id][0].empty()) return -1;
  int ret = 1;
  for(int i=0;i<2;i++)
    ret = max( ret, getk(Q[id][i].top().S,A));
  return ret;
}
void deleted_point(){
  for(int i=0;i<4;i++){
    while( !Q[0][i].empty() && Used[Q[0][i].top().S] ) Q[0][i].pop();
  }
}
int main(){
  scanf("%d",&N);
  for(int i=0;i<N;i++){
    scanf("%d %d",&X[i],&Y[i]);
    for(int j=0;j<4;j++){
      Q[0][j].push(P(mp[j]*X[i]+mm[j]*Y[i],i));
    }
  }  

  while( !Q[0][0].empty() ){
    PP h = max_point(0,0);
    PP p1 = max_point(0,1);
    PP p2 = max_point(0,2);
    if ( h.F > p1.F && h.F > p2.F ){
      int p1m = max( max_point_s(1,h.S.F), max_point_s(2,h.S.S));
      /*max ( max( max_point(1,1).F, max_point_s(1,h.S.F) ),
	max( max_point(2,2).F, max_point_s(2,h.S.S) ) );
      */
      int p2m = max( max_point_s(1,h.S.S), max_point_s(2,h.S.F));
      /*max ( max( max_point(1,1).F, max_point_s(1,h.S.S) ),
	max( max_point(2,2).F, max_point_s(2,h.S.F) ) );  
      */
      Used[h.S.F]=1;
      Used[h.S.S]=1;
      if( p1m > p2m ){
	for(int i=0;i<4;i++){
	  Q[1][i].push( P(mp[i]*X[h.S.S]+mm[i]*Y[h.S.S],h.S.S) );
	  Q[2][i].push( P(mp[i]*X[h.S.F]+mm[i]*Y[h.S.F],h.S.F) );
	}
      } else {
	for(int i=0;i<4;i++){
	  Q[2][i].push( P(mp[i]*X[h.S.S]+mm[i]*Y[h.S.S],h.S.S) );
	  Q[1][i].push( P(mp[i]*X[h.S.F]+mm[i]*Y[h.S.F],h.S.F) );
	}
      }
    } else if( p1 > p2){
      Used[ p1.S.F ] = 1;
      for(int i=0;i<4;i++)
	Q[2][i].push( P(mp[i]*X[p1.S.F]+mm[i]*Y[p1.S.F],p1.S.F) );
    } else {
      Used[ p2.S.F ] = 1;
      for(int i=0;i<4;i++)
	Q[1][i].push( P(mp[i]*X[p2.S.F]+mm[i]*Y[p2.S.F],p2.S.F) );
    }
    deleted_point();
  }
  printf("%d\n",max( max_point(1,1).F, max_point(2,2).F ) );
}