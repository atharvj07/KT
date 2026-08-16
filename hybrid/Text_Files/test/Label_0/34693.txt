import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class C357 {
	public static void main(String[] args) {
		MyScanner scan = new MyScanner();
		PrintWriter out = new PrintWriter(System.out);
		
		int N = scan.nextInt();
		PriorityQueue<Integer> q = new PriorityQueue<>();
		ArrayList<Op> list = new ArrayList<>();
		
		for(int i=0;i<N;i++){
			String s = scan.next();
			if(s.equals("insert")){
				int t = scan.nextInt();
				q.add(t);
				list.add(new Op(0, t, i));
			}
			if(s.equals("getMin")){
				int t = scan.nextInt();
				if(q.isEmpty()||!q.peek().equals(t)){
					while(!q.isEmpty()&&q.peek().compareTo(t)<0){
						q.poll();
						list.add(new Op(1, -1,-1));
					}
					if(q.isEmpty()||q.peek().compareTo(t)>0){
						q.add(t);
						list.add(new Op(0, t, i));
					}
				}
				list.add(new Op(2, t, i));
			}
			if(s.equals("removeMin")){
				if(q.size()==0){
					list.add(new Op(0, 1, -1));
				}
				list.add(new Op(1, -1,-1));
				q.poll();
			}
		}
		out.println(list.size());
		for(int i=0;i<list.size();i++){
			if(list.get(i).type==0){
				out.println("insert "+list.get(i).val);
			}
			if(list.get(i).type==1){
				out.println("removeMin");
			}
			if(list.get(i).type==2){
				out.println("getMin "+list.get(i).val);
			}
		}
		out.close();
	}
	private static class Op {
		int type, val, idx;
		//0 = insert, 1 = remove, 2 = getMin
		public Op(int type, int val, int idx){
			this.type = type;
			this.val = val;
			this.idx = idx;
		}
	}
	private static class MyScanner {
		BufferedReader br;
		StringTokenizer st;
		public MyScanner() {br = new BufferedReader(new InputStreamReader(System.in));}
		String next(){
			while(st==null||!st.hasMoreElements()){
				try{st = new StringTokenizer(br.readLine());}
				catch(IOException e){e.printStackTrace();}
			}return st.nextToken();
		}
		int nextInt() {return Integer.parseInt(next());}
		long nextLong() {return Long.parseLong(next());}
	}
}
