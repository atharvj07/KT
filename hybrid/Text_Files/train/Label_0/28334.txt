#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
	map<string,vector<int> > dict;
	string str;
	int page;
	while(cin >> str >> page)
		dict[str].push_back(page);
	for(map< string,vector<int> >::iterator it = dict.begin();it!=dict.end();it++){
		sort(it->second.begin(),it->second.end());
		cout << it->first << endl;
		for(unsigned i=0;i<it->second.size();i++){
			cout << it->second[i];
			if(i<it->second.size()-1)
				cout << " ";
			else
				cout << endl;
		}
	}
	return 0;
}