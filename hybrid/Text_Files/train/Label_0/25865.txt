#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class KuraInfo{
public:
	int num;
	int dist;
	int weight;
};

typedef pair<double,vector<int> > P;
P dp[(1<<15)][15];
int dp2[(1<<15)];

int n;
KuraInfo kuras[15];
const int INF=100000000;


P dfs(const int s,const int d,const double sumWeight,const int depth){
	if(s==0)
		return P(0,vector<int>());
	double minCost=INF;
	vector<int> rv;
	if(d==-1){
		for(int i = 0; i < n; i++){
			if(((s>>i)&1)){
				P ret = dfs((s&~(1<<i)),i,sumWeight+kuras[i].weight,depth+1);
				if(minCost>ret.first){
//					dp2[s]=i;
					ret.second.push_back(i);
					rv=ret.second;
					minCost=min(minCost,ret.first);
				}
			}
		}
	}
	else{
		if(dp[s][d].first!=INF)
			return dp[s][d];
		for(int i = 0; i < n; i++){
			if(((s>>i)&1)){
				P ret = dfs((s&~(1<<i)),i,sumWeight+kuras[i].weight,depth+1);
				ret.first+= ((double)abs(kuras[i].dist-kuras[d].dist))
					/(((double)2000)/(70+sumWeight));
				if(minCost>ret.first){
//					dp2[s]=i;
					ret.second.push_back(i);
					rv=ret.second;
					minCost=min(minCost,ret.first);
				}
			}
		}

	}
	dp[s][d]=P(minCost,rv);
	return dp[s][d];
}

int main(){

//	while(cin>>n){
	cin>>n;
	for(int i = 0; i < n; i++){
		cin>>kuras[i].num>>kuras[i].dist>>kuras[i].weight;
		kuras[i].weight*=20;
	}
	for(int i = 0; i < (1<<15); i++){
		fill(dp[i],dp[i]+15,P(INF,vector<int>()));
	}
	fill(dp2,dp2+(1<<15),INF);
	
	vector<int> v=dfs((1<<n)-1,-1,0,0).second;
	reverse(v.begin(),v.end());
	for(int i = 0; i < v.size(); i++){
		cout<<kuras[v[i]].num;
		if(i==v.size()-1)
			cout<<endl;
		else
			cout<<" ";
	}
		
		//int s = (1<<n)-1;
		//while(1){
		//	cout<<kuras[dp2[s]].num;
		//	s=(s&~(1<<dp2[s]));
		//	if(s==0){
		//		cout<<endl;
		//		break;
		//	}
		//	else
		//		cout<<" ";
		//}
//	}

	return 0;
}