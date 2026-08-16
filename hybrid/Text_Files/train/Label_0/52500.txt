import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.NoSuchElementException;


public class Main {
  public static void main(String[] args) {
    FastScanner sc = new FastScanner();
    int N = sc.nextInt();
    int M = sc.nextInt();
    
    int[][] range = sc.nextIntTable(N, 2);

    StarrySkyTree sst = new StarrySkyTree(300001);
    Arrays.sort(range, (a, b) -> (a[1] - a[0]) - (b[1] - b[0]));
    
    
    int idx = 0;
    for (int m = 1; m <= M; m ++) {
      int count = 0;
      for (; idx < N && range[idx][1] - range[idx][0] + 1 < m; idx ++) {
        sst.add(range[idx][0], range[idx][1] + 1, 1);
      }
      count += N - idx;
      
      for (int k = 0; k <= M; k += m) {
        count += sst.min(k, k + 1);
      }
      System.out.println(count);
    }
  }

  
}

class StarrySkyTree {
  public int M, H, N;
  public int[] st;
  public int[] plus;
  public int I = Integer.MAX_VALUE/4; // I+plus<int
  
  public StarrySkyTree(int n)
  {
      N = n;
      M = Integer.highestOneBit(Math.max(n-1, 1))<<2;
      H = M>>>1;
      st = new int[M];
      plus = new int[H];
  }
  
  public StarrySkyTree(int[] a)
  {
      N = a.length;
      M = Integer.highestOneBit(Math.max(N-1, 1))<<2;
      H = M>>>1;
      st = new int[M];
      for(int i = 0;i < N;i++){
          st[H+i] = a[i];
      }
      plus = new int[H];
      Arrays.fill(st, H+N, M, I);
      for(int i = H-1;i >= 1;i--)propagate(i);
  }
  
  private void propagate(int i)
  {
      st[i] = Math.min(st[2*i], st[2*i+1]) + plus[i];
  }
  
  public void add(int l, int r, int v){ if(l < r)add(l, r, v, 0, H, 1); }
  
  private void add(int l, int r, int v, int cl, int cr, int cur)
  {
      if(l <= cl && cr <= r){
          if(cur >= H){
              st[cur] += v;
          }else{
              plus[cur] += v;
              propagate(cur);
          }
      }else{
          int mid = cl+cr>>>1;
          if(cl < r && l < mid){
              add(l, r, v, cl, mid, 2*cur);
          }
          if(mid < r && l < cr){
              add(l, r, v, mid, cr, 2*cur+1);
          }
          propagate(cur);
      }
  }
  
  public int min(int l, int r){ return l >= r ? I : min(l, r, 0, H, 1);}
  
  private int min(int l, int r, int cl, int cr, int cur)
  {
      if(l <= cl && cr <= r){
          return st[cur];
      }else{
          int mid = cl+cr>>>1;
          int ret = I;
          if(cl < r && l < mid){
              ret = Math.min(ret, min(l, r, cl, mid, 2*cur));
          }
          if(mid < r && l < cr){
              ret = Math.min(ret, min(l, r, mid, cr, 2*cur+1));
          }
          return ret + plus[cur];
      }
  }
  
  public int[] toArray() { return toArray(1, 0, H, new int[H]); }
  
  private int[] toArray(int cur, int l, int r, int[] ret)
  {
      if(r-l == 1){
          ret[cur-H] = st[cur];
      }else{
          toArray(2*cur, l, l+r>>>1, ret);
          toArray(2*cur+1, l+r>>>1, r, ret);
          for(int i = l;i < r;i++)ret[i] += plus[cur];
      }
      return ret;
  }
}

class FastScanner {
	public static String debug = null;

	private final InputStream in = System.in;
	private int ptr = 0;
	private int buflen = 0;
	private byte[] buffer = new byte[1024];
	private boolean eos = false;

	private boolean hasNextByte() {
		if (ptr < buflen) {
			return true;
		} else {
			ptr = 0;
			try {
				if (debug != null) {
					buflen = debug.length();
					buffer = debug.getBytes();
					debug = "";
					eos = true;
				} else {
					buflen = in.read(buffer);
				}
			} catch (IOException e) {
				e.printStackTrace();
			}
			if (buflen < 0) {
				eos = true;
				return false;
			} else if (buflen == 0) {
				return false;
			}
		}
		return true;
	}

	private int readByte() {
		if (hasNextByte())
			return buffer[ptr++];
		else
			return -1;
	}

	private static boolean isPrintableChar(int c) {
		return 33 <= c && c <= 126;
	}

	private void skipUnprintable() {
		while (hasNextByte() && !isPrintableChar(buffer[ptr]))
			ptr++;
	}

	public boolean isEOS() {
		return this.eos;
	}

	public boolean hasNext() {
		skipUnprintable();
		return hasNextByte();
	}

	public String next() {
		if (!hasNext())
			throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = readByte();
		while (isPrintableChar(b)) {
			sb.appendCodePoint(b);
			b = readByte();
		}
		return sb.toString();
	}

	public long nextLong() {
		if (!hasNext())
			throw new NoSuchElementException();
		long n = 0;
		boolean minus = false;
		int b = readByte();
		if (b == '-') {
			minus = true;
			b = readByte();
		}
		if (b < '0' || '9' < b) {
			throw new NumberFormatException();
		}
		while (true) {
			if ('0' <= b && b <= '9') {
				n *= 10;
				n += b - '0';
			} else if (b == -1 || !isPrintableChar(b)) {
				return minus ? -n : n;
			} else {
				throw new NumberFormatException();
			}
			b = readByte();
		}
	}

	public int nextInt() {
		return (int) nextLong();
	}

	public long[] nextLongList(int n) {
		return nextLongTable(1, n)[0];
	}

	public int[] nextIntList(int n) {
		return nextIntTable(1, n)[0];
	}

	public long[][] nextLongTable(int n, int m) {
		long[][] ret = new long[n][m];
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < m; j ++) {
				ret[i][j] = nextLong();
			}
		}
		return ret;
	}

	public int[][] nextIntTable(int n, int m) {
		int[][] ret = new int[n][m];
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < m; j ++) {
				ret[i][j] = nextInt();
			}
		}
		return ret;
	}
}