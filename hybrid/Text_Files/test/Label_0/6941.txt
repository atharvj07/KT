// B - Two Colors Card Game
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<(int)(n);++i)

string in(){string x;cin>>x;return x;}

int main(){
	int n; cin>>n;
	map<string,int> s;
	rep(i, n) s[in()]++;
	int m; cin>>m;
	rep(i, m) s[in()]--;
	int ans = 0;
	for(auto x:s) ans = max(ans, x.second);
	cout<< ans <<endl;
}
