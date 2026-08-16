import java.util.*;
public class Main
{
	public static void main(String[] args) 
	{
		Scanner in=new Scanner(System.in);
		for(;;)
		{
			int n=in.nextInt();
			if(n==0)
				return;
			Point p[]=new Point[n];
			boolean exist[][]=new boolean[5001][5001];
			int max=0;
			for(int i=0;i<n;i++)
			{
				int x=in.nextInt(),y=in.nextInt();
				p[i]=new Point(x,y);
				exist[x][y]=true;
			}
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++)
				{
					if(i==j)
						continue;
					int x1=p[i].x,y1=p[i].y;
					int x2=p[j].x,y2=p[j].y;
					if(x2-y2+y1>=0&&y2+x2-x1>=0&&x1+y1-y2>=0&&y1+x2-x1>=0)
						if(x2-y2+y1<=5000&&y2+x2-x1<=5000&&x1+y1-y2<=5000&&y1+x2-x1<=5000)
							if(exist[x2-y2+y1][y2+x2-x1]&&exist[x1+y1-y2][y1+x2-x1])
								max=Math.max(max,(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
				}
			System.out.println(max);
		}
	}
	static public void debug(Object... o)
	{
		System.err.println(Arrays.deepToString(o));
	}
}
class Point
{
	int x;
	int y;
	Point(int x,int y)
	{
		this.x=x;
		this.y=y;
	}
}