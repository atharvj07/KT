#include <iostream>
#include <queue>

using namespace std;

int waiti[100];
int seat[17];

const int INIT = 0xffffff;

typedef struct MATI
{
	int id;
	int num;
	int eat;
} MATI;

int get_eat(int n)
{
	return 17 * (n%2) + 3 * (n%3) + 19;
}

int get_num(int n)
{
	if(n%5==1) return 5;
	else return 2;
}

int can_sit(int n)
{
	bool is_able = true;
	for(int i=0; i<=17-n; i++)
	{
		is_able = true;
		for(int j=0; j<n; j++)
		{
			if(seat[i+j] != 0)
			{
				is_able = false;
				break;
			}
		}
		
		if(is_able) return i;
	}
	
	return -1;
}

void refresh()
{
	for(int i=0; i<17; i++)
	{
		if(seat[i] != 0)
		{
			seat[i] = seat[i] - 1;
			
		}
	}
}

void solve()
{
	for(int i=0; i<17; i++)
	{
		seat[i] = 0;
	}
	
	queue<MATI> col;
	
	for(int i=0; i<1000; i++)
	{
		int current_time = i;
		refresh();
		
		if(current_time%5==0)
		{
			MATI m;
			m.id = current_time /5;
			m.num = get_num(m.id);
			m.eat = get_eat(m.id);
			col.push(m);
		}
		
		while(!col.empty())
		{
			MATI m = col.front();
			int setter = can_sit(m.num);
			if(setter != -1)
			{
				for(int j=0; j<m.num; j++)
				{
					seat[setter+j] = m.eat;
				}
				
				int wait_time = current_time - m.id * 5;
				waiti[m.id] = wait_time;
				if(m.id==99) return;
				col.pop();
			}
			else
			{
				break;
			}
		}
	}
}

int main(int argc, char** argv)
{
	int n;
	solve();
	
	while(cin >> n)
	{
		cout << waiti[n] << endl;
	}
}