#include <iostream>
using namespace std;

int main()
{
	int w;
	while(cin >> w, w>=0)
	{
		int a = 4280-1150;
		
		if(w>30)
		{
			a -= (w-30)*160;
			w  = 30;
		}
		if(w>20)
		{
			a -= (w-20)*140;
			w  = 20;
		}
		if(w>10)
		{
			a -= (w-10)*125;
		}

		cout << a << endl;
	}
}