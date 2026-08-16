import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int i=sc.nextInt();
		int x=-1;
		int max=-1;
		for (int m=0;m<i;m++) {
			for (int n=0;n<i;n++) {
				int s=sc.nextInt();
				if (s>x) {
					x=s;	
				}
			}
			if (x>max) {
				max=x;
			}else if(x==max) {
				x++;
			}
			if (i==m) {
				System.out.print(x);
				break;
			}
			System.out.print(x+" ");
			x=-1;
		}
		
	}
}