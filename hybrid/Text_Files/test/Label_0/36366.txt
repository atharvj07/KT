import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}
	public Main() {
		new RitProE().doIt();
	}
	class RitProE{
		int n,m,e,start,end,days;
		boolean[][] map;
		int[][] eventMap;
		int[] a,b,c;
		void doIt(){
			n = in.nextInt();
			m = in.nextInt();
			e = in.nextInt();
			start = in.nextInt();
			end = in.nextInt();
			days = in.nextInt();
			map = new boolean[n][n];
			a = new int[e];
			b = new int[e];
			c = new int[e];
			for(int i=0;i<m;i++){
				int a = in.nextInt();
				int b = in.nextInt();
				map[a][b] = map[b][a] = true;
			}
			for(int i=0;i<e;i++){
				a[i] = in.nextInt();
				b[i] = in.nextInt();
				c[i] = in.nextInt();
			}
			int result = djkstra(start);
			System.out.println(result);
		}
		
		int djkstra(int v){
			PriorityQueue<Data> q = new PriorityQueue<Main.RitProE.Data>();
			int bbit = 0;
			for(int i=0;i<e;i++)if(c[i] == v){
				bbit |= 1 << i;
				break;
			}
			q.add(new Data(v, 0, bbit, 0));
			boolean[][][] close = new boolean[n][days+3][1<<8];
			while(q.size()>0){
				Data d = q.remove();
				int d_v = d.v;
				int cost = d.cost;
				int day = d.day;
				int bit = d.bit;

				if(days < day)continue;
//				System.out.println(" v= "+d_v+" cost= "+cost+" day= "+day+" bit= "+Integer.toBinaryString(bit));
				if(d.v == end)return d.cost;
				for(int i=0;i<e;i++)if(c[i] == d.v){
					bit |= 1 << i;
					break;
				}
				for(int i=0;i<n;i++){//normal mode
					if(map[d.v][i]){
						Data data = new Data(i, day+1, bit, cost+1);
						if (close[data.v][data.day][data.bit])continue;
						close[data.v][data.day][data.bit] = true;
						q.add(data);
						
					}
				}
				
				Data data = new Data(start, 0, bit, cost+1);
				if (close[data.v][data.day][data.bit] == false)q.add(data);
				close[data.v][data.day][data.bit] = true;
				
				for(int i=0;i<e;i++){
					if (((bit >> i) & 1) == 1) {
						if(a[i] == d.v){
							data = new Data(b[i], day+1, bit, cost+1);
							if (close[data.v][data.day][data.bit] == false)q.add(data);
							close[data.v][data.day][data.bit] = true;
						}else if(b[i] == d.v){
							data = new Data(a[i], day+1, bit, cost+1);
							if (close[data.v][data.day][data.bit] == false)q.add(data);
							close[data.v][data.day][data.bit] = true;
						}
					}
				}
			}
			return -1;
		}
		
		class Data implements Comparable<Data>{
			int v,day,bit,cost;
			public Data(int v,int day,int bit, int cost){
				this.v = v;
				this.day = day;
				this.bit = bit;
				this.cost = cost;
			}
			public int compareTo(Data o) {
				return this.cost-o.cost;
			}
		}
		
	}
}