#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <queue>
#include <vector>
#include <sstream>

#define rep(x,to) for(int x=0;x<to;x++)
#define rep2(x,from,to) for(int x=from;x<to;x++)

using namespace std;

int f(int y,int m,int d){
	return (y*365+y/4-y/100+y/400+m*28+(m+1)*26/10+d-400);
}

int main(void){

  int d[6];
	while(!cin.eof()){
		rep(i,6) cin >> d[i];
		rep(i,6) if(d[i]<0) goto endd;
		
		if(d[1]<3){ d[1] +=12; d[0]--;}
		if(d[4]<3){ d[4] +=12; d[3]--;}
		cout << (f(d[3],d[4],d[5]) - f(d[0],d[1],d[2])) << endl;
	}
  endd:
	return 0;
	
}