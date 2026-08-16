#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;cin>>s;
	int cnt=0;for(int i=0;i<s.size();i++)cnt+=(s[i]=='x');
	cout<<(cnt>=8?"NO\n":"YES\n");
	return 0;
}