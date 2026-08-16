import java.awt.*;
import java.awt.geom.*;
import java.io.*;
import java.util.*;
class Main {
	
	static int[][] map;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char[] S = sc.next().toCharArray();
		char[] T = Arrays.copyOf(S, S.length);
		
		
		
		for(int i = 0; i < S.length-7; i++) {
			int[] check = new int[8];
			for(int j = 0; j < 8; j++) {
				switch(S[i + j]) {
				case 'A':check[0]++; break;
				case 'I':check[1]++; break;
				case 'D':check[2]++; break;
				case 'U':check[3]++; break;
				case 'N':check[4]++; break;
				case 'Y':check[5]++; break;
				}
			}
			if(check[0] == 2 && check[1] == 1 && check[2] == 1 && check[3] == 1 && check[4] == 2 && check[5] == 1) {
				T[i] = 'A';
				T[i+1] = 'I';
				T[i+2] = 'Z';
				T[i+3] = 'U';
				T[i+4] = 'N';
				T[i+5] = 'Y';
				T[i+6] = 'A';
				T[i+7] = 'N';
			}
		}
		
		System.out.println(String.valueOf(T));
		
		
		
	}
 	
}