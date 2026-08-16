#include <iostream>
#include <map>
#include <string>
using namespace std;

int main(){
	int id;
	char c;
	string bt;
	map<string, int> b;
	while(cin >> id >> c >> bt){
		b[bt]++;
	}
	cout << b["A"] << endl;
	cout << b["B"] << endl;
	cout << b["AB"] << endl;
	cout << b["O"] << endl;
	return 0;
}