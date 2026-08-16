import java.util.Arrays;
import java.util.Scanner;
import java.math.*;

class Main{
	static final int INF = 114514810;
	static int n, m;
	static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args){
		while(true){
			n = sc.nextInt();
			m = sc.nextInt();
			if(n == 0) return;
			
			solve();
		}
	}
	
	static void solve(){
		int[] point = new int[n+10];
		for(int i = 0; i < n+10; i++) point[i] = INF;
		
		for(int i = 0; i < n; i++){
			point[i] = sc.nextInt();
		}
		n++;
		point[n]=0;
		Arrays.sort(point);
		
		int[] enu = new int[n*n];
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				enu[i*n+j] = point[i]+point[j];
			}
		}
		Arrays.sort(enu);
		
		int j = n*n-1, ans=0;
		for(int i = 0; i < n*n; i++){
			while(enu[i]+enu[j] > m && j > 0) j--;
			if(enu[i]+enu[j] <= m) ans = Math.max(ans, enu[i]+enu[j]);
		}
		
		System.out.println(ans);
	}
}