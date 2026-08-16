#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int main(){
	int h,w; cin>>h>>w;
	vector<string> B(h);
	rep(i,h) cin>>B[i];

	vector<string> res1(h,string(w,'.'));
	vector<string> res2(h,string(w,'.'));
	rep(i,h) rep(j,w) {
		if(i==0 || (i<h-1 && j%2==0)) res1[i][j]='#';
		else                          res2[i][j]='#';
		if(B[i][j]=='#') res1[i][j]=res2[i][j]='#';
	}

	rep(i,h) cout<<res1[i]<<'\n';
	cout<<'\n';
	rep(i,h) cout<<res2[i]<<'\n';

	return 0;
}
