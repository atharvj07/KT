#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <functional>
#include <utility>
#include <algorithm>
#include <numeric>
#include <typeinfo>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <ctime>

using namespace std;

#define dump(n) cout<<"# "<<#n<<"="<<(n)<<endl
#define debug(n) cout<<__FILE__<<","<<__LINE__<<": #"<<#n<<"="<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define rep(i,n) repi(i,0,n)
#define iter(c) __typeof((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();i++)
#define allof(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

int main()
{
	map<char,string> atoc;
	{
		char a[]={
			'A','B','C','D','E','F','G','H',
			'I','J','K','L','M','N','O','P',
			'Q','R','S','T','U','V','W','X',
			'Y','Z',' ','.',',','-','\'','?',
		};
		string c[]={
			"00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111",
			"01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111",
			"10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111",
			"11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111",
		};
		rep(i,32)
			atoc[a[i]]=c[i];
	}
	map<string,char> ctoa;
	{
		string c[]={
			"101", "000000", "000011", "10010001", "010001", "000001", "100101", "10011010",
			"0101", "0001", "110", "01001", "10011011", "010000", "0111", "10011000",
			"0110", "00100", "10011001", "10011110", "00101", "111", "10011111", "1000",
			"00110", "00111", "10011100", "10011101", "000010", "10010010", "10010011", "10010000",
		};
		char a[]={
			' ','\'',',','-','.','?','A','B',
			'C','D','E','F','G','H','I','J',
			'K','L','M','N','O','P','Q','R',
			'S','T','U','V','W','X','Y','Z',
		};
		rep(i,32)
			ctoa[c[i]]=a[i];
	}
	
	for(string a;getline(cin,a);){
		string c;
		rep(i,a.size())
			c+=atoc[a[i]];
		
		string res;
		for(int i=0;;){
			bool found=false;
			foreach(j,ctoa){
				if(j->first==c.substr(i,j->first.size())){
					res+=j->second;
					i+=j->first.size();
					found=true;
					break;
				}
			}
			if(!found)
				break;
		}
		cout<<res<<endl;
	}
	
	return 0;
}