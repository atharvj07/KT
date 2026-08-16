import java.awt.geom.Point2D;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.io.Reader;
import java.io.StringReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Scanner;

public class Main {
	static int n;
	
	static ArrayList<Point2D.Double> xy1, xy2;
	
	private static double cross(Point2D.Double a, Point2D.Double b)
	{
		return (a.x * b.y - a.y * b.x);
	}
	
	// a + b
	private static Point2D.Double add(Point2D.Double a, Point2D.Double b)
	{
		return new Point2D.Double(a.x + b.x, a.y + b.y); 
	}
	
	// a - b
	private static Point2D.Double sub(Point2D.Double a, Point2D.Double b)
	{
		return new Point2D.Double(a.x - b.x, a.y - b.y); 
	}
	
	// a * t
	private static Point2D.Double mul(Point2D.Double a, double t)
	{
		return new Point2D.Double(a.x * t, a.y * t);
	}
	
	private static Boolean isCrossing(Point2D.Double a1, Point2D.Double a2, Point2D.Double b1, Point2D.Double b2)
	{
		return (cross(sub(a2, a1), sub(b1, a1)) * cross(sub(a2, a1), sub(b2, a1)) < 1e-10) &&
			   (cross(sub(b2, b1), sub(a1, b1)) * cross(sub(b2, b1), sub(a2, b1)) < 1e-10);
	}
	
	private static Point2D.Double crosspoint(Point2D.Double a1, Point2D.Double a2, Point2D.Double b1, Point2D.Double b2)
	{
		Point2D.Double b = sub(b2, b1);
		double d1 = Math.abs(cross(b, sub(a1, b1)));
		double d2 = Math.abs(cross(b, sub(a2, b1)));
		double t = d1 / (d1 + d2);
		
		return add(a1, mul(sub(a2, a1), t));
	}
	
	public static void main(String[] args)
	{
		Scanner sca = new Scanner(System.in);
		
		while(true)
		{
			n = sca.nextInt();
			if(n == 0) break;
			
			int i, j, k;
			
			xy1 = new ArrayList<Point2D.Double>();
			xy2 = new ArrayList<Point2D.Double>();
			
			for(i = 0;i < n;i++)
			{
				double x1 = sca.nextDouble();
				double y1 = sca.nextDouble();
				double x2 = sca.nextDouble();
				double y2 = sca.nextDouble();
				
				Point2D.Double p;
				
				p = new Point2D.Double(x1, y1);
				xy1.add(p);
				p = new Point2D.Double(x2, y2);
				xy2.add(p);
			}
			
			int area = 2;
			for(i = 1;i < n;i++)
			{
				ArrayList<Point2D.Double> store = new ArrayList<Point2D.Double>();
				Point2D.Double a1 = xy1.get(i);
				Point2D.Double a2 = xy2.get(i);
				
				for(j = 0;j < i;j++)
				{
					Point2D.Double b1 = xy1.get(j);
					Point2D.Double b2 = xy2.get(j);
					
					if(!isCrossing(a1, a2, b1, b2)) continue;
					
					Point2D.Double cross = crosspoint(a1, a2, b1, b2);
					
					// 正方形の辺上にあるときcontinue
					double dx = Math.abs(Math.abs(cross.x) - 100);
					double dy = Math.abs(Math.abs(cross.y) - 100);
					if(dx < 1e-10 || dy < 1e-10) continue;
					
					// 今までの点で一致しているものが無いか探す
					for(k = 0;k < store.size();k++)
					{
						Point2D.Double sp = store.get(k);
						dx = Math.abs(sp.x - cross.x);
						dy = Math.abs(sp.y - cross.y);
						if(dx < 1e-10 && dy < 1e-10) break;
					}
					if(k == store.size())
					{
						store.add(cross);
					}
				}
				
				area += store.size() + 1;
			}
			
			System.out.println(area);
		}
	}
}