import java.util.*;
import java.io.*;
import java.awt.Point;
import java.math.BigInteger;

public class polygon {

	public static void main(String[] args) throws Exception {
		FastIO sc = new FastIO(System.in);
		PrintWriter pw = new PrintWriter(System.out);
		
		int N = sc.nextInt();
		
		TreeMap<Integer, ArrayList<Point>> byX = new TreeMap<Integer, ArrayList<Point>>();
		TreeMap<Integer, ArrayList<Point>> byY = new TreeMap<Integer, ArrayList<Point>>();
		
		Point[] points = new Point[N];
		
		for(int i = 0; i < N; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			if(!byX.containsKey(a)) byX.put(a, new ArrayList<Point>());
			if(!byY.containsKey(b)) byY.put(b, new ArrayList<Point>());
			
			Point p = new Point(a, b);
			points[i] = p;
			
			byX.get(a).add(p);
			byY.get(b).add(p);
		}
		
		long bigArea = 2* (((long) (byX.lastKey()) - (long) (byX.firstKey())) + ((long) (byY.lastKey()) - (long) (byY.firstKey())));
		
		long bigThree = 0;
		
		ArrayList<Point> lowestX = byX.get(byX.firstKey());
		ArrayList<Point> highestX = byX.get(byX.lastKey());
		
		ArrayList<Point> lowestY = byY.get(byY.firstKey());
		ArrayList<Point> highestY = byY.get(byY.lastKey());
		
		HashSet<Point> all = new HashSet<Point>();
		all.addAll(lowestX);
		all.addAll(lowestY);
		all.addAll(highestX);
		all.addAll(highestY);
		
		Point[] allPoints = all.toArray(new Point[0]);
		
		for(int i = 0; i < allPoints.length-1; i++) {
			Point a = allPoints[i];
			for(int j = i+1; j < allPoints.length; j++) {
				Point b = allPoints[j];
				
				for(int k = 0; k < points.length; k++) {
					if(points[k].equals(a)) continue;
					if(points[k].equals(b)) continue;
					
					bigThree = Math.max(bigThree, areaThree(a, b, points[k]));
				}
				
			}
		}
		
		pw.print(bigThree);
		for(int i = 4; i <= N; i++) {
			pw.print(" ");
			pw.print(bigArea);
		}
		pw.println();
		
		pw.close();
		
	}
	
	
	
	static long areaThree(Point a, Point b, Point c) {
		long maxX = max(a.x, b.x, c.x);
		long maxY = max(a.y, b.y, c.y);
		long minX = min(a.x, b.x, c.x);
		long minY = min(a.y, b.y, c.y);
		
		return 2* ((maxX - minX) + (maxY - minY));
	}
	
	static int max(int a, int b, int c) {
		return Math.max(a, Math.max(b, c));
	}
	
	static int min(int a, int b, int c) {
		return Math.min(a, Math.min(b, c));
	}

	static class FastIO {

		//Is your Fast I/O being bad?

		InputStream dis;
		byte[] buffer = new byte[1 << 17];
		int pointer = 0;

		public FastIO(String fileName) throws Exception {
			dis = new FileInputStream(fileName);
		}

		public FastIO(InputStream is) throws Exception {
			dis = is;
		}

		int nextInt() throws Exception {
			int ret = 0;

			byte b;
			do {
				b = nextByte();
			} while (b <= ' ');
			boolean negative = false;
			if (b == '-') {
				negative = true;
				b = nextByte();
			}
			while (b >= '0' && b <= '9') {
				ret = 10 * ret + b - '0';
				b = nextByte();
			}

			return (negative) ? -ret : ret;
		}

		long nextLong() throws Exception {
			long ret = 0;

			byte b;
			do {
				b = nextByte();
			} while (b <= ' ');
			boolean negative = false;
			if (b == '-') {
				negative = true;
				b = nextByte();
			}
			while (b >= '0' && b <= '9') {
				ret = 10 * ret + b - '0';
				b = nextByte();
			}

			return (negative) ? -ret : ret;
		}

		byte nextByte() throws Exception {
			if (pointer == buffer.length) {
				dis.read(buffer, 0, buffer.length);
				pointer = 0;
			}
			return buffer[pointer++];
		}

		String next() throws Exception {
			StringBuffer ret = new StringBuffer();

			byte b;
			do {
				b = nextByte();
			} while (b <= ' ');
			while (b > ' ') {
				ret.appendCodePoint(b);
				b = nextByte();
			}

			return ret.toString();
		}

	}
}
