import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		int n = stdIn.nextInt();
		int []h = new int[n];
		
		for(int i = 0; i < n; i++) {
			h[i] = stdIn.nextInt();
		}
		
		int cnt = 0;
		int max = 0;
		
		
		for(int i = 0; i < n-1; i++) {
			if(h[i]>= h[i+1]) {
				cnt++;
				max = Math.max(cnt, max);
			}else {
				cnt = 0;
			}
		}
		
		System.out.println(max);
	}
	
	
	
	
	
}
