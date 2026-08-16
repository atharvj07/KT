import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		for(int i=0;i<n;i++){
			String s = sc.next();
			double a = Double.valueOf(s.substring(0, 2));
			double b = Double.valueOf(s.substring(3, 5));
			double x = a*30 + b/2;
			double y = b*6;
			double z = Math.abs(x-y);
			if(z>180) z = 360-z;
			if(z<30) System.out.println("alert");
			else if(z>=90 && z<=180) System.out.println("safe");
			else System.out.println("warning");	
		}
	}	
}