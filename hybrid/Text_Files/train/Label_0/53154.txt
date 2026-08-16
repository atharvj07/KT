import java.util.Scanner;


public class Main {
	
	final int ny = 19*5+20*5;
	final int sy = 20*10;
	
	final long mill = tonum(1000, 1, 1);
	
	long ytod(int y) {
		y = y-1;
		int last = y%3;
		return (y/3)*(ny+ny+sy) + last * ny;
	}
	
	long mtod(int y, int m) {
		m = m-1;
		if(y % 3 == 0) {
			return m * 20;
		} else {
			int mm = m/2;
			return (m-mm) * 20 + mm * 19;
		}
	}
	
	long tonum(int y, int m, int d) {
		return ytod(y) + mtod(y,m) + d-1;
	}
	
	long solve(int y, int m, int d) {
		return mill - tonum(y,m,d);
	}
	
	public Main() {
		Scanner scanner = new Scanner(System.in);
		
		while(scanner.hasNext()) {
			int n = scanner.nextInt();
			for(int i=0; i<n; i++) {
				int y = scanner.nextInt();
				int m = scanner.nextInt();
				int d = scanner.nextInt();
				System.out.println(solve(y,m,d));
			}
		}
		
		scanner.close();
	}
	
	public static void main(String[] args) {
		new Main();
	}

}