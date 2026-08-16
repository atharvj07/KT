import java.util.Scanner;

//Area of Polygon
public class Main{

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n==0)break;
			double sa = 0;
			int s = 360;
			while(--n!=0){
				int t = sc.nextInt();
				s -= t;
				sa += Math.sin(t*Math.PI/180);
			}
			sa += Math.sin(s*Math.PI/180);
			n = sc.nextInt();
			s = 360;
			double sb = 0;
			while(--n!=0){
				int t = sc.nextInt();
				s -= t;
				sb += Math.sin(t*Math.PI/180);
			}
			sb += Math.sin(s*Math.PI/180);
			if(Math.abs(sa-sb)<1e-8)System.out.println(0);
			else System.out.println(sb<sa?1:sa<sb?2:0);
		}
	}
}