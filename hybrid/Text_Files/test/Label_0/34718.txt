import java.util.Scanner;
public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int w = sc.nextInt();
		int h = sc.nextInt();
		int n = sc.nextInt();
		
		int wmin = 0;
		int wmax = w;
		int hmin = 0;
		int hmax = h;
		
		for(int i = 0; i < n ;i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			int a = sc.nextInt();
			
			if(a == 1) {
				wmin = Math.max(wmin, x);
			}
			if(a == 2) {
				wmax = Math.min(wmax, x);
			}
			if(a == 3){
				hmin = Math.max(hmin, y);
			}
			if(a == 4) {
				hmax = Math.min(hmax, y);
			}
			
		}
		
		if(wmax <= wmin || hmax <=hmin) {
			System.out.println(0);
		}
		else {
			System.out.println((wmax-wmin)*(hmax - hmin));
		}
	}
}
