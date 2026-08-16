import java.io.IOException; 
import java.io.InputStream; 
import java.io.PrintWriter; 
import java.util.*; 
 

public class Main{ 

	static void solve(){
		int h = ni(), w=ni();
		int H = w+h+1, W=h+w+1;
		int[][] cnt = new int[H][W];
		int[][] cnty=new int[H][W];
		long ans =0;
		Map<Integer, List<Integer> > ytox=new HashMap<>();
		Map<Integer, List<Integer> > xtoy= new HashMap<>();
		for(int i=0;i<h;++i){
			String s = ns();
			for(int j=0;j<w;++j)if(s.charAt(j)=='#'){
				int y=j-i+h+1, x=i+j+1;
				cnt[y][x]++;
				cnty[y][x]++;
				if(!ytox.containsKey(y))ytox.put(y, new ArrayList<>());
				ytox.get(y).add(x);
				if(!xtoy.containsKey(x))xtoy.put(x, new ArrayList<>());
				xtoy.get(x).add(y);
			}
		}

		for(int i=0;i<H;++i)for(int j=1;j<W;++j)cnt[i][j]+=cnt[i][j-1];
		for(int j=0;j<W;++j)for(int i=1;i<H;++i)cnty[i][j]+=cnty[i-1][j];
		for(Map.Entry<Integer, List<Integer>> entry: ytox.entrySet()){
			List<Integer> list = entry.getValue();
			Collections.sort(list);
			int y = entry.getKey();
			for(int i=0;i<list.size()-1;++i){
				for(int j=i+1;j<list.size();++j){
					int d = Math.abs(list.get(i)-list.get(j));
					if(inrange(y+d, list.get(i), H, W))ans+=(long)(cnt[y+d][list.get(j)]-cnt[y+d][list.get(i)-1]);
					if(inrange(y-d, list.get(i), H, W))ans+=(long)(cnt[y-d][list.get(j)]-cnt[y-d][list.get(i)-1]);
				}
			}
		}
		for(Map.Entry<Integer, List<Integer>> entry: xtoy.entrySet()){
			List<Integer> list = entry.getValue();
			Collections.sort(list);
			int x = entry.getKey();
			for(int i=0;i<list.size()-1;++i){
				for(int j=i+1;j<list.size();++j){
					int d = Math.abs(list.get(i)-list.get(j));
					if(inrange(list.get(i), x-d, H, W))ans+=(long)(cnty[list.get(j)-1][x-d]-cnty[list.get(i)][x-d]);
					if(inrange(list.get(i), x+d, H, W))ans+=(long)(cnty[list.get(j)-1][x+d]-cnty[list.get(i)][x+d]);
				}
			}
		}
		out.println(ans);
 
	} 
 
 
 
 
	 public static void main(String[] args){ 
		 solve(); 
		 out.flush(); 
	 } 
	 private static InputStream in = System.in; 
	 private static PrintWriter out = new PrintWriter(System.out); 
 
	 static boolean inrange(int y, int x, int h, int w){ 
		 return y>=0 && y<h && x>=0 && x<w; 
	 } 
	 @SuppressWarnings("unchecked") 
	 static<T extends Comparable> int lower_bound(List<T> list, T key){ 
		 int lower=-1;int upper=list.size(); 
		 while(upper - lower>1){ 
		 int center =(upper+lower)/2; 
		 if(list.get(center).compareTo(key)>=0)upper=center; 
		 else lower=center; 
		 } 
		 return upper; 
	 } 
	 @SuppressWarnings("unchecked") 
	 static <T extends Comparable> int upper_bound(List<T> list, T key){ 
		 int lower=-1;int upper=list.size(); 
		 while(upper-lower >1){ 
		 int center=(upper+lower)/2; 
		 if(list.get(center).compareTo(key)>0)upper=center; 
		 else lower=center; 
		 } 
		 return upper; 
	 } 
	 @SuppressWarnings("unchecked") 
	 static <T extends Comparable> boolean next_permutation(List<T> list){ 
		 int lastIndex = list.size()-2; 
		 while(lastIndex>=0 && list.get(lastIndex).compareTo(list.get(lastIndex+1))>=0)--lastIndex; 
		 if(lastIndex<0)return false; 
		 int swapIndex = list.size()-1; 
		 while(list.get(lastIndex).compareTo(list.get(swapIndex))>=0)swapIndex--; 
		 T tmp = list.get(lastIndex); 
		 list.set(lastIndex++, list.get(swapIndex)); 
		 list.set(swapIndex, tmp); 
		 swapIndex = list.size()-1; 
		 while(lastIndex<swapIndex){ 
		 tmp = list.get(lastIndex); 
		 list.set(lastIndex, list.get(swapIndex)); 
		 list.set(swapIndex, tmp); 
		 ++lastIndex;--swapIndex; 
		 } 
		 return true; 
	 } 
	 private static final byte[] buffer = new byte[1<<15]; 
	 private static int ptr = 0; 
	 private static int buflen = 0; 
	 private static boolean hasNextByte(){ 
		 if(ptr<buflen)return true; 
		 ptr = 0; 
		 try{ 
			 buflen = in.read(buffer); 
		 } catch (IOException e){ 
			 e.printStackTrace(); 
		 } 
		 return buflen>0; 
	 } 
	 private static int readByte(){ if(hasNextByte()) return buffer[ptr++]; else return -1;} 
	 private static boolean isSpaceChar(int c){ return !(33<=c && c<=126);} 
	 private static int skip(){int res; while((res=readByte())!=-1 && isSpaceChar(res)); return res;} 
 
	 private static double nd(){ return Double.parseDouble(ns()); } 
	 private static char nc(){ return (char)skip(); } 
	 private static String ns(){ 
		 StringBuilder sb = new StringBuilder(); 
		 for(int b=skip();!isSpaceChar(b);b=readByte())sb.append((char)b); 
		 return sb.toString(); 
	 } 
	 private static int[] nia(int n){ 
		 int[] res = new int[n]; 
		 for(int i=0;i<n;++i)res[i]=ni(); 
		 return res; 
	 } 
	 private static long[] nla(int n){ 
		 long[] res = new long[n]; 
		 for(int i=0;i<n;++i)res[i]=nl(); 
		 return res; 
	 } 
	 private static int ni(){ 
		 int res=0,b; 
		 boolean minus=false; 
		 while((b=readByte())!=-1 && !((b>='0'&&b<='9') || b=='-')); 
		 if(b=='-'){ 
			 minus=true; 
			 b=readByte(); 
		 } 
		 for(;'0'<=b&&b<='9';b=readByte())res=res*10+(b-'0'); 
		 return minus ? -res:res; 
	 } 
	 private static long nl(){ 
		 long res=0,b; 
		 boolean minus=false; 
		 while((b=readByte())!=-1 && !((b>='0'&&b<='9') || b=='-')); 
		 if(b=='-'){ 
			 minus=true; 
			 b=readByte(); 
		 } 
		 for(;'0'<=b&&b<='9';b=readByte())res=res*10+(b-'0'); 
		 return minus ? -res:res; 
	} 
} 

