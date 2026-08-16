#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


typedef unsigned long long ll;

vector<vector<ll> > lines;
int n;
int field[9][9];

vector<ll> tmp;

const int dy[]={0,0,-1,1};
const int dx[]={1,-1,0,0};

bool ok=false;

ll fin;


void dfs(ll s,int idx){
	if(ok){
		return;
	}
	if(idx==lines.size()){
		if(fin==s)
			ok=true;
		return;
	}
	for(int i = 0; i < lines[idx].size(); i++){
		if((s&lines[idx][i])==0){
			dfs(s|lines[idx][i],idx+1);
		}
	}
}

void lineSearch(ll s,int curSum,int ret,int x,int y){
	if(curSum==ret){
		tmp.push_back(s);
	}
	for(int i= 0; i < 4; i++){
		int nx=x+dx[i];
		int ny=y+dy[i];
		if(nx>=0&&ny>=0&&nx<n&&ny<n&&field[ny][nx]>=1&&(curSum+field[ny][nx]<=ret)){
			if(!((s>>(ny*n+nx))&(1ull))){
				ll ns=s|(((1ull)<<(ny*n+nx)));
				lineSearch(ns,curSum+field[ny][nx],ret,nx,ny);
			}
		}
	}
}

int main(){


	while(cin>>n&&n!=0){
		fin=0;
		for(int i = 0; i < n*n; i++){
			fin|=(1ull<<i);
		}

		ok=false;
		lines.clear();
		vector<pair<int,pair<int,int> > > vpii;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cin>>field[i][j];
				if(field[i][j]<0){
					vpii.push_back(make_pair(field[i][j],make_pair(i,j)));
				}
			}
		}
		for(int i = 0; i < vpii.size(); i++){
			tmp.clear();
			lineSearch(((1ull)<<(vpii[i].second.first*n+vpii[i].second.second)),0,-vpii[i].first,vpii[i].second.second,vpii[i].second.first);
			lines.push_back(tmp);
		}
		dfs(0ull,0);
		if(ok)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}

	return 0;
}