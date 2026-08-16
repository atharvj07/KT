#include<iostream>
#include<algorithm>
using namespace std;
int a[26]={0},b[26]={0};
int main(){
	string s,t;
	int i,j,f=1;
	cin >> s >> t;
	for(i=0;i<s.size();i++){
		a[s[i]-'a']++;
	}
	for(i=0;i<t.size();i++){
		b[t[i]-'a']++;
	}
	sort(a,a+26);
	sort(b,b+26);
	for(i=0;i<26;i++){
		if(a[i]!=b[i]){
			f=0;
			break;
		}
	}
	if(f==0){
		cout <<"No\n";
	}
	else{
		cout << "Yes\n";
	} 
	return 0;
}
