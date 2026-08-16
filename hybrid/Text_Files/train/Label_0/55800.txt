import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int Case = 1;
		
		int t = scan.nextInt();
		
		while(t-- != 0){
			System.out.println("Case " + Case++ + ":");
			
			int x = scan.nextInt();
			x *= x;
			
			for(int i = 0; i < 10; i++){
				String s = x + "";
				while(s.length() < 8)s = "0" + s;
				x = Integer.parseInt(s.substring(2,6));
				System.out.println(x);
				x *= x;
			}
		}
	}
}