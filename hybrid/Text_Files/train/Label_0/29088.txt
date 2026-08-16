#include<bits/stdc++.h>
using namespace std;
int dp[3005][3005];
int n, t; vector<pair<int, int> >v;
int f(int now, int time){
	if(now==n) return 0;
	if(time>=t) return 0;
	if(dp[now][time]!=-1) return dp[now][time];
	dp[now][time]=max(0, max(f(now+1, time), f(now+1, time+v[now].first)+v[now].second));
	return dp[now][time];
}
int main(){
	cin>>n>>t; v.resize(n);
	for(int i=0; i<n; i++){
		cin>>v[i].first>>v[i].second;
	}
	sort(v.begin(), v.end());
	memset(dp, -1, sizeof(dp));
	cout<<f(0, 0)<<endl;
	return 0;
}