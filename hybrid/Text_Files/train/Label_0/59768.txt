import static java.lang.Math.PI;
import static java.lang.Math.abs;
import static java.lang.Math.acos;
import static java.lang.Math.cos;
import static java.lang.Math.min;
import static java.lang.Math.sin;
import static java.lang.Math.sqrt;
import static java.lang.System.in;
import static java.lang.System.out;


import java.io.*;
import java.util.*;

public class D350 {
	static final double EPS = 0.0000001;
	static final double INF = 1 << 31;
	static final double PI = Math.PI;
	int hashBase = 30000;

	public static Scanner sc = new Scanner(in);
	StringBuilder sb = new StringBuilder();
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public void run() throws IOException {
		String input;
		String[] inputArray;
		input = br.readLine();
		inputArray = input.split(" ");
		int n = Integer.valueOf(inputArray[0]);
		int m = Integer.valueOf(inputArray[1]);
		int x1,y1,x2,y2;
		TreeMap<Long, ArrayList<Long>> left = new TreeMap<Long, ArrayList<Long>>();
		TreeMap<Long, ArrayList<Long>> right = new TreeMap<Long, ArrayList<Long>>();
		for (int i=0; i<n; i++){
			input = br.readLine();
			inputArray = input.split(" ");
			x1 = Integer.valueOf(inputArray[0]);
			y1 = Integer.valueOf(inputArray[1]);
			x2 = Integer.valueOf(inputArray[2]);
			y2 = Integer.valueOf(inputArray[3]);
			long A, B, C;
			A = y1-y2;
			B = x2-x1;
			C = x1*y2 - y1*x2;
			long g = gcd(A, gcd(B,C));
			if (A/g<0 || (A==0 && B/g<0)) g=-g;
			A/=g;
			B/=g;
			C/=g;
			long hashV = A*hashBase*hashBase+B*hashBase+C;
			if (!left.containsKey(hashV)){
				left.put(hashV, new ArrayList<Long>());
				right.put(hashV, new ArrayList<Long>());
			}
			if (x2<x1 || (x1==x2 && y2<y1)){
				left.get(hashV).add((long) (x2*hashBase+y2));
				right.get(hashV).add((long) (x1*hashBase+y1));
			} else{
				right.get(hashV).add((long) (x2*hashBase+y2));
				left.get(hashV).add((long) (x1*hashBase+y1));
			}
		}
		for(Map.Entry<Long,ArrayList<Long>> entry : left.entrySet()) 
			Collections.sort(entry.getValue());
		for(Map.Entry<Long,ArrayList<Long>> entry : right.entrySet()) 
			Collections.sort(entry.getValue());
		ArrayList <Circle> cir = new ArrayList <Circle>();
		for (int i=0; i<m; i++){
			input = br.readLine();
			inputArray = input.split(" ");
			cir.add(new Circle(Integer.valueOf(inputArray[0]),Integer.valueOf(inputArray[1]),
					Integer.valueOf(inputArray[2])));
		}
		int ans = 0;
		for (int i=0; i<m; i++)
			for (int j=i+1; j<m; j++)
				if (cir.get(i).r==cir.get(j).r && !Circle.intersect(cir.get(i), cir.get(j))){
					Circle c1 = cir.get(i);
					Circle c2 = cir.get(j);
					long A, B, C;
					A = 2*(c1.x-c2.x);
					B = 2*(c1.y-c2.y);
					C = -(long)((c1.x - c2.x)*(c1.x+c2.x)+(c1.y - c2.y)*(c1.y + c2.y));
					long g = gcd(A, gcd(B,C));
					if (A/g<0 || (A==0 && B/g<0)) g=-g;
					A/=g;
					B/=g;
					C/=g;
					double px = (c1.x + c2.x)/2;
					double py = (c1.y + c2.y)/2;
					double p = px*hashBase+py;
					//int cntL = left.ceilingEntry(ceilingEntry(A+B+D,px*hashBase + py);
					long hashV = A*hashBase*hashBase+B*hashBase+C;
					if (left.containsKey(hashV)){
						int all = left.get(hashV).size();
						//upper bound
						int l = 0, r = all;
						while(l+1<r){
							int mid =(l+r)/2;
							if (left.get(hashV).get(mid)>p) r = mid;
							else l = mid;
						}
						while((l<all && left.get(hashV).get(l)<p+EPS)) l++;
						int total =all-l;
						//right bound
						all = right.get(hashV).size();
						l = -1; r = all-1;
						while(l+1<r){
							int mid =(l+r)/2;
							if (right.get(hashV).get(mid)<p) l = mid;
							else r = mid;
						}
						while((l+1<all && right.get(hashV).get(l+1)<p)) l++;
						total+=(l+1);
						ans+=Math.max(all-total,0);
					}
				}
		sb.append(ans);
		ln(sb);
	}

	static class Circle{
		int x,y;
		int r;
		Circle(int a, int b, int c){
			x = a; y = b; r = c;
		}
		public static boolean intersect(Circle c1, Circle c2){
			int d = (c1.x-c2.x)*(c1.x-c2.x) + (c1.y-c2.y)*(c1.y-c2.y);
			if((c1.r+c2.r)*(c1.r+c2.r)+EPS<d)return false;
			else return true;
		}
		public String toString(){
			return x + " " + y;
		}
	}
	public static void main(String[] args) throws IOException {
		new D350().run();
	}
	public static void ln(Object obj) {
		out.println(obj);
	}
	public long gcd (long a, long b){
		//if (a<b) return gcd(b,a);
		if (b==0) return a;
		return gcd(b,a%b);
	}
}
