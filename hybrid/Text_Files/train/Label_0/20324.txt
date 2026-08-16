#include <bits/stdc++.h>
using namespace std;
vector<vector<int> > A;
typedef pair<int,int> P;

bool bfs(){
  sort(A.begin(),A.end());
  A.erase(unique(A.begin(),A.end()),A.end());
  int n = A.size();
  for(int i=0;i<n;i++)
    for(int j=0,used[10]={};j<A[i].size();j++)if(used[A[i][j]]++) return 1;

  queue<P> Q;
  bool D[1<<10][1<<10]={};
  D[0][0]=1;
  Q.push(P(0,0));
  while(!Q.empty()){
    P t = Q.front();Q.pop();
    int I = t.first,J = t.second;
    if(I&&J&&__builtin_popcount(I&J) == __builtin_popcount(J)) return 1;

    for(int i=0;i<n;i++){
      for(int k=0,ni=I;k<A[i].size();k++){
	int num = A[i][k],nj =(J|1<<num);
	if(k&&D[ni][nj]==0&&J!=nj)D[ni][nj]=1, Q.push(P(ni,nj));
	if(I&(1<<num))break;
	ni |= (1<<num);
      }
    }
  }
  return 0;
}

int main(){
  int n;
  while(cin>>n,n){
    string str;
    cin>>str;
    A.clear();
    for(int i=0;i<str.size();i++){
      A.push_back(vector<int>());
      while(str[i]!='u') A.back().push_back(str[i++]-'0');
    }
    cout<<(bfs()? "UN":"")<<"SAFE"<<endl;
  }
  return 0;
}