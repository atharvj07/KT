import java.util.Scanner;

//Pi is Three
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		double EPS = 1e-10;
		for(;;){
			double R = sc.nextDouble();
			if(R==0)break;
			int n = 1, d = 1;
			double min = 1<<29;
			int an = 0, ad = 1<<29;
			while(d<=ad){
				double r = Math.PI-n*1.0/d;
				double e = Math.abs(r);
				if(e<R+EPS&&e<min){
					min = e; an = n; ad = d;
				}
				if(r<0)d++;
				else n++;
			}
			System.out.println(an+"/"+ad);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}