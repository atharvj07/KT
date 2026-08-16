import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner scan=new Scanner(System.in);
		String str=scan.next();
		String a=str.substring(0,2);
		String b=str.substring(2,4);
		boolean YYMM=false;
		boolean MMYY=false;
		int B=Integer.parseInt(b);
		int A=Integer.parseInt(a);
		if(B>0&&B<13) {
			YYMM=true;
		}
		if(A>0&&A<13) {
			MMYY=true;
		}
		if(YYMM) {
			if(MMYY) {
				System.out.println("AMBIGUOUS");
			}
			else {
				System.out.println("YYMM");
			}
		}
		else {
			if(MMYY) {
				System.out.println("MMYY");
			}
			else {
				System.out.println("NA");
			}
		}
	}
}
