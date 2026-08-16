#include<iostream>
#include<algorithm>
using namespace std;

/*--------*/
/*   06   */
/* 05  04 */
/*   03   */
/* 02  01 */
/*   00   */
/*--------*/

/*------------*/
/*     18     */
/*   17  16   */
/* 15  14  13 */
/*   12  11   */
/* 10  09  08 */
/*   07  06   */
/* 05  04  03 */
/*   02  01   */
/*     00     */
/*------------*/

const int block[7][7] = { {  0,  1,  2,  4,  6,  7,  9},
			  {  1,  3,  4,  6,  8,  9, 11},
			  {  2,  4,  5,  7,  9, 10, 12},
			  {  4,  6,  7,  9, 11, 12, 14},
			  {  6,  8,  9, 11, 13, 14, 16},
			  {  7,  9, 10, 12, 14, 15, 17},
			  {  9, 11, 12, 14, 16, 17, 18}	};

int main(){
  string f;
  while(cin >> f){
    if(f=="#")return 0;
    
    bool res = true;
    for(int input=0;input<(1<<19);input++){
      int next = 0;
      for(int i=0;i<7;i++){
	int bit = 0;
	for(int j=0;j<7;j++){
	  if( (input>>block[i][j]) & 1 ) bit |= 1<<j;
	}
	if(f[bit] == '1')next |= 1<<i;
      }

      if( (f[next]-'0') != ((next>>3)&1) ){
	res = false; break;
      }
    }
    
    if(res)cout << "yes" << endl;
    else cout << "no" << endl;
  }
}