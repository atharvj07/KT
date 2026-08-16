#include "bits/stdc++.h"
#include<vector>
#include<iostream>
#include<queue>
#include<algorithm>
#include<map>
#include<set>
#include<iomanip>
#include<assert.h>
#include<unordered_map>
#include<unordered_set>
#include<string>
#include<stack>
#include<complex>
#pragma warning(disable:4996)
using namespace std;
using ld = long double;
template<class T>
using Table = vector<vector<T>>;
const ld eps=1e-9;
	
#define WHATS(var)//cout<<__LINE__<<' '<<#var<<"="<<var<<endl;
	
template<class S, class T> ostream& operator <<(ostream &os, const pair<S, T> v){
	os << "( " << v.first << ", " << v.second << ")"; return os;
}
template<class T> ostream& operator <<(ostream &os, const vector<T> &v){
	for(int i = 0; i < v.size(); i++){if(i > 0){os << " ";} os << v[i];} return os;
}
template<class T> ostream& operator <<(ostream &os, const vector<vector<T>> &v){
	for(int i = 0; i < v.size(); i++){if(i > 0){os << endl;} os << v[i];} return os;
}
template<class T> ostream& operator <<(ostream &os, const vector<set<T>> &v){
	for(int i = 0; i < v.size(); i++){if(i > 0){os << endl;} os << v[i];} return os;
}
template<class T> ostream& operator <<(ostream &os, const set<T> &v){
	int i=0;
	for(auto it:v){
		if(i > 0){os << ' ';}
		os << it;
		i++;
	} 
	return os;
}

using ll =long long ;
ll mod;

void solve(vector<vector<int>>&cango){
	int tt=cango.size();
	for(int i=0;i<tt;++i){
		for(int j=0;j<tt;++j){
			for(int k=0;k<tt;++k){
				cango[j][k]|=cango[j][i]&cango[i][k];
			}
		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	int N;cin>>N;
	cin>>mod;
	vector<vector<ll>>dp(2,vector<ll>(1<<12,false));
	{
		vector<int>v(3);
		for(;v[0]<2;++v[0]){
			for(;v[1]<2;++v[1]){
				for(;v[2]<2;++v[2]){
					vector<vector<int>>cango(4,vector<int>(4));
					if(v[0])cango[0][2]=true;
					else cango[2][0]=true;
					if(v[1])cango[1][3]=true;
					else cango[3][1]=true;
					if(v[2])cango[2][3]=true;
					else cango[3][2]=true;
					solve(cango);
					int nextj=0;
					int id=0;
					for(int x=0;x<4;++x){
						for(int y=0;y<4;++y){
							if(x==y)continue;
							else{
								if(cango[x][y])nextj|=(1<<id);
								id++;
							}
						}
					}
					dp[1][nextj]+=1;
					WHATS(cango)
				}
				v[2]=0;
			}
			v[1]=0;
		}
	}		

	for(int i=1;i<N;++i){
		int cur=i&1;
		int tar=1-cur;
		//cout<<5<<endl;
		for(int j=0;j<(1<<12);++j){
			
			if(!dp[cur][j])continue;
			vector<int>v(3);
			for(;v[0]<2;++v[0]){
				for(;v[1]<2;++v[1]){
					for(;v[2]<2;++v[2]){
						bool ok=true;
						vector<vector<int>>cango(6,vector<int>(6));
						for(int k=0;k<12;++k){
							int from=k/3;
							int to=k%3;
							if(to>=from)to++;
							if(j&(1<<k))cango[from][to]=true;
						}
						if(v[0])cango[2][4]=true;
						else cango[4][2]=true;
						if(v[1])cango[3][5]=true;
						else cango[5][3]=true;
						if(v[2])cango[4][5]=true;
						else cango[5][4]=true;
						
						WHATS(cango)
						solve(cango);
						for(int x=0;x<6;++x){
							if(cango[x][x])ok=false;

						}
						if(i==N-1&&(cango[0][4]||cango[4][0]||cango[5][1]||cango[1][5]||(cango[0][1]&&cango[5][4])||(cango[1][0]&&cango[4][5])))ok=false;
						
						if(ok){
							vector<int>all{0,1,4,5};
							int id=0;
							int nextj=0;
							for(int x=0;x<4;++x){
								for(int y=0;y<4;++y){
									if(x==y)continue;
									else{
										if(cango[all[x]][all[y]])nextj|=(1<<id);
										id++;
									}
								}
							}
							dp[tar][nextj]+=dp[cur][j];
							if(dp[tar][nextj]>=mod)dp[tar][nextj]-=mod;
						}
					}
					v[2]=0;
				}
				v[1]=0;
			}
			v[0]=0;
		}
		dp[cur]=vector<ll>(1<<12,false);
		//cout<<4<<endl;
	}
	ll answer=0;
	//cout<<6<<endl;
	for(int j=0;j<(1<<12);++j){
		
		answer+=dp[N%2][j];
	}
	answer%=mod;
	cout<<answer<<endl;
	return 0;	
}
