import java.util.*;
public class Main{
	static long y=1;
	static long l=1;
	static Scanner cs=new Scanner(System.in);
	public static void main(String args[]){
		while(true){
			int n=cs.nextInt();
			if (n==0)break;
			long x=cs.nextLong();
			y=cs.nextLong();
			l=1;
			for(int i=0;i<n;i++){
				l=l*2;
			}
			x=l-x+1;
			System.out.println(solve(l,x));
			}
	}
	static String solve(long h,long x){
		String res="";
		if (h==1)return("");
		if (x<=h/2) {
			res=solve(h/2,x);
			if (y<=l/2){
				res=res+"R";
				l=l/2;
			}
			else {
				res=res+"L";
				y=y-l/2;
				l=l/2;
			}
		}else{
			res=solve(h/2,h-x+1);
			if (y<=l/2){
				res=res+"L";
				y=l/2-y+1;
				l=l/2;
			}
			else {
				res=res+"R";
				y=l-y+1;
				l=l/2;
			}
		}
		return(res);
	}
}
