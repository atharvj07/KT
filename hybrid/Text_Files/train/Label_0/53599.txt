import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] a = new int[2];
		int[] b = new int[2];
		int[] c = new int[2];
		int[] d = new int[2];
		
		double x, y;
		while(sc.hasNext()){
			x = sc.nextDouble();
			y = sc.nextDouble();
			
			if(x>=1.1) a[0]++;
			else if(x>=0.6) b[0]++;
			else if(x>=0.2) c[0]++;
			else d[0]++;
			
			if(y>=1.1) a[1]++;
			else if(y>=0.6) b[1]++;
			else if(y>=0.2) c[1]++;
			else d[1]++;
		}
		
		System.out.println(a[0] + " " + a[1]);
		System.out.println(b[0] + " " + b[1]);
		System.out.println(c[0] + " " + c[1]);
		System.out.println(d[0] + " " + d[1]);
	}	
}