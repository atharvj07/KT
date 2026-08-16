#include <bits/stdc++.h>
using namespace std;
int h, w,cnt;
char c;
int main() {
	cin>>h>>w;
  	for(int i=0;i<h;i++){
    	for(int j=0;j<w;j++){
       		cin>>c;
          	if(c=='#')cnt++;
        }
    }
  cout<<(cnt==h+w-1?"Possible":"Impossible")<<endl;
}