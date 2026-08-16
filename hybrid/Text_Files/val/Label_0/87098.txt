import java.util.Scanner;

class Main {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		
		int q;
		double x0, y0, x1, y1, x2, y2, x3, y3;
		boolean flag;
		
		q = scan.nextInt();
		
		for(int i = 0; i < q; i++) {
			flag = false;
			
			x0 = scan.nextDouble();
			y0 = scan.nextDouble();
			x1 = scan.nextDouble();
			y1 = scan.nextDouble();
			x2 = scan.nextDouble();
			y2 = scan.nextDouble();
			x3 = scan.nextDouble();
			y3 = scan.nextDouble();
			
			if( ((y0 - y1) * (x2 - x0) - (x0 - x1) * (y2 - y0)) * 
				((y0 - y1) * (x3 - x0) - (x0 - x1) * (y3 - y0)) == 0
				&&
				((y2 - y3) * (x0 - x2) - (x2 - x3) * (y0 - y2)) *
				((y2 - y3) * (x1 - x2) - (x2 - x3) * (y1 - y2)) == 0) {
				
				if(x0 > x1) {
					double tmp = x0;
					x0 = x1;
					x1 = tmp;
				}
				if(y0 > y1) {
					double tmp = y0;
					y0 = x1;
					y1 = tmp;
				}
				
				if((x0 > x2 && x0 > x3) || (x1 < x2 && x1 < x3)) {
					System.out.println(0);
					
				} else if((y0 > y2 && y0 > y3) || (y1 < y2 && y1 < y3)) {
					System.out.println(0);
					
				} else {
					System.out.println(1);
					
				}
					
			} else if( ((y0 - y1) * (x2 - x0) - (x0 - x1) * (y2 - y0)) * 
				((y0 - y1) * (x3 - x0) - (x0 - x1) * (y3 - y0)) <= 0
				&&
				((y2 - y3) * (x0 - x2) - (x2 - x3) * (y0 - y2)) *
				((y2 - y3) * (x1 - x2) - (x2 - x3) * (y1 - y2)) <= 0) {
				System.out.println(1);
				
			} else {
				
				System.out.println(0);
			}
		}
		
		scan.close();
	}
}