#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
regex reg("A?KIHA?BA?RA?");
string s;
int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cin >> s;
	puts(regex_match(s,reg) ? "YES" : "NO");
}