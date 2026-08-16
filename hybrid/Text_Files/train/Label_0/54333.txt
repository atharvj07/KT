import java.util.Scanner;

public class C {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long x = sc.nextLong();
		long y = sc.nextLong();
		long m = sc.nextLong();

		if (x <= 0 && y <= 0 && m > 0)
			System.out.println(-1);
		// else if(x>=0 && y>=0 && m<)
		else if (x >= m || y >= m)
			System.out.println(0);
		else if(x<0 && y<0 &&(m>x && m>y))
			System.out.println(-1);
		else {
			long count=0;
			
			if(x<0)
			{
				long temp=x*-1;
				long t=temp%y ==0? (temp/y) :((temp/y)+1);
				count+=t;
				x+=t*y;
			}
			else if (y<0)
			{
				long temp=y*-1;
				long t=temp%x ==0? (temp/x) :((temp/x)+1);
				count+=t;
				y+=t*x;	
			}
			while(x<m && y<m)
			{
				count++;
				if(x>y)
				{
					y=y+x;
				}else
					x=x+y;
			}
			System.out.println(count);
//			
//			if (x>0 && y>0) {
//				long remx=m-y;
//				long devx=(remx%x==0)?(remx/x): (remx/x + 1);
//				long remy=m-x;
//				long devy=(remy%y==0)?(remy/y): (remy/y +1);
//				System.out.println(Math.min(devx, devy));
//			}
//			else if(x>0)
//			{
//				long remx=m-y;
//				long devx=(remx%x==0)?(remx/x): (remx/x+1);
//				System.out.println(devx);
//			}
//			else if (y>0)
//			{
//				long remy=m-x;
//				long devy=(remy%y==0)?(remy/y): (remy/y +1);
//				System.out.println(devy);
//			}
		}
	}

}
//-1000000000000000000 1 1000000000000000000