#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int main(){
	string s;
	int i;
	getline(cin, s);
	for(i=0;i<s.size();i++)
	if(s[i]==','||s[i]=='.')s[i]=' ';
	stringstream ss;
	ss<<s;
	int f=0,n;
	while(ss>>s){
		n=s.size();
		if(n>=3&&n<=6){
			cout<<((f==1)?" ":"")<<s;
			f=1;
		}
	}
	cout<<endl;
}