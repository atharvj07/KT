import java.util.*;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		for(int set=1;;set++){
			int n = sc.nextInt();
			if(n == 0) break;

			ArrayList<ArrayList<Edge>> map = new ArrayList<ArrayList<Edge>>();
			for(int i=0;i<=80000;i++){
				map.add(new ArrayList<Edge>());
			}

			for(int i=0;i<n;i++){
				double x = sc.nextDouble();
				double y = sc.nextDouble();
				double r = sc.nextDouble();

				int left = (int)((x - r) * 100) + 40000;
				int right = (int)((x + r) * 100) + 40000;
				for(int j=left;j<right;j++){
					map.get(j).add(new Edge((int)((y-r)*100),true));
					map.get(j).add(new Edge((int)((y+r)*100),false));
				}
			}

			int ans = 0;
			for(int i=0;i<=80000;i++){
				if(map.get(i).isEmpty()) continue;
				Collections.sort(map.get(i));
				int level = 0;
				int top = 0;
				for(Edge e : map.get(i)){
					if(e.d){
						if(level == 0) top = e.place;
						level++;
					}
					else{
						level--;
						if(level == 0) ans += (e.place - top);
					}
				}
			}

			System.out.printf("%d %.2f\n",set,0.0001*ans);
		}
	}
}

class Edge implements Comparable<Edge>{
	int place;
	boolean d; //true : from, false : to

	Edge(int place,boolean d){
		this.place = place;
		this.d = d;
	}

	public int compareTo(Edge e){
		if(place < e.place) return -1;
		if(place > e.place) return 1;
		if(d == false && e.d == true) return 1;
		if(d == true && e.d == false) return -1;
		return 0;
	}
}