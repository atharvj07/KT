import java.util.Scanner;

//Speed Skating Badge Test
public class Main{

	public static void main(String[] args) {
		double[][] a = {{35.5,71},{37.5,77},{40,83},{43,89},{50,105},{55,116},{70,148}};
		String[] c = {"AAA","AA","A","B","C","D","E","NA"};
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			double x = sc.nextDouble();
			double y = sc.nextDouble();
			int k = 0;
			while(k<7){
				if(x<a[k][0]&&y<a[k][1])break;
				k++;
			}
			System.out.println(c[k]);
		}
	}
}