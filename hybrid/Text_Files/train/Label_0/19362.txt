#include <iostream>
#include <string>

using namespace std;

int main()
{
	int s, t, u, d, w, h;
	string str;
	
	while(1){
		cin >> w >> h;
		if(w == 0 && h == 0){
			break;
		}
		s = t = 1;
		d = 0;
		while(1){
			cin >> str;
			if(str == "STOP"){
				break;
			} else if(str == "FORWARD"){
				cin >> u;
				if(d == 0){
					s+=u;
				} else if(d == 1){
					t+=u;
				} else if(d == 2){
					s-=u;
				} else {
					t-=u;
				}
			} else if(str == "RIGHT"){
				d++;
				if(d == 4){
					d = 0;
				}
			} else if(str == "LEFT"){
				d--;
				if(d < 0){
					d = 3;
				}
			} else if(str == "BACKWARD"){
				cin >> u;
				if(d == 0){
					s-=u;
				} else if(d == 1){
					t-=u;
				} else if(d == 2){
					s+=u;
				} else {
					t+=u;
				}
			}
			if(s < 1){
				s = 1;
			} else if(s > h){
				s = h;
			} else if(t < 1){
				t = 1;
			} else if(t > w){
				t = w;
			}
		}
		cout << t << " " << s << endl;
	}
	
	return 0;
}