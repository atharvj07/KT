import java.util.*;
public class Main {
	static Scanner sc = new Scanner(System.in);
	static int n, m;
	static int[] t;
	public static void main(String[] args) {
		while(read()){
			solve();
		}

	}
	static boolean read(){
		n = sc.nextInt(); m = sc.nextInt();
		if( n == 0 && m == 0 )return false;
		t = new int[n+m];
		for(int i = 0; i < t.length; i++){
			t[i] = sc.nextInt();
		}
		return true;
	}
	static void solve(){
		Arrays.sort(t);
		int max = t[0];
		int diff = 0;
		
		for(int i = 0; i < t.length -1; i++){
			diff = t[i+1] - t[i];
			if( diff > max)max = diff;
		}
		System.out.println(max);
	}

}