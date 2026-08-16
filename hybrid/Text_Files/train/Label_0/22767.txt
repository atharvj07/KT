#include <bits/stdc++.h>
using namespace std;
int main(){
	int n,m;
	while(true){
		cin>>n;
		if(n==0)	return 0;
		cin>>m;
		string s;	cin>>s;
		long long ans=0;
		for(int i=0;i<m;i++){
			if(s[i]=='I'){
				int cnt=0;
				while(i+2<m&&s[i+1]=='O'&&s[i+2]=='I')	i+=2,cnt++;
				ans+=max(0,cnt-n+1);
			}
		}
		cout<<ans<<endl;
	}
}