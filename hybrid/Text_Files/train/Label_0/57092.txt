import java.util.*;

class Main {

	private static int ans[] = new int[1000];
	private static int pos;

	public static void main(String args[]){
		Scanner in = new Scanner(System.in);
		for(;;){
			int n = in.nextInt();
			if(n==0) return ;
			rec(n,n);
		}
	}
	
	private static void rec(int res, int ub){
		if(res ==0){
			for(int i=0; ; i++){
				System.out.print(ans[i] + ((ans[i+1]>0)?" ":"\n"));
				if(ans[i+1]==0) return ;
			}
		}
		for(int i=Math.min(res, ub); i>=1; i--){
			ans[pos] = i;
			pos++;
			rec(res-i, i);
			pos--;
			ans[pos] = 0;
		}
		return ;
	}
}