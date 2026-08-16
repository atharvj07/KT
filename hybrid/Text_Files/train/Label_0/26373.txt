#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin>>N;
  vector<vector<int>> G(N);
  for(int i=1;i<N;i++){
    int a,b;
    cin>>a>>b;
    a--,b--;
    G[b].push_back(a);
    G[a].push_back(b);
  }
  int A=0;
  queue<int> q;
  q.push(A);
  vector<int> seen(N);
  seen[A]=1;
  while(!q.empty()){
    A=q.front();
    q.pop();
    for(int x:G[A]){
      if(!(seen[x])){
        q.push(x);
        seen[x]=1;
      }
    }
  }
  q.push(A);
  vector<int> sen(N);
  sen[A]=2;
  while(!q.empty()){
    A=q.front();
    q.pop();
    for(int x:G[A]){
      if(!(sen[x])){
        q.push(x);
        sen[x]=sen[A]+1;
      }
    }
  }
  int Z=sen[A];
  if(Z%3){
    cout<<"First"<<endl;
  }
  else{
    cout<<"Second"<<endl;
  }
}