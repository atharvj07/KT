#include <bits/stdc++.h>
using namespace std;
const int inf = 2000000000;

struct P{
	int x,y;
};
P p[40];

P operator - (P a,P b){
	return {a.x - b.x, a.y - b.y};
}

int cross(P a,P b){
	return a.x * b.y - a.y * b.x;
}
P bP;
bool operator < (const P &a,const P &b){
	return cross(a-bP,b-bP) > 0;
};
int cmp(int i,int j){
	return p[i] < p[j];
}
int area(int i,int j,int k){
	return cross(p[j]-p[i],p[k]-p[i]);
}

// dp[1st][k][k-1th][kth]
int dp[40][41][40][40];
int prv[40][41][40][40];

int main(){
	for(int i = 0 ; i < 40 ; i++)
		for(int j = 0 ; j < 41 ; j++)
			for(int k = 0 ; k < 40 ; k++)
				for(int l = 0 ; l < 40 ; l++)
					dp[i][j][k][l] = inf;

	int N;
	cin >> N;
	for(int i = 0 ; i < N ; i++){
		cin >> p[i].x >> p[i].y;
	}
	for(int i = 0 ; i < N ; i++){
		vector<int> id;
		for(int j = 0 ; j < N ; j++)
			if( i != j && p[i].x <= p[j].x ) id.push_back(j);
		
		bP = p[i];
		sort(id.begin(),id.end(),cmp);
		for(int J = 0 ; J < id.size() ; J++){
			int j = id[J];
			for(int K = J+1 ; K < id.size() ; K++){
				int k = id[K];
				if( cmp(j,k) ){
					dp[i][3][j][k] = area(i,j,k);
					prv[i][3][j][k] = i;
				}
			}
		}
		for(int s = 4 ; s <= 40 ; s++)
			for(int J = 0 ; J < id.size() ; J++){
				int j = id[J];
				for(int K = J+1 ; K < id.size() ; K++){
					int k = id[K];
					if( dp[i][s-1][j][k] == inf ) continue;
					for(int L = K+1 ; L < id.size() ; L++){
						int l = id[L];
						if( cross(p[k]-p[j],p[l]-p[j]) > 0  && dp[i][s][k][l] > dp[i][s-1][j][k] + area(i,k,l) ){
							dp[i][s][k][l] = dp[i][s-1][j][k] + area(i,k,l);
							prv[i][s][k][l] = j;
						}
					}
				}
			}
	}
	int Q;
	cin >> Q;
	for(int i = 0 ; i < Q ; i++){
		int s;
		cin >> s;
		int a,b,c;
		int ans = inf;
		for(int j = 0 ; j < N ; j++){
			for(int k = 0 ; k < N ; k++){
				for(int l = 0 ; l < N ; l++){
					if( ans > dp[j][s][k][l] ){
						ans = dp[j][s][k][l];
						a = j;
						b = k;
						c = l;
					}
				}
			}
		}
		if( ans == inf ) cout << "NA" << endl;
		else{
			vector<int> idx;
			while(s > 3 ){
				idx.push_back(c);
				int t = prv[a][s][b][c];
				c = b;
				b = t;
				s--;
			}
			idx.push_back(c);
			idx.push_back(b);
			idx.push_back(a);
			reverse(idx.begin(),idx.end());
			int lowX = inf;
			int lowY = inf;
			int pos;
			for(int j = 0 ; j < idx.size() ; j++)
				if( lowY > p[idx[j]].y ){
					lowY = p[idx[j]].y;
					lowX = p[idx[j]].x;
					pos = j;
				}else if( lowY == p[idx[j]].y ){
					if( lowX > p[idx[j]].x ){
						lowX = p[idx[j]].x;
						pos = j;
					}
				}
			rotate(idx.begin(),idx.begin()+pos,idx.end());
			for(int j = 0 ; j < idx.size() ; j++)
				cout << idx[j]+1 << " \n"[j+1==idx.size()];
		}

	}
}