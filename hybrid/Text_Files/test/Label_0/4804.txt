#include<iostream>
#include<queue>
#include<map>
#define rep(i,n) for(int i=0;i<n;i++)
using namespace std;
int main(){
	int s,d;
	while(cin>>s>>d,s){
		int sd[s][d],dd[d][d],t;
		rep(i,s)rep(j,d)cin>>sd[i][j];
		rep(i,d)rep(j,d){
			if(i<j)cin>>t,dd[i][j]=dd[j][i]=t;
			if(i==j)dd[i][i]=0;
		}
		int cost=0,V[d],v=0; rep(i,d)V[i]=0;
		priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > >F;
		rep(i,s)rep(j,d)if(sd[i][j])F.push(make_pair(sd[i][j],j));
		while(v<d&&!F.empty()){
			int cc=F.top().first,cn=F.top().second;F.pop();
			if(V[cn]||!cc)continue;
			V[cn]=1,cost+=cc,v++;
			rep(i,d)if(!V[i]&&dd[cn][i])F.push(make_pair(dd[cn][i],i));
		}
		cout<<cost<<endl;
	}
	return 0;
}