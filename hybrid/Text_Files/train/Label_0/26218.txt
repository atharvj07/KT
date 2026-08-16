#include <iostream>
using namespace	std;
int main()
{
  int n;
  cin >> n;
  for(int j=0;j<n;j++){
    int y,m,d,c=0;
    cin >> y >> m >> d;
    for(int i=y; i<1000 ;i++){
      if (i%3==0)
        c+=200;
      else
        c+=195;
    }
    c-=d;
    c++;
    for (int i=1;i<m;i++){
      if(y%3==0)
        c-=20;
      else{
        if(i%2==0)
          c-=19;
        else
          c-=20;
      }
    }
    cout << c << endl;
  }
}