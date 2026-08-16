import java.util.*;
import java.io.*;
import java.math.*;

class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true) {
			int n = sc.nextInt();
			
			int m = sc.nextInt();
			if(n == 0 && m == 0) break;
			char[][] N = new char[n][8];
			int[] M = new int[n];
			for(int i = 0; i < n; i++) {
				N[i] = sc.next().toCharArray();
				M[i] = sc.nextInt();
			}
			
			char[][] B = new char[m][8];
			for(int i = 0; i < m; i++) {
				B[i] = sc.next().toCharArray();
			}
			long ans = 0;
			for(int i = 0; i < n; i++) {
				IN:for(int j = 0; j < m; j++) {
					for(int k = 0; k < 8; k++) {
						if(N[i][k] == '*') continue;
						if(N[i][k] != B[j][k]) continue IN;
					}
					ans += M[i];
				}
			}
			System.out.println(ans);
			
			
			
		}
	}
}