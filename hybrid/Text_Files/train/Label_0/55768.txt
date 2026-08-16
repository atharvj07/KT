import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.PriorityQueue;
 
public class Main {
	private static FastScanner sc = new FastScanner();
	static City[] c;
	
	public static void main(String[] args) {
		int N = sc.nextInt();
		
		c = new City[N];
		for(int i=0; i<N; i++) {
			c[i] = new City(sc.nextInt(), sc.nextInt(), i);
		}
		
		PriorityQueue<Road> r = new PriorityQueue<>((a, b) -> a.cost - b.cost);
		
		City[] ca = c.clone();
		
		Arrays.sort(ca, (a, b) -> a.x - b.x);
		for(int i=0; i<N-1; i++) {
			r.add(new Road(ca[i+1].x - ca[i].x, ca[i].id, ca[i+1].id));
		}
		
		Arrays.sort(ca, (a, b) -> a.y - b.y);
		for(int i=0; i<N-1; i++) {
			r.add(new Road(ca[i+1].y - ca[i].y, ca[i].id, ca[i+1].id));
		}
		
		long ans = 0;
		while(!r.isEmpty()) {
			Road road = r.poll();
			int p1 = c[road.id1].findParent();
			int p2 = c[road.id2].findParent();
			
			if(p1 != p2) {
				c[p2].parent = p1;
				ans += road.cost;
//				System.out.println(p1 + " " + p2 + " " + ans);
			}
		}
		
		System.out.println(ans);
	}
	
	static class City {
		int id;
		int x;
		int y;
		int parent = -1;
		
		City(int x, int y, int id) {
			this.x = x;
			this.y = y;
			this.id = id;
		}
		
		public int findParent() {
			if(parent == -1) {
				return id;
			}
			int p = c[parent].findParent();
			parent = p;
			return p;
		}
	}

	static class Road {
		int cost;
		int id1;
		int id2;
		
		Road(int cost, int id1, int id2) {
			this.cost = cost;
			this.id1 = id1;
			this.id2 = id2;
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