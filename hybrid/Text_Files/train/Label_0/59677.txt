import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			int n = sc.nextInt();
			if(n==0) break;
			
			int[] a = new int[n];
			for(int i=0;i<n;i++) a[i] = sc.nextInt();
			Arrays.sort(a);
			
			int[] b = new int[n];
			int c;
			for(int i=0;i<n;i++){
				c = sc.nextInt();
				for(int j=0;j<c;j++) b[j]++;
			}
			
			c = 0;
			for(int i=0;i<n;i++){
				if(a[i]!=b[n-1-i]){
					c = 1;
					break;
				}
			}
			
			if(c==0) System.out.println("Yes");
			else System.out.println("No");
		}	
	}	
}