
import java.util.Scanner;
public class Main {
		
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		for(int i = 0; i < 3; i++) {
			int s1 = 0;
			int s2 = 0;
			
			s1 += stdIn.nextInt() * 3600;
			s1 += stdIn.nextInt() * 60;
			s1 += stdIn.nextInt();
			
			s2 += stdIn.nextInt() * 3600;
			s2 += stdIn.nextInt() * 60;
			s2 += stdIn.nextInt();
			
			s1 = s2 - s1;
			
			int h = s1 / 3600;
			s1 -= h*3600;
			int m = s1 / 60;
			s1 -= m*60;
			
			System.out.println(h + " " + m + " " + s1);
			
			
		}
		
		
		
	}
}