import java.util.*;

class Main{
	static Scanner s=new Scanner(System.in);
	
	static int a,b,c;
	static int[]v=new int[11];
	
	static int f(int d,int m) {
		//System.out.println(d+" "+m);
		if(m<0)
			return 0;
		if(d==b+1)
			return m==0?1:0;
		int sum=0;
		for(v[d]=v[d-1]+1;v[d]<=a;++v[d]) {
			sum+=f(d+1,m-v[d]);
		}
		return sum;
	}
	
	public static void main(String[] $){
		while(true) {
			a=s.nextInt();
			if(a==0)return;
			b=s.nextInt();
			c=s.nextInt();
			
			System.out.println(f(1,c));
		}
	}
}
