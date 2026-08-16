#include <iostream>
#include <set>
#define PI pair<int,int>
using namespace std;
char m[101][101];
int main()
{
  int h,w,i,j;
  for(;;){
    cin >> h >> w;
    if(h==0 && w==0) break;
    for(i=0;i<h;i++){
      cin >> m[i];
    }
    i = j = 0;
    set< PI > s;
    s.insert(PI(i,j));
    for(;;){
      if(m[i][j] == '.') {
	cout << j << " " << i << endl;
	break;
      }
      switch(m[i][j]){
      case '>': j++; break;
      case '<': j--; break;
      case '^': i--; break;
      case 'v': i++; break;
      }
      if(s.find(PI(i,j)) != s.end()){
	cout << "LOOP" << endl;
	break;
      }
      s.insert(PI(i,j));
    }
  }
  return 0;
}