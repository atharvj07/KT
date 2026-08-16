#include <bits/stdc++.h>
using namespace std;
int A[2][500005];
string S[2];
void Z(int x){
	A[x][0] = S[x].size();
	int i=1,j=0;
	while(i<S[x].size()){
		while(i+j<S[x].size() && S[x][j]==S[x][i+j])j++;
		A[x][i]=j;
		if(j==0){
			i++; continue;
		}
		int k = 1;
		while(i+k<S[x].size() && k+A[x][k]<j) A[x][i+k]=A[x][k],++k;
		i+=k;j-=k;
	}
}
vector<int>v[500005];
bool bad[500005],bad2[500005];
int main(){
	cin >> S[0];
	reverse(S[0].begin(),S[0].end());
	S[1] = S[0];
	reverse(S[0].begin(),S[0].end());
	Z(0); Z(1);
	for(int i=1;i<500005;i++)for(int j=2*i;j<500005;j+=i)v[j].push_back(i);
	for(int i=0;i<S[0].size();i++){
		for(int x=0;x<v[i+1].size();x++){
			int a = v[i+1][x];
			if(A[0][a] >= i+1-a){
				bad[i] = 1; break;
			}
		}
	}
	for(int i=0;i<S[1].size();i++){
		for(int x=0;x<v[i+1].size();x++){
			int a = v[i+1][x];
			if(A[1][a] >= i+1-a){
				bad2[i] = 1; break;
			}
		}
	}
	if(!bad[S[0].size()-1]){
		cout << 1 << endl << 1 << endl;
	}
	else{
	    int ans=0;
		for(int i=1;i<S[0].size();i++){
			if(!bad[i-1] && !bad2[S[0].size()-i-1]) ans++;
		}
		if(!ans) cout << S[0].size() << endl << 1 << endl;
		else cout << 2 << endl << ans << endl;
	}
}