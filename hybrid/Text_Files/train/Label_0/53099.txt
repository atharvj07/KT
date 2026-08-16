import java.io.IOException;
import java.io.InputStream;
import java.util.NoSuchElementException;

public class Main {
	private static FastScanner sc = new FastScanner();

	public static void main(String[] args) {
		int q = sc.nextInt();
		StringBuilder ans = new StringBuilder();
		for(int i=0; i<q; i++) {
			double mind = Double.MAX_VALUE;
			Point p1 = new Point(sc.nextDouble(), sc.nextDouble());
			Point p2 = new Point(sc.nextDouble(), sc.nextDouble());
			Point p3 = new Point(sc.nextDouble(), sc.nextDouble());
			Point p4 = new Point(sc.nextDouble(), sc.nextDouble());
			
			if(checkCross(p1, p2, p3, p4)) {
				ans.append(0);
				ans.append("\n");
				continue;
			}
			
			Point per1 = perpLine(p1, p2, p3);
			if(per1.x >= Math.min(p1.x, p2.x) && per1.x <= Math.max(p1.x, p2.x)
					&& per1.y >= Math.min(p1.y, p2.y) && per1.y <= Math.max(p1.y, p2.y)) {
				if(distance(per1, p3) < mind) {
					mind = distance(per1, p3);
				}
			} else {
				if(distance(p1, p3) < mind) {
					mind = distance(p1, p3);
				}
				if(distance(p2, p3) < mind) {
					mind = distance(p2, p3);
				}
			}
			
			Point per2 = perpLine(p1, p2, p4);
			if(per2.x >= Math.min(p1.x, p2.x) && per2.x <= Math.max(p1.x, p2.x)
					&& per2.y >= Math.min(p1.y, p2.y) && per2.y <= Math.max(p1.y, p2.y)) {
				if(distance(per2, p4) < mind) {
					mind = distance(per2, p4);
				}
			} else {
				if(distance(p1, p4) < mind) {
					mind = distance(p1, p4);
				}
				if(distance(p2, p4) < mind) {
					mind = distance(p2, p4);
				}
			}
			
			Point per3 = perpLine(p3, p4, p1);
			if(per3.x >= Math.min(p3.x, p4.x) && per3.x <= Math.max(p3.x, p4.x)
					&& per3.y >= Math.min(p3.y, p4.y) && per3.y <= Math.max(p3.y, p4.y)) {
				if(distance(per3, p1) < mind) {
					mind = distance(per3, p1);
				}
			} else {
				if(distance(p1, p3) < mind) {
					mind = distance(p1, p3);
				}
				if(distance(p1, p4) < mind) {
					mind = distance(p1, p4);
				}
			}
			
			Point per4 = perpLine(p3, p4, p2);
			if(per4.x >= Math.min(p3.x, p4.x) && per4.x <= Math.max(p3.x, p4.x)
					&& per4.y >= Math.min(p3.y, p4.y) && per4.y <= Math.max(p3.y, p4.y)) {
				if(distance(per4, p2) < mind) {
					mind = distance(per4, p2);
				}
			} else {
				if(distance(p2, p3) < mind) {
					mind = distance(p2, p3);
				}
				if(distance(p2, p4) < mind) {
					mind = distance(p2, p4);
				}
			}
			
			ans.append(mind);
			ans.append("\n");
		}
		System.out.print(ans);
	}
	
	static Point perpLine(Point p1, Point p2, Point p) {
		double a = (p2.y - p1.y) / (p2.x - p1.x);
		double b = p1.y - a * p1.x;
		double x = 0;
		double y = 0;
		if(p1.y == p2.y) {
			x = p.x;
			y = p1.y;
		} else if(p1.x == p2.x) {
			x = p1.x;
			y = p.y;
		} else {
			x = (p.y + p.x / a - b) / (a + 1 / a);
			y = p.y + p.x / a - x / a;
		}
		
		return new Point(x, y);
	}
	
	static double distance(Point p1, Point p2) {
		return Math.sqrt((p2.x-p1.x)*(p2.x-p1.x) + (p2.y-p1.y)*(p2.y-p1.y));
	}
	
	static boolean checkCross(Point p1, Point p2, Point p3, Point p4) {
		if(p1.x >= p2.x) {
			if((p1.x<p3.x && p1.x<p4.x) || (p2.x>p3.x && p2.x>p4.x)) {
				return false;
			}
		} else {
			if((p2.x<p3.x && p2.x<p4.x) || (p1.x>p3.x && p1.x>p4.x)) {
				return false;
			}
		}
		
		if(p1.y >= p2.y) {
			if((p1.y<p3.y && p1.y<p4.y) || (p2.y>p3.y && p2.y>p4.y)) {
				return false;
			}
		} else {
			if((p2.y<p3.y && p2.y<p4.y) || (p1.y>p3.y && p1.y>p4.y)) {
				return false;
			}
		}
		
		if(((p1.x-p2.x)*(p3.y-p1.y)+(p1.y-p2.y)*(p1.x-p3.x))*((p1.x-p2.x)*(p4.y-p1.y)+(p1.y-p2.y)*(p1.x-p4.x))>0) {
			return false;
		}
		if(((p3.x-p4.x)*(p1.y-p3.y)+(p3.y-p4.y)*(p3.x-p1.x))*((p3.x-p4.x)*(p2.y-p3.y)+(p3.y-p4.y)*(p3.x-p2.x))>0) {
			return false;
		}
		
		return true;
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