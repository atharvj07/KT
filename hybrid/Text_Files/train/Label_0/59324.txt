import java.io.IOException;
import java.io.InputStream;
import java.util.NoSuchElementException;

public class Main {
	private static FastScanner sc = new FastScanner();

	public static void main(String[] args) {
		int n = sc.nextInt();
		Point[] p = new Point[n];
		for(int i=0; i<n; i++) {
			p[i] = new Point(sc.nextDouble(), sc.nextDouble());
		}
		
		double maxdist = distance(p[0], p[1]);
		int j = 1;
		for(int i=2; i<n; i++) {
			double dist = distance(p[0], p[i]);
			if(dist > maxdist) {
				maxdist = dist;
				j = i;
			}
		}
		
//		System.out.println(0 + " " + j + " " + maxdist);
		
		for(int i=1; i<n; i++) {
			double maxdist2 = distance(p[i], p[j%n]);
			while(true) {
				double dist = distance(p[i], p[(j+1)%n]);
				if(dist > maxdist2) {
					maxdist2 = dist;
					j++;
				} else {
					break;
				}
			}
			
//			System.out.println(i + " " + j + " " + maxdist2);
			
			if(maxdist2 > maxdist) {
				maxdist = maxdist2;
			}
		}
		
		System.out.println(maxdist);
		
	}
	
	static double distance(Point p1, Point p2) {
		return Math.sqrt((p2.x-p1.x)*(p2.x-p1.x) + (p2.y-p1.y)*(p2.y-p1.y));
	}

	static class Point {
		double x;
		double y;
		Point(double x, double y) {
			this.x = x;
			this.y = y;
		}
	}
	
	static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1024];
        private int ptr = 0;
        private int buflen = 0;
        private boolean hasNextByte() {
            if(ptr < buflen) {
                return true;
            } else {
                ptr = 0;
                try {
                    buflen = in.read(buffer);
                } catch(IOException e) {
                    e.printStackTrace();
                }
                if(buflen <= 0) {
                    return false;
                }
            }
            return true;
        }
        private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
        private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
        private void skipUnprintable() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;}
        public boolean hasNext() { skipUnprintable(); return hasNextByte();}
        public String next() {
            if (!hasNext()) throw new NoSuchElementException();
            StringBuilder sb = new StringBuilder();
            int b = readByte();
            while(isPrintableChar(b)) {
                sb.appendCodePoint(b);
                b = readByte();
            }
            return sb.toString();
        }
        public long nextLong() {
            return Long.parseLong(next());
        }
        public int nextInt(){
            return Integer.parseInt(next());
        }
        public double nextDouble(){
            return Double.parseDouble(next());
        }
    }
}