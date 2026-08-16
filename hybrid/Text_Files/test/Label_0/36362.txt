import java.util.*;
public class Main {
	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}
	public Main() {
		new AOJ2013().doIt();
	}
	
	class AOJ2013{
		int n;
		ArrayList<Data> list;
		
		void solve(){
			int result = 0;
			int[] map = new int[25*60*60];
			for(int i=0;i<list.size();i++)for(int s=list.get(i).start;s<list.get(i).end;s++)map[s]++;
			for(int i=0;i<map.length;i++)result = Math.max(result, map[i]);
			System.out.println(result);
		}
		
		void doIt(){
			while(in.hasNext()){
				n = in.nextInt();
				if(n==0)break;
				list = new ArrayList<Data>();
				for(int i=0;i<n;i++)list.add(new Data(in.next(), in.next()));
				solve();
			}
		}
		class Data{
			int start,end;
			public Data(String a,String b){
				String[] input = a.split(":");
				start = getTime(Integer.parseInt(input[0]), Integer.parseInt(input[1]), Integer.parseInt(input[2]));
				input = b.split(":");
				end = getTime(Integer.parseInt(input[0]), Integer.parseInt(input[1]), Integer.parseInt(input[2]));
//				System.out.println(start+" "+end);
			}
			
			int getTime(int h,int m,int s){
				int result = s;
				result += m*60;
				result += h*60*60;
				return result;
			}
			
		}
	}
	
}