import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			int n = sc.nextInt();
			if(n==0)break;
			int[] p = new int[n];
			int sum = 0;
			for(int i=0;i<n;i++){
				p[i] = sc.nextInt();
				sum += p[i];
			}
			Arrays.sort(p);
			sum = (sum-p[0]-p[n-1])/(n-2);
			System.out.println(sum);
		}
	}	
}