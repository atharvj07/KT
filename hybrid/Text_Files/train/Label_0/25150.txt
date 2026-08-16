#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;
using lint=long long;

lint solve(lint h,lint w){
	lint res=h*w;
	rep(i,h-1){
		lint a=(i+1)*w,b=(h-i-1)*w;
		lint c=((i+1)/2)*w;
		lint d=(i+1)*(w/2);
		res=min(res,max({b,c,a-c})-min({b,c,a-c}));
		res=min(res,max({b,d,a-d})-min({b,d,a-d}));
	}
	return res;
}

int main(){
	lint h,w; cin>>h>>w;
	cout<<min(solve(h,w),solve(w,h))<<endl;
	return 0;
}
