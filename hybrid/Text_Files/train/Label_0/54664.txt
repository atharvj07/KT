
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long x=sc.nextLong();
		long y=100;
		long cnt = 0;
		for(int i=0;i<2;) {
			cnt+=1;
			y=(long) (y*1.01);
			if(y>=x) {
				break;
			}
		}
		System.out.println(cnt);
	}

}
