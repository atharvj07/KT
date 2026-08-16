import java.util.*;
import java.awt.Point;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		while(true){
			int n = sc.nextInt();
			if(n == 0) break;

			LinkedList< LinkedList<Integer> > s = new LinkedList< LinkedList<Integer> >();

			for(int i=1;i<=n;i++){
				LinkedList<Integer> tmp = new LinkedList<Integer>();
				tmp.add(i);
				s.add(tmp);
			}

			while(true){
				int from = sc.nextInt(), to = sc.nextInt();
				if(from == 0 && to == 0) break;

				Point resA = find(s,from);
				Point resB = find(s,to);

				if(resB == null){
					if(resA.y == 0) continue;
					fall(s,resA);
					LinkedList<Integer> tmp = new LinkedList<Integer>();
					tmp.add(s.get(resA.x).removeLast());
					s.add(tmp);
				}
				else if(resA.x == resB.x && resA.y < resB.y){
					fall(s,resA);
					resB = find(s,to);
					s.get(resB.x).add(s.get(resA.x).removeLast());
				}
				else if(resA.x != resB.x){
					fall(s,resA);
					s.get(resB.x).add(s.get(resA.x).removeLast());
				}
			}

			ArrayList<Integer> ans = new ArrayList<Integer>();
			for(int i=0;i<s.size();i++)
				if(s.get(i).size() > 0) ans.add(s.get(i).size());

			Collections.sort(ans);
			for(int x : ans) System.out.println(x);
			System.out.println("end");
		}
	}

	private static Point find(LinkedList< LinkedList<Integer> > list, int x){
		for(int i=0;i<list.size();i++){
			LinkedList<Integer> tmp = list.get(i);
			if(tmp.contains(x)) return new Point(i,tmp.indexOf(x));
		}
		return null;
	}

	private static void fall(LinkedList< LinkedList<Integer> > list,Point p){
		while(list.get(p.x).size() > p.y + 1){
			LinkedList<Integer> tmp = new LinkedList<Integer>();
			tmp.add(list.get(p.x).removeLast());
			list.add(tmp);
		}
	}
}