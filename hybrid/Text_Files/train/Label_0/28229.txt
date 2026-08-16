#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <functional>
#include <map>

#define INPUT_FROM_FILE (0) 
#if INPUT_FROM_FILE
#include <fstream>
#endif


int main(){
	int q, com;
	std::string key;
	long x;
	std::map<std::string, long> m;

#if INPUT_FROM_FILE
	std::ifstream ifs("test.txt");
#endif

#if INPUT_FROM_FILE
	ifs >> q;
#else
	std::cin >> q;
#endif
	
	for(int i = 0; i < q; i++){
#if INPUT_FROM_FILE
		ifs >> com >> key;
#else
		std::cin >> com >> key;
#endif
		if(com == 0){
#if INPUT_FROM_FILE
			ifs >> x;
#else
			std::cin >> x;
#endif
			m[key] = x;
		}
		else if(com == 1){
			std::cout << m[key] << std::endl;
		}
		else if(com == 2){
		}
		else{
	
		}
	}
	return 0;
}
