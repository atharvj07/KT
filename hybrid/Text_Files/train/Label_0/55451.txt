import java.util.*;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		while(true){
			int n=sc.nextInt(), m=sc.nextInt();
			if(n==0 && m==0) break;
			boolean flg[] = new boolean[n+1];
			PriorityQueue<Packet> pq = new PriorityQueue<Packet>();

			while(m-- > 0)
				pq.add(new Packet(sc.nextInt(),sc.nextInt(),sc.nextInt()));

			flg[1] = true;
			while(!pq.isEmpty()){
				Packet p = pq.poll();
				if(flg[p.s]) flg[p.d]=true;
			}

			int ans = 0;
			for(int i=1;i<=n;i++) if(flg[i]) ans++;

			System.out.println(ans);
		}
	}
}

class Packet implements Comparable<Packet>{
	int t,s,d;

	public Packet(int t, int s, int d){
		this.t = t;
		this.s = s;
		this.d = d;
	}

	public int compareTo(Packet p){
		return this.t - p.t;
	}
}