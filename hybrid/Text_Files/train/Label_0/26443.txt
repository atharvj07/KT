#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int l,r,ans;
char s[1000000];
int main(){
	cin>>s;l=0;r=strlen(s)-1;
	while (l<r){
		if (s[l]==s[r]){l++;r--;continue;}
		if (s[l]=='x'){l++;ans++;continue;}
		if (s[r]=='x'){r--;ans++;continue;}
		cout<<-1<<endl;return 0;
	}cout<<ans<<endl;
}