#include <iostream>
#include <vector>
#include <cstring>

#define rep(i,n) for(int i=0;i<(n);i++)
#define YOKO 1
#define TATE 2

using namespace std;

struct B{
	int d;	// ubNÌü«@(1: ¡ü« 2: cü« )
	int p;	// ubNÌ·³  (1  d  5 )
	int q;	// ubNÌÊu@(1  p  5 ¡ü«ÌêÍ¶[ÌR}ª¿éÊu )
};

const int Hight = 5001;
const int Width = 5;

bool f[Hight][Width];

// cÁ½ubNðJEg
int count_block (void )
{
	int res = 0;

	for (int i = 0; i < Hight; i++ ){
		for (int j = 0; j < Width; j++ ){
			if (f[i][j] )
				res++;
		} // end for
	} // end for

	return res;
}

// ubNªlÜÁÄ¢éCðÁ·
void del_block (int n )
{
	for (int i = n + 1; i < Hight; i++ ){
		for (int j = 0; j < Width; j++ ){
			f[i-1][j] = f[i][j];
		} // end for
	} // end for
}

void is_all_row (void ) // ·×ÄubNªÜÁÄ¢éCðÁ·
{
	bool found = false;
	do{
		found = false;
		for (int i = 0; i < Hight; i++ ){
			int sum = 0;
			for (int j = 0; j < Width; j++ ){
				if (f[i][j] ){
					++sum;
				} // end if
			} // end for
			if (sum == Width ){
				del_block (i );
				found = true;
				break;			
			} // end if
		} // end for
	}while (found );
}

// row,colÌêÌãÌÊuªJ¢Ä¢é©Ç¤©Ì`FbN
bool check_tate (int row, int col )
{
	for (int i = row; i < Hight; i++ ){
		if (f[i][col] )
			return false;
	} // end for

	return true;
}

int main()
{
	int n;

	while (cin >> n && n ){
		memset (f, false, sizeof(f ) );
		vector <B> b (n );
		for (int i = 0; i < n; i++ ){
			cin >> b[i].d >> b[i].p >> b[i].q;
			b[i].q--;
		}// end for
	
		for (int i = 0; i < n; i++ ){
			int curr = 0;
			bool found = false; // »ÌÊuÉæqª é©Ç¤©
			do{
				found = false;	
				for (int j = b[i].q; j < b[i].q + b[i].p; j++ ){
					if (!check_tate (curr, j ) ){
						found = true;
						break;
					} // end if
					if (!f[curr][j] ){
						if (b[i].d == TATE ){	// cü«ÌêAê¾¯ÅOK
							break;
						}else{ 
							continue;
						} // end if
					}else{
						found = true;
						break;
					} // end if
				} // end for
				if (!found ){
					if (b[i].d == YOKO ){	// ¡ü«Ìê
						for (int j = b[i].q; j < b[i].q + b[i].p; j++ ){
							f[curr][j] = true;
						} // end for
					}else{					// cü«Ìê
						for (int j = 0; j < b[i].p; j++ ){
							f[curr+j][b[i].q] = true;
						} // end for 						
					} // end if
				}else{
					curr++;	// ²¸·ésðâ·
				} // end if
			}while (found );
			is_all_row ();	// ·×ÄÌCªlÜÁÄ¢é©`FbN
		} // end for

		int res = count_block();
		cout << res << endl;
	} // end loop
		
	return 0;
}