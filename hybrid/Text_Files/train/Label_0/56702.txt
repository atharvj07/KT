import java.util.*;
class Main{
	static int n;
	static int count;
	static String str;
	static boolean R;
	static void solve(int a,int b){
	//	System.out.println(a+" "+b);
		int now=0;
		for(int i=a;i<=b;i++){
			if('0'<=str.charAt(i)&&str.charAt(i)<='9'){
				now*=10;
				now+=(int)(str.charAt(i)-'0');
			}else if(str.charAt(i)=='('){
				if(now==0)now=1;
				int K=1;
				int j;
				for(j=i+1;j<=b;j++){
					if(str.charAt(j)=='(')K++;
					if(str.charAt(j)==')')K--;
					if(K==0)break;
				}
				for(int k=0;k<now;k++){
					solve(i+1,j-1);
					if(R)return ;
				}
				i=j;
				now=0;
			}else{
				if(now==0)now=1;
				for(int j=0;j<now;j++){
					if(count==n){
						System.out.println(str.charAt(i));
						R=true;
						return;
					}
					count++;
				}
				now=0;
			}
		}
	}
	public static void main(String[] args){
		Scanner s=new Scanner(System.in);
		while(true){
			str=s.next();
			int a=s.nextInt();
			n=a;
			count=0;
			R=false;
			if(str.equals("0"))break;
			solve(0,str.length()-1);
			if(!R)System.out.println("0");
		}
	}
}