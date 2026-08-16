#include <iostream>
#include <string>
using namespace std;

int main(void){
	string s;
	while(cin >> s){
		int ioi=0,joi=0;
		for(int i=0;i<s.size()-2;i++){
			if(s[i] == 'I' && s[i+1] == 'O' && s[i+2] == 'I') ioi++;
			if(s[i] == 'J' && s[i+1] == 'O' && s[i+2] == 'I') joi++;
		}
		cout << joi << endl;
		cout << ioi << endl;
	}
}