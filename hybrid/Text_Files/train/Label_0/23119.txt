#include<bits/stdc++.h>
#define INF (1e9)
#define N 101
using namespace std;
typedef pair<int,int> P;
typedef pair<int,P> P1;

int m,n,k1,s,t,flag;
vector<int> ei[N],eo[N];
string cond;
vector<P1> v[N];
map<int,P> pam[N];

int main(){
  cin>>m>>n;
  for(int i=0;i<m;i++){
    cin>>k1;
    for(int j=0;j<k1;j++){
      cin>>s>>cond>>t;
      if(cond[0]=='>')v[i].push_back(P1(s,P(t,INF)));
      else v[i].push_back(P1(s,P(0,t)));
    }
    sort(v[i].begin(),v[i].end());
  }
  
  for(int i=0;i<m;i++){
    for(int j=0;j<(int)v[i].size()-1;j++){
      if(v[i][j].first!=v[i][j+1].first)continue;
      int min1=v[i][j].second.first;
      int max1=v[i][j].second.second;
      int min2=v[i][j+1].second.first;
      int max2=v[i][j+1].second.second;
      if(max1<min2)flag=1;
      else{
	v[i][j]=P1(v[i][j+1].first,P(max(min1,min2),min(max1,max2)));
	v[i].erase(v[i].begin()+j+1);
	j--;
      }
    }
  }
  for(int i=0;i<m;i++)
    for(int j=0;j<(int)v[i].size();j++){
      int t1=v[i][j].first;
      int t2=v[i][j].second.first;
      int t3=v[i][j].second.second;
      pam[i].insert(make_pair(t1,P(t2,t3)));
    }
  for(int i=1;i<=n;i++){
    for(int j=0;j<m;j++){
      if(pam[j].find(i)==pam[j].end())continue;
      map<int,P>::iterator ite1=pam[j].find(i);
      for(int k=j+1;k<m;k++){
	if(pam[k].find(i)==pam[k].end())continue;
	if(j==k)continue;
	map<int,P>::iterator ite2=pam[k].find(i);
	int min1=(*ite1).second.first;
	int max1=(*ite1).second.second;
	int min2=(*ite2).second.first;
	int max2=(*ite2).second.second;
	if(max1<min2){
	  eo[j].push_back(k);
	  ei[k].push_back(j);
	}
	if(max2<min1){
	  eo[k].push_back(j);
	  ei[j].push_back(k);
	}
      }
    }
  }
  queue<int> S,L;
  for(int i=0;i<m;i++)
    if(!ei[i].size())S.push(i);
  while(!S.empty()){
    int t=S.front(); S.pop();
    L.push(t);
    for(int i=0;i<eo[t].size();i++){
      int out=eo[t][i];
      for(int k=0;k<ei[out].size();k++)
	if(ei[out][k]==t)ei[out].erase(ei[out].begin()+k);
      eo[t].erase(eo[t].begin()+i);
      i--;
      if(!ei[out].size())S.push(out);
    }
  }
  for(int i=0;i<m;i++)
    if(ei[i].size()||eo[i].size())flag=1;
  if(flag)cout<<"No"<<endl;
  else cout<<"Yes"<<endl;
  return 0;
}