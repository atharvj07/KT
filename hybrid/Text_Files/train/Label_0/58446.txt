import java.util.Scanner;

class Main {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		
		int q;
		double x0, y0, x1, y1, x2, y2, x3, y3;
		
		q = scan.nextInt();
		
		for(int i = 0; i < q; i++) {
			x0 = scan.nextDouble();
			y0 = scan.nextDouble();
			x1 = scan.nextDouble();
			y1 = scan.nextDouble();
			x2 = scan.nextDouble();
			y2 = scan.nextDouble();
			x3 = scan.nextDouble();
			y3 = scan.nextDouble();
			
			if(y0 == y1) {
				if(y2 == y3) {
					System.out.println(2);
					
				} else if(x2 == x3) {
					System.out.println(1);
					
				} else {
					System.out.println(0);
					
				}
			} else if(x0 == x1) {
				if(x2 == x3) {
					System.out.println(2);
					
				} else if(y2 == y3) {
					System.out.println(1);
					
				} else {
					System.out.println(0);
					
				}
			} else {				
				if(((y1 - y0) / (x1 - x0)) == ((y3 - y2) / (x3 - x2))) {
					System.out.println(2);
					
				} else if(((y1 - y0) / (x1 - x0) * (y3 - y2) / (x3 - x2)) == -1) {
					System.out.println(1);
					
				} else {
					System.out.println(0);
					
				}
			}
		}
		
		scan.close();
	}
}