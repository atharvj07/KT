import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		for(int i=0;i<t;i++){
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int x2 = sc.nextInt() + x1;
			int y2 = sc.nextInt() + y1;
			
			int n = sc.nextInt();
			int count = 0;
			int x, y;
			for(int j=0;j<n;j++){
				x = sc.nextInt();
				y = sc.nextInt();
				if(x1<=x && x<=x2 && y1<=y && y<=y2) count++;
			}
			System.out.println(count);
		}
	}	
}