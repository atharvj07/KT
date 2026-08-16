#include<iostream>
#include<string>
#include<iomanip>
#include<cmath>
#include<vector>
#include<algorithm>

using namespace std;

#define int long long
#define endl "\n"

const long long INF = (long long)1e18;
const long long MOD = (long long)1e9 + 7; 

string yn(bool f){return f?"Yes":"No";}
string YN(bool f){return f?"YES":"NO";}

#define MAX

signed main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout<<fixed<<setprecision(10);
	
	int H, W;
	int ans = 0;
	vector<string> c;
	vector<pair<int,int>> in;
	
	
	in.resize(4);
	in[0] = make_pair(INF,INF);
	in[1] = make_pair(INF,0);
	in[2] = make_pair(0,INF);
	in[3] = make_pair(0,0);
	
	cin>>H>>W;
	
	c.resize(H);
	
	for(int i  = 0; i < H; i++){
		cin>>c[i];
	}
	for(int i = 0; i < H; i++){
		for(int j = 0; j < W; j++){
			if(c[i][j] != 'B') continue;
			if(abs(in[0].first) + in[0].second > i + j){
				in[0] = make_pair(i,j);
			}
			if(abs(in[1].first) + abs(in[1].second-W+1) > abs(i) + abs(j-W+1)){
				in[1] = make_pair(i,j);
			}
			
			if(abs(in[2].first -H+1) + abs(in[2].second) > abs(i-H+1) + abs(j)){
				in[2] = make_pair(i,j);
			}
			
			if(abs(in[3].first -H+1) + abs(in[3].second-W+1) > abs(i -H+1) + abs(j-W+1)){
				in[3] = make_pair(i,j);
			}
		}
	}
	
	for(int i = 0; i < 4; i++){
		for(int j = i+1; j < 4; j++){
			ans = max(ans, abs(in[i].first-in[j].first) + abs(in[i].second-in[j].second));
		}
	}
	cout<<ans<<endl;
	return 0;
}
