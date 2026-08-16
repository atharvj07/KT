#include<bits/stdc++.h>
using namespace std;
int T,last[205],vis[205],cnt;
char ans[205];
string s;
stack<char>st;
int main(){
	cin>>T;
	while(T--){
		cnt=0;
		memset(last,0,sizeof(last));
		memset(vis,0,sizeof(vis));
		cin>>s;
		for(int i=0;i<s.size();i++)last[s[i]]=i;
		for(int i=0;i<s.size();i++){
			if(vis[s[i]])continue;
			while(!st.empty()&&st.top()<s[i]&&last[st.top()]>i){
				vis[st.top()]=0;
				st.pop();
			}
			st.push(s[i]);
			vis[s[i]]=1;
		}
		while(!st.empty()){
			ans[++cnt]=st.top();
			st.pop();
		}
		for(int i=cnt;i>=1;i--)cout<<ans[i];
		cout<<endl;
	}
}