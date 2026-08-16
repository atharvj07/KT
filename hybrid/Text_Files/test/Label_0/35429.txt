import java.io.*;
import java.util.*;
import java.math.*;

public class D{
	
	static Scanner in;
	static PrintWriter out;
	
	static int n, k, posOffice;
	static int[] posP, posK;
	
	public static void main(String args[]) throws Exception{
		
		in = new Scanner(System.in);
		out = new PrintWriter(System.out);
		
		input();
		solve();
		
		out.close();
	}
	
	static void input(){
		n = in.nextInt();
		k = in.nextInt();
		posOffice = in.nextInt();
		posP = new int[1005];
		posK = new int[2005];
		for (int i = 1; i <= n; i++){
			posP[i] = in.nextInt();
		}
		Arrays.sort(posP, 1, n + 1);
		
		for (int i = 1; i <= k; i++){
			posK[i] = in.nextInt();
		}
		Arrays.sort(posK, 1, k + 1);
	}
	
	static void solve(){
		long left = -1, right = 2000000007;
		while (right - left > 1){
			long mid = (left + right) / 2;
			if (isFeasible(mid)){
				right = mid;
			}
			else{
				left = mid;
			}
		}
		out.println(right);
	}
	
	static boolean isFeasible(long time){
		int ptr = 1;
		for (int i = 1; i <= n; i++){
			while (ptr <= k && Math.abs(posP[i] - posK[ptr]) + Math.abs(posK[ptr] - posOffice) > time){
				ptr++;
			}
			if (ptr > k) return false;
			else ptr++;
		}
		return true;
	}
}