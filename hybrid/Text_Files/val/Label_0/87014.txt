import java.util.Scanner;

public class A {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String s = sc.next();
		for (int i = 0; i < n; i++) {
			for (int j = 1; j < n; j++) {
				boolean f = true;
				for(int k = 0; k < 5; k++)
					if(i + k * j < n && s.charAt(i + k * j) == '*')
						;
					else f = false;
				if(f){
					System.out.println("yes");
					System.exit(0);
				}
			}
		}
		
		System.out.println("no");
	}
}
