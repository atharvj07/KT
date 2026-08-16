#include <iostream>
#include <string>
#include <map>
using namespace std;

map<char, string> encode_table;
map<string, char> decode_table;

char decode(string s) {
//    cout << s << endl;
    return decode_table[s];
}

string encode(string s) {
    string tmp;
    for (string::iterator si = s.begin(); si != s.end(); si++) {
        tmp.append(encode_table[*si]);
    }
//    cout << tmp << endl;

    string ret;
    while (true) {
        bool found = false;
        for (int i = 3; i <= 9; i++) {
            if (decode_table[tmp.substr(0, i)] != 0) {
                ret.push_back(decode_table[tmp.substr(0, i)]);
                tmp = tmp.substr(i);
                found = true;
                break;
            }
        }
        if (!found) break;
    }
    return ret;
}

void init() {
    decode_table["101"] =       ' '   ;
    decode_table["000000"] =    '\''  ;
    decode_table["000011"] =    ','   ;
    decode_table["10010001"] =  '-'   ;
    decode_table["010001"] =    '.'   ;
    decode_table["000001"] =    '?'   ;
    decode_table["100101"] =    'A'   ;
    decode_table["10011010"] =  'B'   ;
    decode_table["0101"] =      'C'   ;
    decode_table["0001"] =      'D'   ;
    decode_table["110"] =       'E'   ;
    decode_table["01001"] =     'F'   ;
    decode_table["10011011"] =  'G'   ;
    decode_table["010000"] =    'H'   ;
    decode_table["0111"] =      'I'   ;
    decode_table["10011000"] =  'J'   ;
    decode_table["0110"] =      'K'   ;
    decode_table["00100"] =     'L'   ;
    decode_table["10011001"] =  'M'   ;
    decode_table["10011110"] =  'N'   ;
    decode_table["00101"] =     'O'   ;
    decode_table["111"] =       'P'   ;
    decode_table["10011111"] =  'Q'   ;
    decode_table["1000"] =      'R'   ;
    decode_table["00110"] =     'S'   ;
    decode_table["00111"] =     'T'   ;
    decode_table["10011100"] =  'U'   ;
    decode_table["10011101"] =  'V'   ;
    decode_table["000010"]   =  'W'   ;
    decode_table["10010010"] =  'X'   ;
    decode_table["10010011"] =  'Y'   ;
    decode_table["10010000"] =  'Z'   ;
	encode_table['A']  = string("00000"); 
	encode_table['B']  = string("00001"); 
	encode_table['C']  = string("00010"); 
	encode_table['D']  = string("00011"); 
	encode_table['E']  = string("00100"); 
	encode_table['F']  = string("00101"); 
	encode_table['G']  = string("00110"); 
	encode_table['H']  = string("00111"); 
    encode_table['I']  = string("01000"); 
    encode_table['J']  = string("01001"); 
    encode_table['K']  = string("01010"); 
    encode_table['L']  = string("01011"); 
    encode_table['M']  = string("01100"); 
    encode_table['N']  = string("01101"); 
    encode_table['O']  = string("01110"); 
    encode_table['P']  = string("01111"); 
	encode_table['Q']  = string("10000"); 
	encode_table['R']  = string("10001"); 
	encode_table['S']  = string("10010"); 
	encode_table['T']  = string("10011"); 
	encode_table['U']  = string("10100"); 
	encode_table['V']  = string("10101"); 
	encode_table['W']  = string("10110"); 
	encode_table['X']  = string("10111"); 
	encode_table['Y']  = string("11000"); 
	encode_table['Z']  = string("11001"); 
	encode_table[' ']  = string("11010"); 
	encode_table['.']  = string("11011"); 
	encode_table[',']  = string("11100"); 
	encode_table['-']  = string("11101"); 
	encode_table['\'']  = string("11110");
	encode_table['?']  = string("11111"); 
}  

int main() {
    string s;
    init();
    while (getline(cin, s)) {
        cout << encode(s) << endl;
    }
    return 0;
}