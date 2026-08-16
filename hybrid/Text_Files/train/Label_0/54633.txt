import java.util.*;
import java.util.Map.Entry;
import java.math.*;
import java.awt.geom.*;
import java.io.*;
      
      
public class Main {	
	static char[] tank = new char[] {'^','>','v','<'};
	static int[] vx = new int[] {0,1,0,-1};
	static int[] vy = new int[] {-1,0,1,0};
	static final int INF = 2 << 28;
	static String str;
	static StringBuilder sb;
	static int ID;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int S = sc.nextInt();
		for(int TIME = 0; TIME < S; TIME++) {
			long[] N = new long[9];
			for(int i = 0; i < 9; i++) {
				N[i] = sc.nextLong(16);
			}
			long K = 0;
			for(int i = 0; i < 32; i++) {
				long cSum = 0;
				for(int j = 0; j < 8; j++) {
					cSum += N[j] ^ K;
				}
				if((cSum & 1L << i) != ((N[8] ^ K) & 1L << i)) {
					K |= 1L << i;
				}
			}
			System.out.println(Long.toHexString(K));
			
		}
		
	}
	
	
	
	
	
 }