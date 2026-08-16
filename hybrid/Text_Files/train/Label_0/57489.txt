
import java.util.Scanner;

public class Main {

	static int p,q,n,a,ans;;
	static double pq;
	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while(true){
			p=cin.nextInt();
			q=cin.nextInt();
			a=cin.nextInt();
			n=cin.nextInt();
			if(p+q+a+n==0){
				break;
			}
			ans=0;
			pq = (double)p/(double)q;
			for(double i = 1;i<a;i++){
				a(1.0/i,(int)i,(int)i,1);
			}
			System.out.println(ans);
		}
	}
	static void a(double d,int e,int f,int count){
		//System.out.println(d+" " + e+" " +count);
		if(count>n){
			//System.out.println("return count");
			return;
		}
		if(sameDouble(pq,d)){
			ans++;
			//System.out.println("answer "+d+" " + e+" " +count);
			return;
		}
		else if(d>pq){
			//System.out.println("return "+d+" " + e+" " +count);
			return;
		}
		for(int i = f;i*e<=a;i++){
			a(1.0/(double)i+d,i*e,i,count+1);
		}
	}
	static boolean sameDouble(double a,double b){
		double c = 0.0000000001;
		return b<a+c&&a-c<b;
	}
}