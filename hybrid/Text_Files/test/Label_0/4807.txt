#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

string s;
int nextWordToFor(int cur)
{
	if(cur==s.size()) return cur;

	for(; cur<s.size(); cur++)
	{
		if(s[cur]!=' ') break;
	}
	for(; cur<s.size(); cur++)
	{
		if(s[cur]==' ') break;
	}

	return cur;
}

int nextWordToDel(int cur)
{
	int tcur=nextWordToFor(cur);

	return tcur;
}

int prevWordToBak(int cur)
{
	if(cur==0) return cur;
	cur--;

	for(; cur>0; cur--)
	{
		if(s[cur]!=' ') break;
	}
	for(; cur>0; cur--)
	{
		if(s[cur]==' ') 
		{
			cur++;
			break;
		}
	}

	return cur;
}

int main()
{
	int N;
	cin >> N;
	
	getline(cin, s);
	while(N--)
	{
		int cur=0;
		getline(cin, s);
	
		int C;
		cin >> C;
		while(C--)
		{
			string c,cmd,obj;
			cin >> cmd;
			getchar();
			getline(cin, obj);

			if(cmd[0]=='f')
			{
				if(obj[0]=='c') 
				{
					if(cur<s.size()) cur++;
				}
				else
				{
					cur=nextWordToFor(cur);
				}
			}
			if(cmd[0]=='b')
			{
				if(obj[0]=='c') 
				{
					if(cur>0) cur--;
				}
				else cur = prevWordToBak(cur);
			}
			if(cmd[0]=='d')
			{
				if(obj[0]=='c')
				{
					if(cur==s.size()) continue;
					s.erase(s.begin()+cur);
				}
				else
				{
					int cur2;
					cur2=nextWordToFor(cur);
					if(cur==s.size()) continue;
					if(s[cur2-1]==' ') continue;

					s.erase(s.begin()+cur, s.begin()+cur2);	
				}
			}
			if(cmd[0]=='i')
			{
				obj = obj.substr(1, obj.size()-2);
				s.insert(cur, obj);
				cur += obj.size();
			}
			string h(s);
			h.insert(cur, "7");
			//cout << h << endl;
		}

		s.insert(cur, "^");
		cout << s << endl;
	}

}