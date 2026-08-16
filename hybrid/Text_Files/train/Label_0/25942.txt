#include<bits/stdc++.h>
using namespace std;
const int N=30;
int t, r, n, cnt[N], ans[N];
bool vis[N];  
string st;
int main(){
	cin>>t;
	while (t){
		t--;
		cin>>st;
		n=st.length();
		for (int i=0; i<N; i++){
			cnt[i]=0;
			vis[i]=0;
		}		
		r=0;
		for (int i=0; i<n; i++) cnt[st[i]-'a']++;
		for (int i=0; i<n; i++){
			int ch=st[i]-'a';
			cnt[ch]--;
			if (vis[ch]) continue;
			while (r>0 && cnt[ans[r-1]] && ch>ans[r-1]) {
				vis[ans[r-1]]=0;
				r--;
			}
			ans[r++]=ch;
			vis[ch]=1;
		}
		for (int i=0; i<r; i++) cout<<(char)('a'+ans[i]);
		cout<<endl;
	}
}