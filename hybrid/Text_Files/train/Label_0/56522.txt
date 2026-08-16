import java.util.Scanner;
public class Main {
	public static void main(String[]args) {
		Scanner s = new Scanner(System.in);
		int a1 = s.nextInt();
		int b1 = s.nextInt();
		String a = Integer.toString(a1);
		String b = Integer.toString(b1);
		
			for(int i = 0; i<b1-1;i++) {
				a += a.charAt(0);
			}
			
			for(int i = 0; i<a1-1;i++) {
				b += b.charAt(0);
			}
		
		if(a.compareTo(b)<=0) {
			System.out.println(a);
		}else System.out.println(b);
		
		
		
		
	}
}
