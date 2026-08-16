import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
public class Main {
	static char[][] map = new char[8][8];
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		while(true) {
			int n = stdIn.nextInt();
			if(n == 0) break;
			char[][] list = new char[n][];
			for(int i = 0; i < n; i++) {
				list[i] = stdIn.next().toCharArray();
			}
			for(int i = 0; i < n; i++) {
				for(int j = 1; j < list[i].length; j++) {
					if(list[i][j] != '.' && list[i][j-1] == '.') {
						for(int k = 0; k < j-1; k++) {
							list[i][k] = ' ';
						}
						list[i][j-1] = '+';
						for(int k = i-1; k >= 0; k--) {
							if(j-1 < list[k].length && list[k][j-1] == ' ') {
								list[k][j-1] = '|';
								continue;
							}
							else {
								break;
							}
						}
						break;
					}
				}
			}
			
			for(int i = 0; i < n; i++) {
				System.out.println(list[i]);
			}

		}
	}
	static char[] retS(char a, int b) {
		char[] tmp = new char[b];
		for(int i = 0; i < b; i++) {
			tmp[i] = ' ';
		}
		return tmp;
	}
}