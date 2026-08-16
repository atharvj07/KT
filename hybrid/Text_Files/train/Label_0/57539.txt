import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int p = sc.nextInt();
		while(p-- > 0) {
			int b  = sc.nextInt(), w = sc.nextInt();
			if(Math.min(b, w)*3+1 < Math.max(b, w)) {
				System.out.println("NO");
				continue;
			}
			System.out.println("YES");
			if(b < w) {
				System.out.println("3 1");
				w--;
				for(int i = 1; i <= b; i++) {
					System.out.println("3 " + (i*2));
					if(w > b) {
						System.out.println("2 " + (i*2));
						w--;
					}
					if(w > b) {
						System.out.println("4 " + (i*2));
						w--;
					}
					System.out.println("3 " + (i*2+1));
				}
			}
			else {
				if(b > w) {
					System.out.println("2 1");
					b--;
				}
				for(int i = 1; i <= w; i++) {
					System.out.println("2 " + (i*2));
					if(w < b) {
						System.out.println("1 " + (i*2));
						b--;
					}
					if(w < b) {
						System.out.println("3 " + (i*2));
						b--;
					}
					System.out.println("2 " + (i*2+1));
				}
			}
		}
		sc.close();
	}
    
   
}