import java.util.*;
import java.io.*;
 
public class Main {
 
	public static void main(String[] args) throws IOException,InterruptedException{
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt(),m=sc.nextInt(),k=sc.nextInt();
		PriorityQueue<pair> pq1=new PriorityQueue<>();
		PriorityQueue<pair> pq2=new PriorityQueue<>();
		PriorityQueue<pair> pq3=new PriorityQueue<>();
		PriorityQueue<pair> pq4=new PriorityQueue<>();
		TreeSet<pair> pq5=new TreeSet<>();
		TreeSet<pair> pq6=new TreeSet<>();
		TreeSet<pair> pq7=new TreeSet<>();
		TreeSet<pair> pq8=new TreeSet<>();
		for (int i = 0; i < n; i++) {
			int t=sc.nextInt(),a=sc.nextInt(),b=sc.nextInt();
			if(a==1&&b==1) {
				pq1.add(new pair(t,i+1));
			}else if(a==1) {
				pq2.add(new pair(t,i+1));
			}else if(b==1) {
				pq3.add(new pair(t,i+1));
			}else {
				pq4.add(new pair(t,i+1));
			}
		}
		long c=0;
		for (int i = 0; i < k; i++) {
			long a=1000000000;
			long b=1000000000;
			if(!pq1.isEmpty()) a=pq1.peek().x;
			if(!pq2.isEmpty()&&!pq3.isEmpty()) b=pq2.peek().x+pq3.peek().x;
			if (a==1000000000&&b==1000000000) {
				c=-1;
				break;
			}
			if(a<=b) {
				c+=a;
				pq5.add(pq1.poll());
			}else {
				c+=b;
				pq6.add(pq2.poll());
				pq7.add(pq3.poll());
			}
		}
		if (pq5.size()+pq6.size()+pq7.size()>m) {
			while (pq5.size()+pq6.size()+pq7.size()>m) {
				if(pq1.isEmpty()) {
					c=-1;
					break;
				}
				c-=pq7.pollLast().x;
				c-=pq6.pollLast().x;
				c+=pq1.peek().x;
				pq5.add(pq1.poll());
			}
		}else if (pq5.size()+pq6.size()+pq7.size()+pq8.size()<m) {
			int c3=0,c2=0;
			while (pq5.size()+pq6.size()+pq7.size()+pq8.size()<m) {
				pair a=new pair(1000000000,1000000000);
				boolean f1=false,f2=false,f3=false;
				if(!pq1.isEmpty()) {
					a=pq1.poll();
					f1=true;
				}
				if(!pq2.isEmpty())
					if (pq2.peek().x<=a.x) {
						if(f1) pq1.add(a);
						a=pq2.poll();
						f2=true;
						f1=false;
					} 
				if(!pq3.isEmpty()) 
					if (pq3.peek().x<=a.x) {
						if(f1) pq1.add(a);
						else if(f2) pq2.add(a);
						a=pq3.poll();
						f3=true;
						f2=false;
						f1=false;
					} 
				if(!pq4.isEmpty()) 
					if (pq4.peek().x<=a.x) {
						if(f1)pq1.add(a);
						else if(f2) pq2.add(a);
						else if(f3) pq3.add(a);
						a=pq4.poll();
						f3=false;
						f2=false;
						f1=false;
					}
				if(f2) c2++;
				if(f3) c3++;
				if(c2>=1&&c3>=1&&!pq5.isEmpty()) {
					c2--;
					c3--;
					c-=pq5.last().x;
					pq1.add(pq5.pollLast());
				}else if (c2>=1&&!pq3.isEmpty()&&!pq5.isEmpty()) {
					if (pq3.peek().x<pq5.last().x) {
						c2--;
						c-=pq5.last().x;
						c+=pq3.peek().x;
						pq1.add(pq5.pollLast());
						pq7.add(pq3.poll());
					}
				}else if (c3>=1&&!pq2.isEmpty()&&!pq5.isEmpty()) {
					if (pq2.peek().x<pq5.last().x) {
						c2--;
						c-=pq5.last().x;
						c+=pq2.peek().x;
						pq1.add(pq5.pollLast());
						pq6.add(pq2.poll());
					}
				}
				if(f1) pq5.add(a);
				else if(f2) pq6.add(a);
				else if(f3) pq7.add(a);
				else pq8.add(a);
				c+=a.x;
			}
		}
		if(pq5.size()+pq6.size()<k||pq5.size()+pq7.size()<k)  c=-1;
		pw.println(c);
		if(c!=-1) {
			while (!pq5.isEmpty()) {
				pw.print(pq5.pollFirst().y+" ");
			} while (!pq6.isEmpty()) {
				pw.print(pq6.pollFirst().y+" ");
			} while (!pq7.isEmpty()) {
				pw.print(pq7.pollFirst().y+" ");
			} while (!pq8.isEmpty()) {
				pw.print(pq8.pollFirst().y+" ");
			} 
			pw.println();
		}
		pw.close();
    }
	
