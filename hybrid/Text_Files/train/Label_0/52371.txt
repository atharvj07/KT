import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.Iterator;

public class Main {

	static BufferedReader reader;
	final static boolean MODE_DEBUG = false;
	static int[] read_line_int;
	static int read_line_int_ptr;
	static long[] read_line_long;
	static int read_line_long_ptr;
	static String[] read_line;
	static int read_line_ptr;
	//static field here
	
	static final int T = 26;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		reader = new BufferedReader(new InputStreamReader(System.in));
		//code here
		int D = readInt();
		
		long S = 0;
		int[] c = readLineInt();
		int[] t = new int[D];
		int[] last = new int[T];
		int[][] next = new int[D][T];
		int[][] prev = new int[D][T];
		Arrays.fill(last,-1);
		Arrays.fill(prev[0],-1);
		int[][] s = new int[D][T];
		for(int d=0;d<D;d++) {
			s[d] = readLineInt();
		}
		for(int d=0;d<D;d++) {
			Arrays.fill(next[d],D);
			t[d] = readInt()-1;
			S+=s[d][t[d]];
			last[t[d]]=d;
			prev[d][t[d]]=d;
			for(int tt=0;tt<T;tt++) {
				S-=c[tt]*(d-last[tt]);
			}
			for(int dd=d;dd>=0;dd--) {
				if(next[dd][t[d]]==D) {
					next[dd][t[d]] = d;
				}else {
					break;
				}
			}
			if(d+1<D) {
				prev[d+1] = Arrays.copyOf(prev[d],T);
			}
		}
		int M = readInt();
		for(int m=0;m<M;m++) {
			int d = readInt()-1;
			int q = readInt()-1;
			int tb = t[d];
			
			//取り除く
			int new_next_num = (d==D-1)?D:next[d+1][tb];
			int new_prev_num = (d==0)?-1:prev[d-1][tb];
			S-=(d-new_prev_num)*(new_next_num-d)*c[tb];
			S-=s[d][tb];
			for(int i=d;i<new_next_num;i++) {
				prev[i][tb] = new_prev_num;
			}
			for(int i=d;i>new_prev_num;i--) {
				next[i][tb] = new_next_num;
			}
			
			//挿入する
			int prev_next_num = next[d][q];
			int prev_prev_num = prev[d][q];
			S+=(d-prev_prev_num)*(prev_next_num-d)*c[q];
			for(int i=d;i<prev_next_num;i++) {
				prev[i][q] = d;
			}
			for(int i=d;i>prev_prev_num;i--) {
				next[i][q] = d;
			}
			S+=s[d][q];
			t[d] = q;
			print(S);
		}
	}
	
	//functions here
	//note that all methods should be STATIC
	private static int sum(int from, int to) {
		return (to*(to+1))/2 - (from*(from-1))/2;
	}

	private static <T> int arraySearch(T needle, T[] heystack) {
		for(int i=0;i<heystack.length;i++) {
			if(needle.equals(heystack[i])) {
				return i;
			}
		}
		return -1;
	}
	private static int[] sort(int[] base) {
		int[] copy = array_copy(base);
		Arrays.sort(copy);
		return copy;
	}
	private static int[] array_copy(int[] base) {
		int[] copy = new int[base.length];
		for(int i=0;i<base.length;i++) {
			copy[i] = base[i];
		}
		return copy;
	}
	private static int[] asArray(ArrayList<Integer> ints) {
		int[] intlist = new int[ints.size()];
		for(int i=0;i<intlist.length;i++) {
			intlist[i] = ints.get(i);
		}
		return intlist;
	}
	private static int readInt() {
		if(read_line_int==null||read_line_int_ptr==read_line_int.length) {
			read_line_int = readLineInt();
			read_line_int_ptr=0;
		}
		return read_line_int[read_line_int_ptr++];
	}
	private static long readLong() {
		if(read_line_long==null||read_line_long_ptr==read_line_long.length) {
			read_line_long = readLineLong();
			read_line_long_ptr=0;
		}
		return read_line_long[read_line_long_ptr++];
	}
	private static String readString() {
		if(read_line==null||read_line_int_ptr==read_line.length) {
			read_line = readLine();
			read_line_ptr=0;
		}
		return read_line[read_line_ptr++];
	}
	private static String[] readLine(){
		try{
			return reader.readLine().split(" ");
		}catch(Exception e){
			e.printStackTrace();
			return new String[]{e.getMessage()};
		}
	}
	private static int[] readLineInt(){
		try{
			String[] s = readLine();
			int[] ints = new int[s.length];
			for(int i=0;i<ints.length;i++) {
				ints[i] = Integer.parseInt(s[i]);
			}
			return ints;
		}catch(Exception e){
			e.printStackTrace();
			return null;
		}
	}
	private static long[] readLineLong(){
		try{
			String[] s = readLine();
			long[] ints = new long[s.length];
			for(int i=0;i<ints.length;i++) {
				ints[i] = Long.parseLong(s[i]);
			}
			return ints;
		}catch(Exception e){
			e.printStackTrace();
			return null;
		}
	}
	private static byte[] readLineByte(){
		try{
			String[] s = readLine();
			byte[] bytes = new byte[s.length];
			for(int i=0;i<bytes.length;i++) {
				bytes[i] = Byte.parseByte(s[i]);
			}
			return bytes;
		}catch(Exception e){
			e.printStackTrace();
			return null;
		}
	}
	private static char[] readLineChar(){
		try{
			String[] s = readLine();
			char[] chars = new char[s.length];
			for(int i=0;i<chars.length;i++) {
				chars[i] = (char)Integer.parseInt(s[i]);
			}
			return chars;
		}catch(Exception e){
			e.printStackTrace();
			return null;
		}
	}
	private static void print(Object o){
		System.out.println(o);
	}
	private static void print(){
		System.out.println();
	}
	private static void printd(Object o){
		if(MODE_DEBUG)System.err.println(o);
	}
	private static void printd(){
		if(MODE_DEBUG)System.err.println();
	}
}
