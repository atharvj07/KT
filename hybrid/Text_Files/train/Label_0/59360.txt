import java.util.Scanner;
public class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int theta = 90;
		double x = 0;
		double y = 0;
		int a = 0;
		int b = 0;
		while(scan.hasNext()){
			String[] str = scan.nextLine().split(",");
			a = Integer.parseInt(str[0]);
			b = Integer.parseInt(str[1]);
			if(a == 0 && b == 0){
				break;
			}
			x += (double)a * Math.cos((double)theta/180*Math.PI);
			y += (double)a * Math.sin((double)theta/180*Math.PI);
			theta -= b;
		}
		System.out.println((int)x + "\n" + (int)y);
	}
}