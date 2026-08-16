#include<iostream>
#include<math.h>
using namespace std;
int n;
int x,y,h1,h2,d1,d2,s1,s2;
  
double dist(int a, int b){
    return sqrt(a*a+b*b+0.0);
}  
int main(){
    while(1){
		bool ok=true;
        cin >> n;
        if(n == 0) break;
        cin >>h1>>h2>>d1>>d2>>s1>>s2;
		if(dist(h1-s1,h2-s2)>= dist(d1-s1,d2-s2))ok=false;
        for(int i=1;i<n;i++){
            cin>>x>>y;
			if(dist(h1-s1,h2-s2)+dist(s1-x,s2-y) >= dist(d1-x,d2-y))ok=false;
        }
  
        if(ok) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}