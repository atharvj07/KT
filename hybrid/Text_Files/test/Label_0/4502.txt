#include <iostream>
#include <string>
using namespace std;

int main(){
	int k;
	string s;
	cin >> s >> k;
	for(int i = 0;i < s.length();i++){
		if(s[i] != 'a' && 'z' - s[i] + 1 <= k){
			k -= 'z' - s[i] + 1;
			s[i] = 'a';
		}
	}
	s[s.length() - 1] += k % 26;
	if(s[s.length() - 1] > 'z') s[s.length() - 1] -= 26;
	cout << s << endl;
}