import java.util.Scanner;

class Main {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		
		double r = 6378.1;
		
		double a, b, c, d, x;
		
		while(true) {
			a = scan.nextDouble();
			b = scan.nextDouble();
			c = scan.nextDouble();
			d = scan.nextDouble();
			
			if(a == -1 && b == -1 && c == -1 && d == -1) break;

			a = a * Math.PI / 180;
			b = b * Math.PI / 180;
			c = c * Math.PI / 180;
			d = d * Math.PI / 180;
			
			double[] p1 =  {r * Math.sqrt((1 - Math.sin(a) * Math.sin(a))) * Math.sin(b),
							-r * Math.sqrt((1 - Math.sin(a) * Math.sin(a))) * Math.cos(b),
							r * Math.sin(a)};
			
			double[] p2 =  {r * Math.sqrt((1 - Math.sin(c) * Math.sin(c))) * Math.sin(d),
							-r * Math.sqrt((1 - Math.sin(c) * Math.sin(c))) * Math.cos(d),
							r * Math.sin(c)};
			
			x = Math.acos((p1[0] * p2[0] + p1[1] * p2[1] + p1[2] * p2[2]) / 
							(Math.sqrt(p1[0] *p1[0] + p1[1] * p1[1] + p1[2] * p1[2]) *
							Math.sqrt(p2[0] *p2[0] + p2[1] * p2[1] + p2[2] * p2[2])));

			System.out.println(Math.round(r * x));
		}
		scan.close();
	}
}