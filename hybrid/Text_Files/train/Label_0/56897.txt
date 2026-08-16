import java.util.*;
public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			int m = sc.nextInt();
			if(n == 0){
				return;
			}		
			int[] max = new int[m];
			for(int i = 0;i < n;i++){
				int d = sc.nextInt()-1;
				int v = sc.nextInt();
				max[d] = Math.max(v,max[d]);
			}
			int ans = 0;
			for(int i = 0;i < m;i++){
				ans += max[i];	
			}
			System.out.println(ans);
		}
	}
}