	static PrintWriter pw=new PrintWriter(System.out);
	static long pow(int a,int b) {
		long r=1l;
		for (int i = 0; i < b; i++) {
			r*=a;
		}
		return r;
	}
	static boolean isprime(long n) {
		for (int i = 2; i <= Math.sqrt(n); i++) {
			if(n%i==0) return false;
		}
		return true;
	}
	static int[]lp;
	static void sieveLinear(int N){
		ArrayList<Integer> primes = new ArrayList<Integer>();
		lp = new int[N + 1];								//lp[i] = least prime divisor of i
		for(int i = 2; i <= N; ++i){
			if(lp[i] == 0){
				primes.add(i);
				lp[i] = i;
			}
			int curLP = lp[i];
			for(int p: primes)//all primes smaller than or equal my lowest prime divisor
				if(p > curLP || p * 1l * i > N)
					break;
				else
					lp[p * i] = p;
		}
	}
	static long gcd(int x,int y) {
		while (x!=y) {
			if(Math.max(x,y)/Math.min(x,y)==(double)(Math.max(x,y))/Math.min(x,y)) return Math.min(x,y);
			if(lp.length!=0) {
				if(lp[x]==x) {
					if(y/x==y/(double)x) return x;
					else return 1;
				}else if (lp[y]==y) {
					if(x/y==x/(double)y) return y;
					else return 1;
				}	
			}
			if(x>y) x-=y;
			else y-=x;
		}
		return x;
	}
	static class pair implements Comparable<pair> {
		int x;
		int y;
 
		public pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
 
		public String toString() {
			return x + " " + y;
		}
		public boolean equals(Object o) {
            if (o instanceof pair) {
                pair p = (pair)o;
                return p.x == x && p.y == y;
            }
            return false;
        }
        public int hashCode() {
            return new Double(x).hashCode() * 31 + new Double(y).hashCode();
        }
        public int compareTo(pair other) {
        	if(this.x==other.x) {
        		return Long.compare(this.y, other.y);
        	}
			return Long.compare(this.x, other.x);
		}
	}
	static class tuble implements Comparable<tuble> {
		int x;
		int y;
		int z;
 
		public tuble(int x, int y, int z) {
			this.x = x;
			this.y = y;
			this.z = z;
		}
 
		public String toString() {
			return x + " " + y + " " + z;
		}
 
		public int compareTo(tuble other) {
			if (this.x == other.x) {
				if(this.y==other.y) return this.z - other.z;
				else return this.y - other.y;
			} else {
				return this.x - other.x;
			}
		}
	}
 	static class Scanner {
		StringTokenizer st;
		BufferedReader br;
 
		public Scanner(InputStream s) {
			br = new BufferedReader(new InputStreamReader(s));
		}
 
		public boolean hasNext() {
			// TODO Auto-generated method stub
			return false;
		}
 
		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}
 
		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}
 
		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}
 
		public String nextLine() throws IOException {
			return br.readLine();
		}
 
		public double nextDouble() throws IOException {
			String x = next();
			StringBuilder sb = new StringBuilder("0");
			double res = 0, f = 1;
			boolean dec = false, neg = false;
			int start = 0;
			if (x.charAt(0) == '-') {
				neg = true;
				start++;
			}
			for (int i = start; i < x.length(); i++)
				if (x.charAt(i) == '.') {
					res = Long.parseLong(sb.toString());
					sb = new StringBuilder("0");
					dec = true;
				} else {
					sb.append(x.charAt(i));
					if (dec)
						f *= 10;
				}
			res += Long.parseLong(sb.toString()) / f;
			return res * (neg ? -1 : 1);
		}
 
		public boolean ready() throws IOException {
			return br.ready();
		}
 
	}
 
}
