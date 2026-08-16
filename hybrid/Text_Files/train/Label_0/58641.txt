import java.util.*;

public class Main{
	
	class Seg implements Comparable<Seg>{
		int start, end;

		public Seg(int start, int end) {
			this.start = start;
			this.end = end;
		}

		@Override
		public int compareTo(Seg o) {
			return this.start- o.start;
		}

		@Override
		public String toString() {
			return "Seg [start=" + start + ", end=" + end + "]";
		}
		
	}
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		int MAX = 1000000000;
		while(true){
			int n = sc.nextInt();
			if(n == 0) break;
			ArrayList<Seg> emptylist = new ArrayList<Seg>();
			emptylist.add(new Seg(0, MAX));
			HashMap<Integer, ArrayList<Seg>> sector = new HashMap<Integer, ArrayList<Seg>>();
			while(n-- > 0){
				char c = sc.next().charAt(0);
				if(c == 'W'){
					int name = sc.nextInt();
					int size = sc.nextInt();
					ArrayList<Seg> newsector  = new ArrayList<Main.Seg>();
					for(int i = 0; i < emptylist.size(); i++){
						Seg nows = emptylist.get(i);
						if(nows.end - nows.start + 1 > size){
							Seg afterS = new Seg(nows.start, nows.start + size - 1);
							newsector.add(afterS);
							emptylist.set(i, new Seg(nows.start + size, nows.end));
							break;
						}
						else if(nows.end - nows.start + 1 == size){
							newsector.add(nows);
							emptylist.remove(i);
							break;
						}
						else{
							newsector.add(nows);
							emptylist.remove(i);
							size = size - (nows.end - nows.start + 1);
							i--;
						}
					}
					sector.put(name, newsector);
				}
				else if(c == 'D'){
					int name = sc.nextInt();
					for(int i = 0; i < sector.get(name).size(); i++){
						emptylist.add(sector.get(name).get(i));
					}
					Collections.sort(emptylist);
					sector.remove(name);
				}
				else if(c == 'R'){
					int sectornum = sc.nextInt();
					int ind = -1;
					for(int key: sector.keySet()){
						for(int i = 0; i < sector.get(key).size(); i++){
							Seg nowS = sector.get(key).get(i);
							if(nowS.start <= sectornum && sectornum <= nowS.end){
								ind = key;
								break;
							}
						}
						if(ind != -1) break;
					}
					System.out.println(ind);
				}
			}
			System.out.println();
		}
	}

	private void debug(Object... o) {
		System.out.println("debug = " + Arrays.deepToString(o));
	}

	public static void main(String[] args) {
		new Main().doit();
	}
}